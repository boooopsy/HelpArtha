/**
 * Whetstone FSRS-6 Spaced-Repetition Scheduler (Pure JavaScript)
 * Pinned against open-spaced-repetition/py-fsrs 6.3.2 and app/src/Scheduler/Fsrs.php
 */
(function (root, factory) {
    if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.Fsrs = factory();
    }
}(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    const AGAIN = 1;
    const HARD  = 2;
    const GOOD  = 3;
    const EASY  = 4;

    const RATINGS = { [AGAIN]: 'again', [HARD]: 'hard', [GOOD]: 'good', [EASY]: 'easy' };
    const BANDS   = { 'worked': 0, 'faded': 1, 'independent': 2 };

    const DEFAULT_WEIGHTS = [
        0.212,  1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194, 0.001,
        1.8722, 0.1666, 0.796,  1.4835, 0.0614, 0.2629, 1.6483, 0.6014,
        1.8729, 0.5425, 0.0912, 0.0658, 0.1542
    ];

    const FUZZ_RANGES = [
        { start: 2.5,  end: 7.0,      factor: 0.15 },
        { start: 7.0,  end: 20.0,     factor: 0.10 },
        { start: 20.0, end: Infinity, factor: 0.05 }
    ];

    function pyRound(x) {
        const floor = Math.floor(x);
        const frac = x - floor;
        if (Math.abs(frac - 0.5) < 1e-12) {
            return (floor % 2 === 0) ? floor : floor + 1;
        }
        return Math.floor(x + 0.5);
    }

    class FsrsParams {
        constructor(options = {}) {
            const w = options.weights || DEFAULT_WEIGHTS;
            if (w.length !== 21) {
                throw new Error('FSRS-6 requires exactly 21 weights, got ' + w.length);
            }
            this.w = w.map(Number);
            this.desiredRetention = Number(options.desiredRetention ?? 0.9);
            if (this.desiredRetention <= 0 || this.desiredRetention >= 1) {
                throw new Error('desiredRetention must be in (0,1)');
            }
            this.learningSteps = options.learningSteps ?? [1, 10];
            this.relearningSteps = options.relearningSteps ?? [10];
            this.maximumInterval = Number(options.maximumInterval ?? 36500);
            this.enableFuzz = Boolean(options.enableFuzz ?? false);
            this.bandFadedDays = Number(options.bandFadedDays ?? 7.0);
            this.bandIndependentDays = Number(options.bandIndependentDays ?? 21.0);

            this.decay = -this.w[20];
            this.factor = Math.pow(0.9, 1.0 / this.decay) - 1.0;
        }
    }

    let defaultParams = new FsrsParams();

    function initialStability(p, rating) {
        return p.w[rating - 1];
    }

    function initialDifficulty(p, rating) {
        return p.w[4] - Math.exp(p.w[5] * (rating - 1)) + 1.0;
    }

    function clampDifficulty(d) {
        return Math.min(Math.max(d, 1.0), 10.0);
    }

    function clampStability(s) {
        return s === null || s === undefined ? null : Math.max(s, 0.001);
    }

    function nextDifficulty(p, difficulty, rating) {
        const arg1 = initialDifficulty(p, EASY);
        const deltaD = -(p.w[6] * (rating - 3));
        const arg2 = difficulty + ((10.0 - difficulty) * deltaD / 9.0);
        const next = p.w[7] * arg1 + (1.0 - p.w[7]) * arg2;
        return clampDifficulty(next);
    }

    function shortTermStability(p, stability, rating) {
        let inc = Math.exp(p.w[17] * (rating - 3 + p.w[18])) * Math.pow(stability, -p.w[19]);
        if (rating === GOOD || rating === EASY) {
            inc = Math.max(inc, 1.0);
        }
        return clampStability(stability * inc);
    }

    function retrievability(p, stability, elapsed) {
        if (stability === null || stability === undefined || elapsed === null || elapsed === undefined) {
            return 0.0;
        }
        const e = Math.max(0, elapsed);
        return Math.pow(1.0 + p.factor * e / stability, p.decay);
    }

    function nextIntervalDays(p, stability) {
        const days = (stability / p.factor) * (Math.pow(p.desiredRetention, 1.0 / p.decay) - 1.0);
        const rounded = pyRound(days);
        return Math.max(1, Math.min(rounded, p.maximumInterval));
    }

    function nextForgetStability(p, d, s, r) {
        const longTerm = p.w[11]
            * Math.pow(d, -p.w[12])
            * (Math.pow(s + 1.0, p.w[13]) - 1.0)
            * Math.exp((1.0 - r) * p.w[14]);
        const shortTerm = s / Math.exp(p.w[17] * p.w[18]);
        return Math.min(longTerm, shortTerm);
    }

    function nextRecallStability(p, d, s, r, rating) {
        const hardPenalty = rating === HARD ? p.w[15] : 1.0;
        const easyBonus   = rating === EASY ? p.w[16] : 1.0;
        return s * (1.0
            + Math.exp(p.w[8])
            * (11.0 - d)
            * Math.pow(s, -p.w[9])
            * (Math.exp((1.0 - r) * p.w[10]) - 1.0)
            * hardPenalty
            * easyBonus);
    }

    function nextStability(p, difficulty, stability, r, rating) {
        const s = (rating === AGAIN)
            ? nextForgetStability(p, difficulty, stability, r)
            : nextRecallStability(p, difficulty, stability, r, rating);
        return clampStability(s);
    }

    function bandFor(p, stability) {
        if (stability === null || stability === undefined || stability < p.bandFadedDays) {
            return 'worked';
        }
        return (stability < p.bandIndependentDays) ? 'faded' : 'independent';
    }

    function nextBand(p, current, stability, lapsed) {
        if (lapsed) return 'worked';
        const target = bandFor(p, stability);
        const curLevel = BANDS[current] ?? 0;
        return (BANDS[target] >= curLevel) ? target : current;
    }

    function stepMachine(p, steps, cardState, step, rating, stability) {
        step = step ?? 0;
        const n = steps.length;
        if (n === 0 || (step >= n && rating !== AGAIN)) {
            return ['review', null, nextIntervalDays(p, stability) * 86400];
        }

        switch (rating) {
            case AGAIN:
                return [cardState, 0, steps[0] * 60];
            case HARD: {
                let secs = 0;
                if (step === 0 && n === 1) {
                    secs = Math.round(steps[0] * 60 * 1.5);
                } else if (step === 0 && n >= 2) {
                    secs = Math.round((steps[0] + steps[1]) * 60 / 2.0);
                } else {
                    secs = steps[step] * 60;
                }
                return [cardState, step, secs];
            }
            case GOOD:
                if (step + 1 === n) {
                    return ['review', null, nextIntervalDays(p, stability) * 86400];
                }
                return [cardState, step + 1, steps[step + 1] * 60];
            case EASY:
            default:
                return ['review', null, nextIntervalDays(p, stability) * 86400];
        }
    }

    function updateMemory(p, stability, difficulty, rating, daysSince, elapsedDays) {
        if (stability === null || stability === undefined || difficulty === null || difficulty === undefined) {
            return [
                clampStability(initialStability(p, rating)),
                clampDifficulty(initialDifficulty(p, rating))
            ];
        }
        if (daysSince !== null && daysSince < 1) {
            return [
                shortTermStability(p, stability, rating),
                nextDifficulty(p, difficulty, rating)
            ];
        }
        return [
            nextStability(p, difficulty, stability, retrievability(p, stability, daysSince), rating),
            nextDifficulty(p, difficulty, rating)
        ];
    }

    function schedule(state, rating, elapsedDays, params = null, fuzz = null) {
        if (rating < 1 || rating > 4) {
            throw new Error('Rating must be between 1 and 4');
        }
        const p = params || defaultParams;

        let cardState  = state.state || 'new';
        let stability  = (state.stability !== null && state.stability !== undefined) ? Number(state.stability) : null;
        let difficulty = (state.difficulty !== null && state.difficulty !== undefined) ? Number(state.difficulty) : null;
        let step       = (state.step !== null && state.step !== undefined) ? Number(state.step) : null;
        let reps       = Number(state.reps || 0);
        let lapses     = Number(state.lapses || 0);
        const bandIn   = state.band || 'worked';
        let hasHistory = Boolean(state.last_review);

        if (cardState === 'new') {
            cardState = 'learning';
            step = 0;
            stability = null;
            difficulty = null;
            hasHistory = false;
        }
        if (cardState === 'learning' || cardState === 'relearning') {
            if (step === null) step = 0;
        }

        const daysSince = hasHistory ? Math.floor(Math.max(0.0, elapsedDays)) : null;
        let lapsed = false;
        let intervalSeconds = 0;

        switch (cardState) {
            case 'learning': {
                const [newS, newD] = updateMemory(p, stability, difficulty, rating, daysSince, elapsedDays);
                stability = newS;
                difficulty = newD;
                const [newState, newStep, newSecs] = stepMachine(p, p.learningSteps, cardState, step, rating, stability);
                cardState = newState;
                step = newStep;
                intervalSeconds = newSecs;
                break;
            }
            case 'review': {
                if (stability === null || difficulty === null) {
                    throw new Error('A review-state concept must carry stability and difficulty');
                }
                if (daysSince !== null && daysSince < 1) {
                    stability = shortTermStability(p, stability, rating);
                } else {
                    stability = nextStability(p, difficulty, stability, retrievability(p, stability, daysSince), rating);
                }
                difficulty = nextDifficulty(p, difficulty, rating);

                if (rating === AGAIN) {
                    lapses++;
                    lapsed = true;
                    if (p.relearningSteps.length === 0) {
                        intervalSeconds = nextIntervalDays(p, stability) * 86400;
                    } else {
                        cardState = 'relearning';
                        step = 0;
                        intervalSeconds = p.relearningSteps[0] * 60;
                    }
                } else {
                    intervalSeconds = nextIntervalDays(p, stability) * 86400;
                }
                break;
            }
            case 'relearning': {
                if (stability === null || difficulty === null) {
                    throw new Error('A relearning concept must carry stability and difficulty');
                }
                const [newS, newD] = updateMemory(p, stability, difficulty, rating, daysSince, elapsedDays);
                stability = newS;
                difficulty = newD;
                const [newState, newStep, newSecs] = stepMachine(p, p.relearningSteps, cardState, step, rating, stability);
                cardState = newState;
                step = newStep;
                intervalSeconds = newSecs;
                break;
            }
            default:
                throw new Error('Unknown state: ' + cardState);
        }

        stability = clampStability(stability);
        difficulty = (difficulty === null) ? null : clampDifficulty(difficulty);
        reps++;

        return {
            state: cardState,
            step: step,
            stability: stability,
            difficulty: difficulty,
            band: nextBand(p, bandIn, stability, lapsed),
            reps: reps,
            lapses: lapses,
            lapsed: lapsed,
            rating: rating,
            elapsed_days: elapsedDays,
            scheduled_days: intervalSeconds / 86400.0,
            interval_seconds: intervalSeconds
        };
    }

    function elapsedDays(lastReviewStr, nowDate = new Date()) {
        if (!lastReviewStr) return 0.0;
        const then = new Date(lastReviewStr.endsWith('Z') ? lastReviewStr : lastReviewStr + 'Z');
        const diffMs = nowDate.getTime() - then.getTime();
        return Math.max(0.0, diffMs / 86400000.0);
    }

    function review(state, rating, nowDate = new Date(), p = null) {
        const elapsed = elapsedDays(state.last_review, nowDate);
        const out = schedule(state, rating, elapsed, p);
        const due = new Date(nowDate.getTime() + out.interval_seconds * 1000);
        out.due_at = due.toISOString().replace('T', ' ').substring(0, 19);
        out.last_review = nowDate.toISOString().replace('T', ' ').substring(0, 19);
        return out;
    }

    function preview(state, nowDate = new Date(), p = null) {
        const out = {};
        for (let r = 1; r <= 4; r++) {
            out[r] = review(state, r, nowDate, p);
        }
        return out;
    }

    function freshState(conceptUid) {
        return {
            concept_uid: conceptUid,
            state: 'new',
            step: null,
            stability: null,
            difficulty: null,
            band: 'worked',
            reps: 0,
            lapses: 0,
            last_review: null,
            due_at: null,
            suspended: 0
        };
    }

    function formatInterval(seconds) {
        if (seconds < 60) return `${seconds}s`;
        const minutes = Math.round(seconds / 60);
        if (minutes < 60) return `${minutes}m`;
        const hours = Math.round(seconds / 3600);
        if (hours < 24) return `${hours}h`;
        const days = Math.round(seconds / 86400);
        if (days < 30) return `${days}d`;
        const months = +(days / 30.4).toFixed(1);
        if (days < 365) return `${months}mo`;
        const years = +(days / 365).toFixed(1);
        return `${years}y`;
    }

    return {
        AGAIN, HARD, GOOD, EASY,
        RATINGS, BANDS,
        DEFAULT_WEIGHTS,
        FsrsParams,
        schedule,
        review,
        preview,
        freshState,
        elapsedDays,
        nextIntervalDays,
        bandFor,
        formatInterval,
        setParams: (p) => { defaultParams = p; },
        getParams: () => defaultParams
    };
}));

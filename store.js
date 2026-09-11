/**
 * Whetstone Client-Side State Management & Persistence Store
 * Manages user accounts, credentials, concept states, study logs, and JSON export/import.
 */
(function (root, factory) {
    const fsrsModule = (typeof Fsrs !== 'undefined') ? Fsrs : ((typeof require !== 'undefined') ? require('./fsrs.js') : (root ? root.Fsrs : null));
    const inst = factory(fsrsModule);
    if (typeof module === 'object' && module.exports) {
        module.exports = inst;
    }
    if (typeof root !== 'undefined') {
        root.WhetstoneStore = inst;
    }
    if (typeof window !== 'undefined') {
        window.WhetstoneStore = inst;
    }
}(typeof self !== 'undefined' ? self : this, function (Fsrs) {
    'use strict';

    const STORAGE_KEY_ACCOUNTS = 'whetstone_accounts';
    const STORAGE_KEY_ACTIVE_USER = 'whetstone_active_user';
    const STORAGE_KEY_USER_PREFIX = 'whetstone_user_state_';

    function getStoredAccounts() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY_ACCOUNTS);
            return raw ? JSON.parse(raw) : [];
        } catch (e) {
            console.error('Failed to read accounts from localStorage', e);
            return [];
        }
    }

    function saveStoredAccounts(accounts) {
        try {
            localStorage.setItem(STORAGE_KEY_ACCOUNTS, JSON.stringify(accounts));
        } catch (e) {
            console.error('Failed to save accounts to localStorage', e);
        }
    }

    function getActiveUserId() {
        try {
            return localStorage.getItem(STORAGE_KEY_ACTIVE_USER) || null;
        } catch (e) {
            return null;
        }
    }

    function setActiveUserId(userId) {
        try {
            if (userId) {
                localStorage.setItem(STORAGE_KEY_ACTIVE_USER, userId);
            } else {
                localStorage.removeItem(STORAGE_KEY_ACTIVE_USER);
            }
        } catch (e) {}
    }

    function defaultUserState(userId, username) {
        return {
            userId: userId,
            username: username,
            createdAt: new Date().toISOString(),
            settings: {
                track: '365', // 90, 180, 365
                newCap: 20,
                reviewCap: 100,
                rolloverHour: 4, // 4 AM local time
                textScale: 1.0,  // 1.0, 1.15, 1.3, 1.5
                theme: 'auto',   // 'auto', 'light', 'dark'
                densityMode: 'apprentice' // 'apprentice', 'master'
            },
            streaks: {
                current: 0,
                longest: 0,
                freezes: 2,
                lastStudyDate: null
            },
            dailyCounts: {},      // { 'YYYY-MM-DD': { new: 0, review: 0 } }
            conceptStates: {},    // { [conceptUid]: { state, step, stability, difficulty, band, reps, lapses, last_review, due_at } }
            readConcepts: {},     // { [conceptUid]: { readAt: string, verified: true } }
            readModules: {},      // { [moduleDir]: { readAt: string, verified: true } }
            attempts: [],         // list of review logs
            projectNotes: {},     // { [projectSlug]: { notes: '', status: 'not_started'|'in_progress'|'done' } }
            artifacts: []         // logged portfolio items
        };
    }

    class Store {
        constructor() {
            this.accounts = getStoredAccounts();
            this.activeUserId = getActiveUserId();
            this.currentUser = null;
            this.state = null;

            // Ensure a default guest account exists if no accounts
            if (this.accounts.length === 0) {
                const defaultUser = {
                    id: 'usr_kumar',
                    username: 'Kumar',
                    password: 'password123',
                    createdAt: new Date().toISOString()
                };
                this.accounts.push(defaultUser);
                saveStoredAccounts(this.accounts);
                this.activeUserId = defaultUser.id;
                setActiveUserId(this.activeUserId);
            }

            this.initSession();
        }

        initSession() {
            if (this.activeUserId) {
                this.currentUser = this.accounts.find(a => a.id === this.activeUserId) || null;
            }
            if (!this.currentUser && this.accounts.length > 0) {
                this.currentUser = this.accounts[0];
                this.activeUserId = this.currentUser.id;
                setActiveUserId(this.activeUserId);
            }

            if (this.currentUser) {
                this.loadUserState(this.currentUser.id);
            } else {
                // Guest mode
                this.state = defaultUserState('guest', 'Guest');
            }
        }

        loadUserState(userId) {
            try {
                const raw = localStorage.getItem(STORAGE_KEY_USER_PREFIX + userId);
                if (raw) {
                    this.state = JSON.parse(raw);
                } else {
                    this.state = defaultUserState(userId, this.currentUser?.username || 'User');
                    this.saveUserState();
                }
            } catch (e) {
                console.error('Failed to load user state', e);
                this.state = defaultUserState(userId, this.currentUser?.username || 'User');
            }
        }

        saveUserState() {
            if (!this.state || !this.state.userId) return;
            try {
                localStorage.setItem(STORAGE_KEY_USER_PREFIX + this.state.userId, JSON.stringify(this.state));
            } catch (e) {
                console.error('Failed to save state to localStorage', e);
            }
        }

        // Account management
        createAccount(username, password) {
            const cleanName = (username || '').trim();
            if (!cleanName) throw new Error('Username cannot be empty');

            const existing = this.accounts.find(a => a.username.toLowerCase() === cleanName.toLowerCase());
            if (existing) throw new Error(`User "${cleanName}" already exists`);

            const id = 'usr_' + Date.now().toString(36) + Math.random().toString(36).substring(2, 6);
            const newAcc = {
                id: id,
                username: cleanName,
                password: password || '',
                createdAt: new Date().toISOString()
            };

            this.accounts.push(newAcc);
            saveStoredAccounts(this.accounts);

            // Switch to new user
            this.activeUserId = id;
            setActiveUserId(id);
            this.currentUser = newAcc;
            this.state = defaultUserState(id, cleanName);
            this.saveUserState();

            return newAcc;
        }

        login(username, password) {
            const cleanName = (username || '').trim();
            const acc = this.accounts.find(a => a.username.toLowerCase() === cleanName.toLowerCase());
            if (!acc) throw new Error(`Account "${cleanName}" not found`);
            if (acc.password && acc.password !== password) {
                throw new Error('Incorrect password');
            }

            this.activeUserId = acc.id;
            setActiveUserId(acc.id);
            this.currentUser = acc;
            this.loadUserState(acc.id);
            return acc;
        }

        switchUser(userId) {
            const acc = this.accounts.find(a => a.id === userId);
            if (!acc) throw new Error('User not found');
            this.activeUserId = acc.id;
            setActiveUserId(acc.id);
            this.currentUser = acc;
            this.loadUserState(acc.id);
        }

        loginGuest() {
            this.activeUserId = null;
            setActiveUserId(null);
            this.currentUser = null;
            this.state = defaultUserState('guest', 'Guest');
        }

        isGuest() {
            return !this.currentUser || this.currentUser.id === 'guest';
        }

        // Study Day & Date calculation
        getStudyDate(dateObj = new Date()) {
            const rolloverHour = this.state.settings.rolloverHour || 4;
            const d = new Date(dateObj);
            // If current hour is before rollover hour, it counts as yesterday's study day
            if (d.getHours() < rolloverHour) {
                d.setDate(d.getDate() - 1);
            }
            const y = d.getFullYear();
            const m = String(d.getMonth() + 1).padStart(2, '0');
            const day = String(d.getDate()).padStart(2, '0');
            return `${y}-${m}-${day}`;
        }

        getTodayCounts() {
            const dateStr = this.getStudyDate();
            return this.state.dailyCounts[dateStr] || { new: 0, review: 0 };
        }

        // Reading Verification Helpers (Explicit Button Verification)
        isConceptRead(conceptUid) {
            if (!this.state || !this.state.readConcepts) return false;
            return !!this.state.readConcepts[conceptUid];
        }

        markConceptRead(conceptUid) {
            if (!this.state.readConcepts) this.state.readConcepts = {};
            this.state.readConcepts[conceptUid] = {
                readAt: new Date().toISOString(),
                verified: true
            };
            this.saveUserState();
        }

        unmarkConceptRead(conceptUid) {
            if (this.state.readConcepts && this.state.readConcepts[conceptUid]) {
                delete this.state.readConcepts[conceptUid];
                this.saveUserState();
            }
        }

        isModuleRead(moduleDir) {
            if (!this.state || !this.state.readModules) return false;
            return !!this.state.readModules[moduleDir];
        }

        markModuleRead(moduleDir) {
            if (!this.state.readModules) this.state.readModules = {};
            this.state.readModules[moduleDir] = {
                readAt: new Date().toISOString(),
                verified: true
            };
            this.saveUserState();
        }

        unmarkModuleRead(moduleDir) {
            if (this.state.readModules && this.state.readModules[moduleDir]) {
                delete this.state.readModules[moduleDir];
                this.saveUserState();
            }
        }

        arePrereqsSatisfied(concept, dataBundle) {
            if (!concept.prereqs || concept.prereqs.length === 0) return true;
            if (!dataBundle) return true;

            for (const prereqStr of concept.prereqs) {
                let targetDom = null;
                let targetTitle = prereqStr;
                if (prereqStr.includes(':')) {
                    const parts = prereqStr.split(':');
                    targetDom = parts[0].trim();
                    targetTitle = parts[1].trim();
                }

                let reqUid = null;
                if (targetDom && dataBundle.conceptsByTitle) {
                    reqUid = dataBundle.conceptsByTitle[`${targetDom}:${targetTitle}`];
                }
                if (!reqUid && dataBundle.conceptsByTitle) {
                    reqUid = dataBundle.conceptsByTitle[targetTitle];
                }

                if (reqUid) {
                    const isRead = this.isConceptRead(reqUid);
                    const s = this.state.conceptStates[reqUid];
                    const isMastered = s && s.reps > 0;
                    if (!isRead && !isMastered) {
                        return false;
                    }
                }
            }
            return true;
        }

        // Concept State helpers
        getConceptState(conceptUid) {
            if (!this.state.conceptStates[conceptUid]) {
                this.state.conceptStates[conceptUid] = Fsrs.freshState(conceptUid);
            }
            return this.state.conceptStates[conceptUid];
        }

        recordAttempt(conceptUid, rating, confidence = 2, elapsedSec = 10, templateIndex = 0) {
            const now = new Date();
            const nowIso = now.toISOString().replace('T', ' ').substring(0, 19);
            const currentState = this.getConceptState(conceptUid);
            const bandBefore = currentState.band;
            const stabilityBefore = currentState.stability;
            const wasNew = (currentState.state === 'new');

            // Compute next FSRS state
            const nextState = Fsrs.review(currentState, rating, now);

            // Update concept state
            this.state.conceptStates[conceptUid] = {
                concept_uid: conceptUid,
                state: nextState.state,
                step: nextState.step,
                stability: nextState.stability,
                difficulty: nextState.difficulty,
                band: nextState.band,
                reps: nextState.reps,
                lapses: nextState.lapses,
                last_review: nextState.last_review,
                due_at: nextState.due_at,
                suspended: currentState.suspended || 0
            };

            // Log attempt
            this.state.attempts.push({
                concept_uid: conceptUid,
                rating: rating,
                confidence: confidence,
                elapsed_sec: elapsedSec,
                band_before: bandBefore,
                band_after: nextState.band,
                stability_before: stabilityBefore,
                stability_after: nextState.stability,
                timestamp: nowIso
            });

            // Update daily counts
            const studyDate = this.getStudyDate(now);
            if (!this.state.dailyCounts[studyDate]) {
                this.state.dailyCounts[studyDate] = { new: 0, review: 0 };
            }
            if (wasNew) {
                this.state.dailyCounts[studyDate].new += 1;
            } else {
                this.state.dailyCounts[studyDate].review += 1;
            }

            // Update streaks
            this.updateStreak(studyDate);

            // Persist
            this.saveUserState();

            return nextState;
        }

        updateStreak(studyDate) {
            const streaks = this.state.streaks;
            if (streaks.lastStudyDate === studyDate) {
                return; // already counted today
            }

            if (!streaks.lastStudyDate) {
                streaks.current = 1;
                streaks.longest = 1;
                streaks.lastStudyDate = studyDate;
                return;
            }

            const lastDate = new Date(streaks.lastStudyDate);
            const currentDate = new Date(studyDate);
            const diffDays = Math.round((currentDate - lastDate) / (1000 * 60 * 60 * 24));

            if (diffDays === 1) {
                streaks.current += 1;
            } else if (diffDays > 1) {
                const missedDays = diffDays - 1;
                if (streaks.freezes >= missedDays) {
                    streaks.freezes -= missedDays;
                    streaks.current += 1; // preserved by freezes!
                } else {
                    streaks.current = 1; // reset streak
                }
            }

            if (streaks.current > streaks.longest) {
                streaks.longest = streaks.current;
            }
            streaks.lastStudyDate = studyDate;
        }

        // Queue generation
        buildStudyQueue(dataBundle) {
            const now = new Date();
            const nowIso = now.toISOString().replace('T', ' ').substring(0, 19);
            const counts = this.getTodayCounts();
            const newCap = this.state.settings.newCap || 20;
            const reviewCap = this.state.settings.reviewCap || 100;

            const remainingNew = Math.max(0, newCap - counts.new);
            const remainingReview = Math.max(0, reviewCap - counts.review);

            const reviewsDue = [];
            const newCandidates = [];
            const readingQueue = [];

            // Traverse all concepts in curriculum order
            for (const domain of (dataBundle.domains || [])) {
                for (const section of (domain.sections || [])) {
                    for (const concept of (section.concepts || [])) {
                        const uid = concept.uid;
                        if (!uid) continue;

                        const s = this.state.conceptStates[uid];
                        const isRead = this.isConceptRead(uid);
                        const prereqsMet = this.arePrereqsSatisfied(concept, dataBundle);

                        if (!s || s.state === 'new') {
                            if (isRead && prereqsMet) {
                                // User has read and verified understanding -> ready for testing!
                                newCandidates.push(concept);
                            } else if (!isRead && prereqsMet) {
                                // Prerequisites met, ready for reading in the textbook!
                                readingQueue.push(concept);
                            }
                        } else if (!s.suspended && s.due_at && s.due_at <= nowIso) {
                            // Calculate urgency based on retrievability
                            const elapsed = Fsrs.elapsedDays(s.last_review, now);
                            const r = Fsrs.retrievabilityOf ? Fsrs.retrievabilityOf(s.stability, elapsed) : 0;
                            reviewsDue.push({ concept, state: s, retrievability: r });
                        }
                    }
                }
            }

            // Reviews sorted by lowest retrievability (most urgently forgotten first)
            reviewsDue.sort((a, b) => a.retrievability - b.retrievability);

            const selectedReviews = reviewsDue.slice(0, remainingReview).map(item => item.concept);
            const selectedNew = newCandidates.slice(0, remainingNew);

            return {
                reviewsDue: selectedReviews,
                newConcepts: selectedNew,
                readingQueue: readingQueue.slice(0, 20),
                totalReviewsDueCount: reviewsDue.length,
                totalNewAvailable: newCandidates.length,
                totalReadingAvailable: readingQueue.length,
                remainingNewCap: remainingNew,
                remainingReviewCap: remainingReview
            };
        }

        // Export state as downloadable JSON file
        exportStateJson() {
            const exportData = {
                app: 'Whetstone',
                exportedAt: new Date().toISOString(),
                accounts: this.accounts,
                activeUserId: this.activeUserId,
                state: this.state
            };
            return JSON.stringify(exportData, null, 2);
        }

        // Download JSON backup file directly in the browser
        downloadBackup() {
            const jsonStr = this.exportStateJson();
            const username = this.currentUser ? this.currentUser.username : 'guest';
            const filename = `whetstone-backup-${username}-${this.getStudyDate()}.json`;
            const blob = new Blob([jsonStr], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        // Restore state from JSON string
        importStateJson(jsonString) {
            try {
                const parsed = JSON.parse(jsonString);
                if (!parsed || !parsed.state) {
                    throw new Error('Invalid Whetstone backup format');
                }

                if (parsed.accounts && Array.isArray(parsed.accounts)) {
                    this.accounts = parsed.accounts;
                    saveStoredAccounts(this.accounts);
                }

                if (parsed.activeUserId) {
                    this.activeUserId = parsed.activeUserId;
                    setActiveUserId(this.activeUserId);
                    this.currentUser = this.accounts.find(a => a.id === this.activeUserId) || null;
                }

                this.state = parsed.state;
                this.saveUserState();
                return true;
            } catch (e) {
                console.error('Import failed', e);
                throw e;
            }
        }
    }

    return new Store();
}));

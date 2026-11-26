-- LifeOS database schema
-- Track 3: Know Thyself

-- Table for storing daily habit entries
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    habit_name TEXT NOT NULL,
    completed INTEGER NOT NULL,
    notes TEXT
);

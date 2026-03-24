-- 1. Total matches
SELECT COUNT(*) FROM cricket_matches;

-- 2. Matches per team
SELECT team1, COUNT(*) FROM cricket_matches GROUP BY team1;

-- 3. Matches per venue
SELECT venue, COUNT(*) FROM cricket_matches GROUP BY venue;

-- 4. Daily matches
SELECT match_date, COUNT(*) FROM cricket_matches GROUP BY match_date;

-- 5. Top teams
SELECT team1, COUNT(*) as total_matches
FROM cricket_matches
GROUP BY team1
ORDER BY total_matches DESC;

-- 6. Unique venues
SELECT DISTINCT venue FROM cricket_matches;

-- 7. Matches involving a team
SELECT * FROM cricket_matches WHERE team1 = 'India';

-- 8. Matches count per team1-team2 combo
SELECT team1, team2, COUNT(*) 
FROM cricket_matches
GROUP BY team1, team2;

-- 9. Most active venue
SELECT venue, COUNT(*) as matches
FROM cricket_matches
GROUP BY venue
ORDER BY matches DESC;

-- 10. Matches per date sorted
SELECT match_date, COUNT(*) 
FROM cricket_matches
GROUP BY match_date
ORDER BY match_date;
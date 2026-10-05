-- event_attendance.sql
-- Sample SQL: creates a small table of home events and
-- summarizes attendance by sport.

CREATE TABLE events (
    event_id    INT PRIMARY KEY,
    sport       VARCHAR(30),
    opponent    VARCHAR(50),
    event_date  DATE,
    attendance  INT,
    capacity    INT
);

INSERT INTO events (event_id, sport, opponent, event_date, attendance, capacity) VALUES
(1, 'Football',   'Opponent A', '2026-09-05', 69250, 69250),
(2, 'Football',   'Opponent B', '2026-09-19', 68400, 69250),
(3, 'Volleyball', 'Opponent C', '2026-09-12',  2100,  3000),
(4, 'Volleyball', 'Opponent D', '2026-09-26',  2650,  3000),
(5, 'Soccer',     'Opponent E', '2026-09-14',  1200,  2000);

-- Average attendance and percent of capacity filled, by sport
SELECT
    sport,
    COUNT(*)                                        AS games,
    ROUND(AVG(attendance), 0)                       AS avg_attendance,
    ROUND(100.0 * SUM(attendance) / SUM(capacity), 1) AS pct_capacity
FROM events
GROUP BY sport
ORDER BY avg_attendance DESC;

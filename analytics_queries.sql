-- Total events
SELECT COUNT(*) FROM events;

-- Event distribution
SELECT event, COUNT(*)
FROM events
GROUP BY event
ORDER BY COUNT(*) DESC;

-- User activity counts
SELECT user_id, COUNT(*)
FROM events
GROUP BY user_id
ORDER BY user_id;

-- Purchase events only
SELECT *
FROM events
WHERE event = 'purchase';

-- Most active users
SELECT user_id, COUNT(*) AS total_events
FROM events
GROUP BY user_id
ORDER BY total_events DESC;
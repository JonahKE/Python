SELECT CONCAT(users.first_name, " ", users.last_name) AS user_name, CONCAT(user2.first_name, " ", user2.last_name) AS friend_name FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
ORDER BY users.last_name, user2.last_name;
DROP DATABASE IF EXISTS mubi_data;
CREATE DATABASE IF NOT EXISTS mubi_data;
USE mubi_data;

DROP TABLE IF EXISTS movie;
CREATE TABLE movie (
	movie_id VARCHAR(255) PRIMARY KEY, 
	movie_title VARCHAR(255), 
	movie_release_year FLOAT, 
	movie_url VARCHAR(255), 
	movie_title_language VARCHAR(255), 
	movie_popularity INT, 
	movie_image_url VARCHAR(255), 
	director_id TEXT, 
	director_name TEXT,
	director_url TEXT,
    average_rating FLOAT
);

DROP TABLE IF EXISTS rating;
CREATE TABLE rating (
    movie_id VARCHAR(255), 
    rating_id VARCHAR(255) PRIMARY KEY, 
    rating_url VARCHAR(255), 
    rating_score FLOAT,
    rating_timestamp_utc TIMESTAMP, 
    critic TEXT, 
    critic_likes INT, 
    critic_comments INT, 
    user_id VARCHAR(255), 
    user_trialist BOOLEAN, 
    user_subscriber BOOLEAN,
    user_eligible_for_trial BOOLEAN, 
    user_has_payment_method BOOLEAN,
	FOREIGN KEY (movie_id) REFERENCES movie(movie_id)
);


INSERT INTO movie (movie_id, movie_title, movie_release_year, movie_url, movie_title_language, movie_popularity, movie_image_url, director_id, director_name, director_url, average_rating) VALUES ("9000000000", "Movie test Rad", 2022.0, "http://mubi.com/films/claires-knee", "en", 674, "https://images.mubicdn.net/images/film/793/cache-8371-1546689614/image-w1280.jpg", "1057", "Éric Rohmer", "http://mubi.com/cast/eric-rohmer", 0); 
INSERT INTO rating (movie_id, rating_id, rating_url, rating_score, rating_timestamp_utc, critic, critic_likes, critic_comments, user_id, user_trialist, user_subscriber, user_eligible_for_trial, user_has_payment_method) VALUES ("9000000000", "10704606", "http://mubi.com/films/pavee-lackeen-the-traveller-girl/ratings/10704606", 2.0, "2014-08-15 23:42:31", "", 0, 0, "85981819", True, True, False, True); 

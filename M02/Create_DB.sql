CREATE DATABASE Zelda;
USE Zelda;

CREATE TABLE game (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name CHAR(50) NOT NULL,
    date_started DATETIME NOT NULL,
    hearts_remaining INT DEFAULT 3,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region CHAR(20) NOT NULL
);

CREATE TABLE game_food (
    game_id INT NOT NULL,
    food_name CHAR(15) NOT NULL,
    quantity_remaining INT,
    PRIMARY KEY (game_id, food_name)
);

CREATE TABLE game_weapons (
    game_id INT NOT NULL,
    weapon_name CHAR(15) NOT NULL,
    equipped BOOLEAN DEFAULT FALSE,
    lives_remaining INT,
    PRIMARY KEY (game_id, weapon_name)
);

CREATE TABLE game_enemies (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    lives_remaining INT,
    PRIMARY KEY (game_id, region, num)
);

CREATE TABLE game_sanctuaries_opened (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    PRIMARY KEY (game_id, region, num)
);

CREATE TABLE game_chests_opened (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    PRIMARY KEY (game_id, region, num)
);
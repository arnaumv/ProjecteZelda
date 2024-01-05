CREATE DATABASE Zelda;
USE Zelda;

CREATE TABLE game (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name CHAR(50) NOT NULL,
    date_started DATE NOT NULL,
    hearts_remaining INT DEFAULT 3,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region CHAR(20) NOT NULL CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'))
);


CREATE TABLE game_food (
    game_id INT NOT NULL,
    food_name CHAR(15) NOT NULL CHECK (food_name IN ('Vegetables','Fish','Meat','Salads','Pescatarian','Roasted')),
    quantity_remaining INT,
    PRIMARY KEY (game_id, food_name),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE game_weapons (
    game_id INT NOT NULL,
    weapon_name CHAR(15) NOT NULL CHECK (weapon_name IN ('Wood Sword','Sword','Wood Shield','Shield')),
    equipped BOOLEAN DEFAULT FALSE,
    lives_remaining INT,
    PRIMARY KEY (game_id, weapon_name),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);


CREATE TABLE game_enemies (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle')),
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    lives_remaining INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE game_sanctuaries_opened (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle')),
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE game_chests_opened (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle')),
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

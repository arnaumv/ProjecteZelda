USE Zelda;

-- Restricciones para la tabla game
ALTER TABLE game
    ADD CONSTRAINT check_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

-- Restricciones para la tabla game_food
ALTER TABLE game_food
    ADD FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_food_name CHECK (food_name IN ('Vegetables','Fish','Meat','Salads','Pescatarian','Roasted'));

-- Restricciones para la tabla game_weapons
ALTER TABLE game_weapons
    ADD FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_weapon_name CHECK (weapon_name IN ('Wood Sword','Sword','Wood Shield','Shield'));

-- Restricciones para la tabla game_enemies
ALTER TABLE game_enemies
    ADD FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_enemies_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

-- Restricciones para la tabla game_sanctuaries_opened
ALTER TABLE game_sanctuaries_opened
    ADD FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_sanctuaries_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

-- Restricciones para la tabla game_chests_opened
ALTER TABLE game_chests_opened
    ADD FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_chests_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

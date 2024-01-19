ALTER TABLE game
    ADD CONSTRAINT check_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

-- Restricciones para la tabla game_food
ALTER TABLE game_food
    ADD CONSTRAINT fk_game_food_game FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_food_name CHECK (food_name IN ('Vegetables','Fish','Meat','Salads','Pescatarian','Roasted'));

-- Restricciones para la tabla game_weapons
ALTER TABLE game_weapons
    ADD CONSTRAINT fk_game_weapons_game FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_weapon_name CHECK (weapon_name IN ('Wood Sword','Sword','Wood Shield','Shield'));

-- Restricciones para la tabla game_enemies
ALTER TABLE game_enemies
    ADD CONSTRAINT fk_game_enemies_game FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_enemies_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

-- Restricciones para la tabla game_sanctuaries_opened
ALTER TABLE game_sanctuaries_opened
    ADD CONSTRAINT fk_game_sanctuaries_game FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_sanctuaries_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));

-- Restricciones para la tabla game_chests_opened
ALTER TABLE game_chests_opened
    ADD CONSTRAINT fk_game_chests_game FOREIGN KEY (game_id) REFERENCES game(game_id),
    ADD CONSTRAINT check_chests_region CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle'));
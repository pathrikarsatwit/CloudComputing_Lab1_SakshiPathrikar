-- Create and select database
CREATE DATABASE IF NOT EXISTS pokemon_shop;
USE pokemon_shop;

-- Create Pokemon table
CREATE TABLE Pokemon (
    pokemon_id INT AUTO_INCREMENT PRIMARY KEY,
    pokemon_name VARCHAR(100),
    pokemon_level INT
);

-- Create Type table
CREATE TABLE Type (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50),
    description VARCHAR(255),
    UNIQUE (type_name)  -- moved the unique constraint here directly
);

-- Create PokemonType table (many-to-many between Pokemon and Type)
CREATE TABLE PokemonType (
    pokemon_id INT,
    type_id INT,
    PRIMARY KEY (pokemon_id, type_id),
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(pokemon_id),
    FOREIGN KEY (type_id) REFERENCES Type(type_id)
);

-- Create SpecialAttacks table
CREATE TABLE SpecialAttacks (
    attack_id INT AUTO_INCREMENT PRIMARY KEY,
    attack_name VARCHAR(100),
    attack_power INT,
    attack_type_id INT,
    FOREIGN KEY (attack_type_id) REFERENCES Type(type_id)
);

-- Create PokemonSpecialAttacks table (many-to-many between Pokemon and SpecialAttacks)
CREATE TABLE PokemonSpecialAttacks (
    pokemon_id INT,
    attack_id INT,
    PRIMARY KEY (pokemon_id, attack_id),
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(pokemon_id),
    FOREIGN KEY (attack_id) REFERENCES SpecialAttacks(attack_id)
);

-- -----------------------------
-- Insert sample data
-- -----------------------------

-- Insert Types
INSERT INTO Type (type_id, type_name, description) VALUES
(1, 'Fire', 'Strong against Grass, weak against Water'),
(2, 'Water', 'Strong against Fire, weak against Electric'),
(3, 'Grass', 'Strong against Water, weak against Fire'),
(4, 'Electric', 'Strong against Water, weak against Ground');

-- Insert Pokemon
INSERT INTO Pokemon (pokemon_id, pokemon_name, pokemon_level) VALUES
(101, 'Charmander', 12),
(102, 'Squirtle', 10),
(103, 'Bulbasaur', 11),
(104, 'Pikachu', 15);

-- Assign Types to Pokemon
INSERT INTO PokemonType (pokemon_id, type_id) VALUES
(101, 1),
(102, 2),
(103, 3),
(104, 4);

-- Insert Special Attacks
INSERT INTO SpecialAttacks (attack_id, attack_name, attack_power, attack_type_id) VALUES
(201, 'Flamethrower', 90, 1),
(202, 'Water Gun', 40, 2),
(203, 'Vine Whip', 45, 3),
(204, 'Thunderbolt', 90, 4);

-- Assign Special Attacks to Pokemon
INSERT INTO PokemonSpecialAttacks (pokemon_id, attack_id) VALUES
(101, 201),
(102, 202),
(103, 203),
(104, 204);

ALTER TABLE pokemon ADD COLUMN image_filename VARCHAR(255);
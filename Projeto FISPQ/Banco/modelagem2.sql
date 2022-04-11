CREATE SCHEMA `DB_FISPQ`;

CREATE TABLE IF NOT EXISTS `DB_FISPQ`.`User` (
  `ID` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `celular` INT(15) NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NULL,
  `update_at` TIMESTAMP NULL,
  `permission_id` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `DB_FISPQ`.`Empresa` (
  `ID_empresa` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  `endereco` VARCHAR(500) NULL,
  `telefone` VARCHAR(45) NULL,
  `Telefone_emergencia` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_empresa`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `DB_FISPQ`.`User_has_Empresa` (
  `User_ID` INT NOT NULL,
  `Empresa_ID_empresa` INT NOT NULL,
  PRIMARY KEY (`User_ID`, `Empresa_ID_empresa`),
  INDEX `fk_User_has_Empresa_Empresa1_idx` (`Empresa_ID_empresa` ASC) VISIBLE,
  INDEX `fk_User_has_Empresa_User_idx` (`User_ID` ASC) VISIBLE,
  CONSTRAINT `fk_User_has_Empresa_User`
    FOREIGN KEY (`User_ID`)
    REFERENCES `DB_FISPQ`.`User` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Empresa_Empresa1`
    FOREIGN KEY (`Empresa_ID_empresa`)
    REFERENCES `DB_FISPQ`.`Empresa` (`ID_empresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

use DB_FISPQ;

INSERT INTO Empresa (
ID_empresa,  nome, endereco, telefone, Telefone_emergencia, email) VALUES
('1', 'Quimlab Produtos de Química Fina Ltda','Rodovia Geraldo Scavone 2300', '12 39554646', '12 39585627','atendimento@quimlab.com.br');

INSERT INTO User (
ID, name, email, celular, password) VALUES
('1', 'Marcos Ferreira de Noronha', 'marcoshefa@gmail.com.br', '988154973', 'marcos');

INSERT INTO User (
ID, name, email, celular, password) VALUES
('2', 'Beto', 'beto@gmail.com.br', '988154973', 'unicornio');

INSERT INTO Empresa (
ID_empresa,  nome, endereco, telefone, Telefone_emergencia, email) VALUES
('2', 'Laboratórios Quimicos e metrologicos Quimlab','Rodovia Geraldo Scavone 2300', '12 39554646', '12 39585627','atendimento@quimlab.com.br');

INSERT INTO User_has_Empresa(
User_ID,  Empresa_ID_empresa) VALUES
('1', '1');
INSERT INTO User_has_Empresa(
User_ID,  Empresa_ID_empresa) VALUES
('1', '2');
INSERT INTO User_has_Empresa(
User_ID,  Empresa_ID_empresa) VALUES
('2', '1');
INSERT INTO User_has_Empresa(
User_ID,  Empresa_ID_empresa) VALUES
('2', '2');

Select * from User_has_Empresa;


Select * from Empresa;
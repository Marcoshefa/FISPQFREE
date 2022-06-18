CREATE SCHEMA IF NOT EXISTS `DB_FISPQ`;

CREATE TABLE IF NOT EXISTS `DB_FISPQ`.`User` (
  `ID` INT NOT NULL AUTO_INCREMENT,
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
  `ID_empresa` INT NOT NULL AUTO_INCREMENT,
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

INSERT INTO `DB_FISPQ`.`User` (
`name`, `email`, `celular`, `PASSWORD`, `permission_id`) VALUES
('admin', 'admin@gmail.com', '12988974', 'Admin','1');
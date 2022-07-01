CREATE DATABASE  IF NOT EXISTS `DB_FISPQ`;
USE `DB_FISPQ`;

DROP TABLE IF EXISTS `Empresa`;

CREATE TABLE `Empresa` (
  `ID_empresa` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `endereco` varchar(500) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `telefone_emergencia` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `cnpj` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `User`;

CREATE TABLE `User` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `celular` varchar(20) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `update_at` timestamp NULL DEFAULT NULL,
  `permission_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `User_has_Empresa`;

CREATE TABLE `User_has_Empresa` (
  `User_ID` int NOT NULL,
  `Empresa_ID_empresa` int NOT NULL,
  PRIMARY KEY (`User_ID`,`Empresa_ID_empresa`),
  KEY `fk_User_has_Empresa_Empresa1_idx` (`Empresa_ID_empresa`),
  KEY `fk_User_has_Empresa_User_idx` (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

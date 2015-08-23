SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema shop_front
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dhop_front
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shop_front` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `shop_front` ;

-- -----------------------------------------------------
-- Table `shop_front`.`user_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop_front`.`user_tbl` (
  `iduser` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `firstName` VARCHAR(20) NULL COMMENT '',
  `surName` VARCHAR(20) NULL COMMENT '',
  `email` VARCHAR(50) NULL COMMENT '',
  `paswrd` VARCHAR(100) NULL COMMENT '',
  `usercol` VARCHAR(45) NULL COMMENT '',
  `userLevel` INT(2) NULL COMMENT '',
  PRIMARY KEY (`iduser`)  COMMENT '')
ENGINE = InnoDB;

CREATE UNIQUE INDEX `iduser_UNIQUE` ON `shop_front`.`user_tbl` (`iduser` ASC)  COMMENT '';

CREATE UNIQUE INDEX `email_UNIQUE` ON `shop_front`.`user_tbl` (`email` ASC)  COMMENT '';
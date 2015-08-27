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
  `joinDate` INT NULL COMMENT '',
  PRIMARY KEY (`iduser`)  COMMENT '')
ENGINE = InnoDB;

CREATE UNIQUE INDEX `iduser_UNIQUE` ON `shop_front`.`user_tbl` (`iduser` ASC)  COMMENT '';

CREATE UNIQUE INDEX `email_UNIQUE` ON `shop_front`.`user_tbl` (`email` ASC)  COMMENT '';

-- -----------------------------------------------------
-- Table `shop_front`.`creator_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop_front`.`creator_tbl`(
	`IDceator` INT NOT NULL AUTO_INCREMENT COMMENT '',
    `first_name` VARCHAR(30) NULL COMMENT '',
	`surname` VARCHAR(30) NULL COMMENT '',
    `email` VARCHAR(30) NULL COMMENT '',
    `password` VARCHAR(100) NULL COMMENT '');
-- Left on hold may be not needed
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `shop_front`.`product_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop_front`.`product_tbl` (
	`IDproduct` INT NOT NULL AUTO_INCREMENT COMMENT '',
    `product_title` VARCHAR(30) NULL COMMENT '',
    `product_cost` FLOAT(7,2) NULL COMMENT '',
    `product_status` VARCHAR(10) NULL COMMENT  '',
	`product_description` VARCHAR(2000) NULL COMMENT '',
    `IDcreator` INT NULL COMMENT '',
    `product_entry_date` INT NULL COMMENT '',
    PRIMARY KEY (`IDproduct`) COMMENT '',
    CONSTRAINT `fk_IDcreator` FOREIGN KEY (`IDcreator`) 
    REFERENCES `shop_front`.`user_tbl` (`iduser`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idproduct_UNIQUE` ON `shop_front`.`product_tbl` (`IDproduct` ASC)  COMMENT '';

-- -----------------------------------------------------
-- Table `shop_front`.`product_image_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop_front`.`product_image_tbl` (
	`IDimage` INT NOT NULL AUTO_INCREMENT COMMENT '',
    `IDproduct` INT NULL COMMENT '',
    `file_name` VARCHAR(60) NULL COMMENT '',
    `ALT_text` VARCHAR(500) NULL COMMENT '',
    `is_default` BOOLEAN NULL COMMENT '',
    PRIMARY KEY (`IDimage`) COMMENT '',
    CONSTRAINT `fk_IDproduct` FOREIGN KEY (`IDproduct`)
    REFEReNCES `shop_front`.`product_tbl` (`IDproduct`))
ENGINE = InnoDB;
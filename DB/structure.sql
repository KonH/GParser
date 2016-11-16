USE `gparser`;

DROP TABLE `app_info`;
DROP TABLE `app`;
DROP TABLE `developer`;
DROP TABLE `page`;
DROP TABLE `task`;
DROP TABLE `task_type`;

# Helpers:
CREATE TABLE `task_type` (
  `task_type_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`task_type_id`));

# Temp tables:
CREATE TABLE `task` (
  `task_id` INT NOT NULL AUTO_INCREMENT,
  `type_id` INT NOT NULL,
  `priority` INT NULL,
  `in_work` TINYINT(1) NULL,
  `complete` TINYINT(1) NULL,
  PRIMARY KEY (`task_id`),
  INDEX `task_type_id_idx` (`type_id` ASC),
  CONSTRAINT `task_type_id`
    FOREIGN KEY (`type_id`)
    REFERENCES `task_type` (`task_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


# Data tables:
CREATE TABLE `app` (
  `app_id` INT NOT NULL AUTO_INCREMENT,
  `bundle` VARCHAR(255) NOT NULL UNIQUE,
  `alive` TINYINT(1),
  PRIMARY KEY (`app_id`));

CREATE TABLE `app_info` (
  `app_info_id` INT NOT NULL AUTO_INCREMENT,
  `app_id` INT NOT NULL,
  `bundle` VARCHAR(255) NOT NULL,
  `date` DATETIME NOT NULL,
  `alive` TINYINT(1),
  PRIMARY KEY (`app_info_id`),
  INDEX `app_id_idx` (`app_id` ASC),
  CONSTRAINT `app_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `app` (`app_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
CREATE TABLE `developer` (
  `developer_id` INT NOT NULL AUTO_INCREMENT,
  `dev_page_id` VARCHAR(255) NOT NULL UNIQUE,
  PRIMARY KEY (`developer_id`));
  
CREATE TABLE `page` (
  `page_id` INT NOT NULL AUTO_INCREMENT,
  `page_url` VARCHAR(255) NOT NULL UNIQUE,
  PRIMARY KEY (`page_id`));
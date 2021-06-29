
CREATE DATABASE `test-python-mysql`;


CREATE TABLE `test-python-mysql`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `nickname` VARCHAR(45) NULL,
  `age` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

INSERT INTO `test-python-mysql`.`User` (`id`, `name`, `email`, `nickname`, `age`) VALUES ('1', 'Ludwing Rivera Amador', 'ludwing.ra@gmail.com', 'ludwing.ra', '32');

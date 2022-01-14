
DROP DATABASE IF EXISTS `income`;
CREATE DATABASE `income`;
USE `income`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `userId` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `contact` int NOT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `contact_UNIQUE` (`contact`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `whishlists`;
CREATE TABLE `whishlist` (
  `whishId` varchar(45) NOT NULL,
  `description` varchar(100) NOT NULL,
  `saveTo` float NOT NULL,
  `color` varchar(45) NOT NULL,
  `saveType` varchar(45) NOT NULL,
  `startSaveDate` varchar(45) NOT NULL,
  PRIMARY KEY (`whishId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

DROP TABLE IF EXISTS `whishlistDetails`;
CREATE TABLE `whishlistdetail` (
  `whishDetailId` int NOT NULL AUTO_INCREMENT,
  `whishId` varchar(45) NOT NULL,
  `userId` varchar(45) NOT NULL,
  `savedAmount` int NOT NULL,
  `savedDate` varchar(200) NOT NULL,
  PRIMARY KEY (`whishDetailId`),
  KEY `whishId` (`whishId`),
  KEY `userId` (`userId`),
  CONSTRAINT `whishlistdetail_ibfk_1` FOREIGN KEY (`whishId`) REFERENCES `whishlist` (`whishId`),
  CONSTRAINT `whishlistdetail_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1

-- CREATE TABLE `users` (
--   `userId` varchar(45) NOT NULL ,
--   `username` varchar(45) NOT NULL,
--   `contact` int(11) NOT NULL,
--   PRIMARY KEY (`userId`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- DROP TABLE IF EXISTS `whishlists`;
-- CREATE TABLE `whishlist` (
--   `whishId` varchar(45) NOT NULL ,
--   `description` varchar(100) NOT NULL,
--   `saveTo` float(11) NOT NULL,
--   PRIMARY KEY (`whishId`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `whishlistDetails`;
CREATE TABLE `whishlistDetail` (
  `whishDetailId` int(11) NOT NULL AUTO_INCREMENT,
  `whishId` varchar(45) NOT NULL,
  `userId` varchar(45) NOT NULL,
  `savedAmount` int(11) NOT NULL,
  `savedDate` varchar(200) NOT NULL,
  PRIMARY KEY (`whishDetailId`),
  FOREIGN KEY (`whishId`) REFERENCES `whishlist`(`whishId`),
  FOREIGN KEY (`userId`) REFERENCES `users`(`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `expands`;
CREATE TABLE `expands` (
  `expId` int(11) NOT NULL AUTO_INCREMENT,
  `userId` varchar(45) NOT NULL,
  `category` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  `paidAmount` int(11) NOT NULL,
  `paidDate` varchar(200) NOT NULL,
  `contact` int(11) NOT NULL,
  PRIMARY KEY (`expId`),
  FOREIGN KEY (`userId`) REFERENCES `expands`(`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `expandDetails`;
CREATE TABLE `expandDetail` (
  `expId` int(11) NOT NULL AUTO_INCREMENT,
  `needToPay` varchar(45) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`expId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



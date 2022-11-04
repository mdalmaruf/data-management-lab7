-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nba
-- ------------------------------------------------------
-- Server version	5.7.28-log

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;

CREATE TABLE `players` (
  `index` bigint(20) DEFAULT NULL,
  `firstName` text,
  `lastName` text,
  `playerId` bigint(20) DEFAULT NULL,
  `teamId` bigint(20) DEFAULT NULL,
  KEY `ix_players_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dump completed on 2020-11-17 12:56:13

-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: cais
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `caisam_address`
--

DROP TABLE IF EXISTS `caisam_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address` varchar(60) DEFAULT NULL,
  `city_id` bigint DEFAULT NULL,
  `country_id` bigint DEFAULT NULL,
  `state_id` bigint DEFAULT NULL,
  `street_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `caisam_address_city_id_0dc70fec_fk_caisam_city_id` (`city_id`),
  KEY `caisam_address_country_id_67acf509_fk_caisam_country_id` (`country_id`),
  KEY `caisam_address_state_id_d93c3101_fk_caisam_state_id` (`state_id`),
  KEY `caisam_address_street_id_4adcd9cd_fk_caisam_street_id` (`street_id`),
  CONSTRAINT `caisam_address_city_id_0dc70fec_fk_caisam_city_id` FOREIGN KEY (`city_id`) REFERENCES `caisam_city` (`id`),
  CONSTRAINT `caisam_address_country_id_67acf509_fk_caisam_country_id` FOREIGN KEY (`country_id`) REFERENCES `caisam_country` (`id`),
  CONSTRAINT `caisam_address_state_id_d93c3101_fk_caisam_state_id` FOREIGN KEY (`state_id`) REFERENCES `caisam_state` (`id`),
  CONSTRAINT `caisam_address_street_id_4adcd9cd_fk_caisam_street_id` FOREIGN KEY (`street_id`) REFERENCES `caisam_street` (`id`),
  CONSTRAINT `caisam_address_user_id_74ad9d31_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_address`
--

LOCK TABLES `caisam_address` WRITE;
/*!40000 ALTER TABLE `caisam_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `caisam_address` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:55

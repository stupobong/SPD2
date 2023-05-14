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
-- Table structure for table `caisam_subject`
--

DROP TABLE IF EXISTS `caisam_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_subject` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `grade_level` varchar(100) DEFAULT NULL,
  `class_subject` varchar(300) DEFAULT NULL,
  `date_added` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_subject`
--

LOCK TABLES `caisam_subject` WRITE;
/*!40000 ALTER TABLE `caisam_subject` DISABLE KEYS */;
INSERT INTO `caisam_subject` VALUES (1,'Grade 12A','A,D,G,I,J,L,R,W,Z,AB,AC,AD,AK','2023-05-13'),(2,'Grade 12B','A,D,G,I,J,L,R,W,Z,AB,AC,AD,AK','2023-05-13'),(3,'Grade 11A','A,E,G,J,L,Q,V,Y,Z,AB,AC,AE,AF,AK','2023-05-13'),(4,'Grade 11B','A,E,G,J,L,Q,V,Y,Z,AB,AC,AE,AF,AK','2023-05-13'),(5,'Grade 10A','A,F,H,J,K,L,P,V,AA,AB,AC,AD,AJ','2023-05-13'),(6,'Grade 10B','A,F,H,J,K,L,P,V,AA,AB,AC,AD,AJ','2023-05-13'),(7,'Grade 9A','A,J,L,N,O,U,AA,AB,AC,AD,AI','2023-05-13'),(8,'Grade 9B','A,J,L,N,O,U,AA,AB,AC,AD,AI','2023-05-13'),(9,'Grade 8A','A,F,H,J,M,T,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(10,'Grade 8B','A,F,H,J,M,T,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(11,'Grade 7A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(12,'Grade 7B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(13,'Grade 6A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(14,'Grade 6B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(15,'Grade 5A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(16,'Grade 5B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(17,'Grade 4A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(18,'Grade 4B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(19,'Grade 3A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(20,'Grade 3B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(21,'Grade 2A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(22,'Grade 2B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(23,'Grade 1A','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(24,'Grade 1B','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(25,'Grade KA','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13'),(26,'Grade KB','A,F,H,J,L,M,S,X,AA,AB,AC,AD,AG,AH','2023-05-13');
/*!40000 ALTER TABLE `caisam_subject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:32:04

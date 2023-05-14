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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$4RMyx0FLLS7E4i0yu6u9ZN$KCL4P/+hoFTPjSfOE2IVdjFVDlGi4PPZ+m0laBrkhsQ=','2023-05-14 02:55:36.815161',1,'admin','Dean','Edwards','admin@caisedu.com',1,1,'2023-05-13 17:15:25.000000'),(2,'pbkdf2_sha256$600000$9QYRmyzy0HzOoOsJYPI6Gu$3AtOfnZrNQpKMvMiWdm9TiuJSt2SFZDDzZMzndTc1us=','2023-05-13 18:05:03.000000',0,'T21301','Chandina','Nang','NangChandina@gmail.com',0,1,'2023-05-13 18:01:29.000000'),(3,'pbkdf2_sha256$600000$x02vDVP9nB9wqXjZIfHAh0$o6Gi7I3rrAFlJvobiG1hqKfV84vHXkPVlZOeciFkGgs=','2023-05-13 18:05:37.000000',0,'T21302','Chomnea','Neoum','NeoumChomnea@gmail.com',0,1,'2023-05-13 18:05:16.000000'),(4,'pbkdf2_sha256$600000$kkYqX370ky8p5k05do6dIM$vWbA4BaWuKscV3BUxLcjf9ZTAGu1Bq9szqIvcavNYKA=','2023-05-13 18:06:13.000000',0,'T21303','Rachana','Vannak','',0,1,'2023-05-13 18:05:54.000000'),(5,'pbkdf2_sha256$600000$0BYHYOCDwBnFvsm1ly0zQV$4s+y9Jd7l3KYnLNbIWlYg0jwcSJOE5JSqWKI6TgUYzg=','2023-05-13 18:06:57.000000',0,'T21304','Vanny','Leng','LengVanny@gmail.com',0,1,'2023-05-13 18:06:39.000000'),(6,'pbkdf2_sha256$600000$JCUiElBRVinukF3gMWno4M$KHo7P64LJkTR+rmGwoSpQdWRpX91Iv/4Ez3iZtUjceo=','2023-05-13 18:07:33.000000',0,'T21305','Vannak','Leng','LengVannak@gmail.com',0,1,'2023-05-13 18:07:19.000000'),(7,'pbkdf2_sha256$600000$zy7RAi2iMAUhDjL7NlEpjQ$PzDrLgbUHsIevCQSjIIo3N8drjGpLhPg4Jgj+HskVVs=','2023-05-13 18:08:14.000000',0,'T21306','Theary','Dos','DosTheary@gmail.com',0,1,'2023-05-13 18:07:52.000000'),(8,'pbkdf2_sha256$600000$HVlHxFVb95Y0ZXJy2hmikB$ZjAZzm7762zDrJGz0i3JVpLNvxlvtoLZbah6UAEoDF0=','2023-05-13 18:08:44.000000',0,'T21307','Sophea','Se','SeSophea@gmail.com',0,1,'2023-05-13 18:08:27.000000'),(9,'pbkdf2_sha256$600000$wZdZEfD545M9wI8Dy13ZSC$7oRF7lAh1UTsCML9x7JQXoX3OuPWD+UgNQbfitrQLH0=','2023-05-13 18:09:31.000000',0,'T21308','July','Thach','thachjuly@caisedu.com',0,1,'2023-05-13 18:09:16.000000'),(10,'pbkdf2_sha256$600000$7cjZUmU3duTsIbv3zzCxYB$W5Vq9OFv79eIc8J8KNZwGH8ODMJGFKfGiFkA7ue4ELA=','2023-05-13 18:11:22.000000',0,'T21309','Danet','Ka','KaDanet@gmail.com',0,1,'2023-05-13 18:10:02.000000'),(11,'pbkdf2_sha256$600000$SnTD9IuWOfEYXqTz7ow6o7$kVlkRHXmrOr8Mx7sHLKiG8MVxDmFiO8PL36J/cnEGC0=','2023-05-13 18:13:16.000000',0,'T21310','Nida','Ka','KaNida@gmail.com',0,1,'2023-05-13 18:11:37.000000'),(12,'pbkdf2_sha256$600000$aSahbhRBGd06iQz4kKvCxf$9lYZR/rkM40NT84QNuSvGpFtiiU1iAbjSJRcIJUT7XM=','2023-05-13 18:13:49.000000',0,'T21311','Sadam','Ka','KaSadam@gmail.com',0,1,'2023-05-13 18:13:35.000000'),(13,'pbkdf2_sha256$600000$Y5q8FmFK7RRiwL1tcRgiZc$wJTCMijmtml1oS9QdrT0EjghtIBLpLglzdJSU9qbvTM=','2023-05-13 18:14:16.000000',0,'T21312','Piseth','Keurm','KeurmPiseth@gmail.com',0,1,'2023-05-13 18:14:03.000000'),(14,'pbkdf2_sha256$600000$aHIyNcawM0aB2HcjGmOeMa$aUXeI1O6kKR3S2a+0zgo0yFOrpg2zx0Vg30IUq2yjXI=','2023-05-13 18:14:46.000000',0,'T21313','Sonisa','Lin','LinSonisa@gmail.com',0,1,'2023-05-13 18:14:30.000000'),(15,'pbkdf2_sha256$600000$Zm2pJvXU3lh3MKNxyGwxZo$Zd2EbN7MBOW59FJAX0JsizBZt2h9MCH/CgsP2ZBKJwk=','2023-05-13 18:15:20.000000',0,'T21314','Sophat','Thach','ThachSophat@gmail.com',0,1,'2023-05-13 18:14:59.000000'),(16,'pbkdf2_sha256$600000$eonWkfekBIvyaTu7RFGF3T$LUTe8SpKPO2XFuheyFPkHavLfhzh3W/bhx9cfEkM+/o=','2023-05-13 18:15:48.000000',0,'T21315','Seiha','Chan','ChanSeiha@gmail.com',0,1,'2023-05-13 18:15:34.000000'),(17,'pbkdf2_sha256$600000$CLe3NfxrrLIHSkuJSVNESl$kKnyyEhKN9Af04vAJ/0szAgz8XSoLnMd14m2518Zc3M=','2023-05-13 18:16:12.000000',0,'T21316','Sopheaktra','Sieng','SiengSopheaktra@gmail.com',0,1,'2023-05-13 18:15:59.000000'),(18,'pbkdf2_sha256$600000$swlRr9nGzsGS0FQsptQuee$yM4zE/Fy0VyRsoYcjvn/0zRFskUS+82s00hEdfBuCEU=','2023-05-13 18:16:38.000000',0,'T21317','Savouen','Chhun','ChhunSavouen@gmail.com',0,1,'2023-05-13 18:16:24.000000'),(19,'pbkdf2_sha256$600000$9DfOpsqYfa6UxSfVzIOazj$Fz4e3XrQ1pYYB1OamS8NS1+yrYvVPD6IP1e9wd90LSo=','2023-05-13 18:17:06.000000',0,'T21318','Sodalin','Sorn','SornSodalin@gmail.com',0,1,'2023-05-13 18:16:50.000000'),(20,'pbkdf2_sha256$600000$qa9c0SLzShqkP5ECOKbbK0$mHmxky0ksNDgVFB8FRbLTGQdgVD3e0kN+i39YsRDROA=','2023-05-13 18:17:40.000000',0,'T21319','Sophia','Phan','PhanSophia@gmail.com',0,1,'2023-05-13 18:17:27.000000'),(21,'pbkdf2_sha256$600000$ZpSIFk449uttKVoeHHxzh2$tM/UdOJB4juUA3mnOg3Y9TkziuYXrFLVsIiaMw/4CqI=','2023-05-13 18:18:12.000000',0,'T21320','Chhaiya','Sou','SouChhaiya@gmail.com',0,1,'2023-05-13 18:17:55.000000'),(22,'pbkdf2_sha256$600000$v3aZHBtSFFHDzwpRDFDxmg$eg/W0c9lNv4PhwlFMkRnch9aBuovq3apK0hl+iugU3w=','2023-05-13 18:18:42.000000',0,'T21321','Silim','Sip','SipSilim@gmail.com',0,1,'2023-05-13 18:18:26.000000'),(23,'pbkdf2_sha256$600000$zrgnf92M4IHj1igJs8VIze$ZnTrq+tDxNzn+xqg1LZAhFfnvFCJLGkH1TUKh27nC5s=','2023-05-14 02:38:52.396576',0,'202103001','Malyta','Bin','BinMalyta@gmail.com',0,1,'2023-05-13 18:37:50.000000'),(24,'pbkdf2_sha256$600000$aSzbk1P3p5N3303JO6gRaG$NZtVWgi/iVcVFXlPHq6cxlnju37PNwVsoAillrJi8FM=','2023-05-13 18:38:39.000000',0,'202103002','Sovan Mony','Reth','RethSovanMony@gmail.com',0,1,'2023-05-13 18:38:40.000000'),(25,'pbkdf2_sha256$600000$3oYebk6YdiM9klZCh8SNtz$qCHECi0XWpGPvJdO+4KVznQZ1DUnsgWZruFOUq8vJ8U=','2023-05-13 18:39:19.000000',0,'202103003','Sotharoth','Eang','EangSotharoth@gmail.com',0,1,'2023-05-13 18:39:04.000000'),(26,'pbkdf2_sha256$600000$6GAK17kQKIPGhLHDzxh4QU$adkg0BhjJadEUvP1rud0znqoy+LP8j0DuL2cXJvNEOI=','2023-05-14 02:38:22.293903',0,'202103004','Rusaly','Leng','LengRusaly@gmail.com',0,1,'2023-05-13 18:39:32.000000'),(27,'pbkdf2_sha256$600000$AWW39e3AfOoFNQiWxT5975$9DaihSaOzKsDUHGzL12XO+MYsiXQZrXnEkYRAgc2ht0=','2023-05-13 18:40:13.000000',0,'202103005','Zamana','Piphoup','PiphoupZamana@gmail.com',0,1,'2023-05-13 18:40:00.000000'),(28,'pbkdf2_sha256$600000$y664XM7RiHhVJsV7Dd6k3K$tpnC4z7X9CjujBmi8TumrAJRnl061eplICXkHFMPbI4=','2023-05-13 18:40:39.000000',0,'202103006','Lymeng','Chey','CheyLymeng@gmail.com',0,1,'2023-05-13 18:40:24.000000'),(29,'pbkdf2_sha256$600000$eHisSPX4L1AScIbo02RaFC$H3uzwhxNUkEYRBkQGvpfQodPcacMMnxgT+5hhUNNyQc=','2023-05-13 18:41:04.000000',0,'202103007','Angdaniyel','Hou','HouAngdaniyel@gmail.com',0,1,'2023-05-13 18:40:50.000000'),(30,'pbkdf2_sha256$600000$ka8tkJiAuOgsCzviDHS4pH$qcIg9qCTXDI51hcakHl1e4VymZCTWE5NS2u7onaBI8U=','2023-05-13 18:41:27.000000',0,'202103008','Mara','Yin','YinMara@gmail.com',0,1,'2023-05-13 18:41:14.000000'),(31,'pbkdf2_sha256$600000$O8Fq4fERNnadm6uKOZJaEb$0tyYtJHLrGfTpgLnOAnqqbYe60JRHvlPNvMZLSJDA8g=','2023-05-13 18:41:54.000000',0,'202103009','Sothearoth','Hean','HeanSothearoth@gmail.com',0,1,'2023-05-13 18:41:38.000000'),(32,'pbkdf2_sha256$600000$ib2Sb1IzmE6I44lVSiFZPB$3WMj5vog3dAyBZbV+mFxuZfRiVhFKHk1ijmR9vhhGrs=','2023-05-13 18:42:20.000000',0,'202103010','Puthipul','Rith','RithPuthipul@gmail.com',0,1,'2023-05-13 18:42:07.000000'),(33,'pbkdf2_sha256$600000$NCtbVxXOwJRI3qmgW7STzO$YF4OpxS8J4nTtqi7AEsshs8g81MWMgX/vfGG0Q8F1/I=','2023-05-13 18:43:43.000000',0,'202102001','Pisalsak','Channa','ChannaPisalsak@gmail.com',0,1,'2023-05-13 18:43:29.000000'),(34,'pbkdf2_sha256$600000$KVWlKybo4Xemj4B9FeOn3H$AYp4+85uhU16ByNc1AVp5kkJLXq3G+vU1cOuRjFxEjg=','2023-05-13 18:44:08.000000',0,'202102002','Naching','Ngan','NganNaching@gmail.com',0,1,'2023-05-13 18:43:54.000000'),(35,'pbkdf2_sha256$600000$tfRimDVv5Ym8sNKARQCAiP$gjSD0Ei5AK3semD+M7cX1AQ1ksVHHzOcIA38XtxhHf4=','2023-05-13 18:44:35.000000',0,'202102003','Souneang','Yin','YinSouneang@gmail.com',0,1,'2023-05-13 18:44:20.000000'),(36,'pbkdf2_sha256$600000$zKLGyh1DK47GgxxDlH0KVT$6dxaLJjNG0HgJ62uRaSahJWhhf/7qmlmUatlQlnFRmk=','2023-05-13 18:45:05.000000',0,'202102004','Vijanineath','Vathana','VathanaVijanineath@gmail.com',0,1,'2023-05-13 18:44:48.000000'),(37,'pbkdf2_sha256$600000$c4KW4flwYW1mEyGUaYBjkC$quNhAaUUEZkhXsme5yrH1MrzLn01dAnvo3yotC6ez+I=','2023-05-13 18:45:33.000000',0,'202102005','Kevy','Beng','BengKevy@gmail.com',0,1,'2023-05-13 18:45:19.000000'),(38,'pbkdf2_sha256$600000$21mgtkRpTQMqThn1sNhxay$lk08T6RI47GhXBV6blidqNtm5fqyuKZVH1W58m9Pexg=','2023-05-13 18:46:04.000000',0,'202101001','Sodanita','Heng','HengSodanita@gmail.com',0,1,'2023-05-13 18:45:49.000000'),(39,'pbkdf2_sha256$600000$DEtsFeM9qvlVeUh06qqt4V$00BPEFxydWmROealXw2sUPFe/8/zl/t4LoALmTQv/1g=','2023-05-13 18:47:10.000000',0,'202101002','Puthivong','Pon','PonPuthivong@gmail.com',0,1,'2023-05-13 18:46:51.000000'),(40,'pbkdf2_sha256$600000$CBgspE47YF26ZtreZ9dQYO$Q8QPbTGPy2gjUFBJW+aJheT8GwJuUz9T52tGfJJ5drY=','2023-05-13 18:47:37.000000',0,'202101003','Sovanrathanak','Siv','SivSovanrathanak@gmail.com',0,1,'2023-05-13 18:47:22.000000'),(41,'pbkdf2_sha256$600000$RcYDFGYqWVTQlIzqPjm2bg$MIG2C975LePOC/Q7vErk1srAFEqEVvxzzYEZjFnRFD8=','2023-05-13 18:48:29.000000',0,'202101004','Phalla Aridem','Yin','YinPhallaAridem@gmail.com',0,1,'2023-05-13 18:48:09.000000'),(42,'pbkdf2_sha256$600000$ZhBS6gH3R4H2M0ArNpIop2$hJUWmNvP3OV/d59MZ2gkc2Cwa94cEZf2FZQLxJIWKr0=','2023-05-13 18:49:06.000000',0,'202101005','Lisoreachiny','Phaung','PhaungLisoreachiny@gmail.com',0,1,'2023-05-13 18:48:50.000000'),(43,'pbkdf2_sha256$600000$3hwLAGgkMwgrc2vAhw5DlN$38jwgOHqFwav/272kjGL8Kk1FyWnp0naotJ6uqGglYU=','2023-05-14 02:52:54.025684',0,'registrar','Bopha','Chin','chinbopha@caisedu.com',0,1,'2023-05-13 18:53:42.000000'),(44,'pbkdf2_sha256$600000$qyrNrmIVITKk16ZngzyIUq$iFcrr12N6O3gQFUvs45791AoGRLcwSprTNoSxIR34Ig=','2023-05-14 02:52:15.981170',0,'julong','Julong','Thach','julongthach@caisedu.com',0,1,'2023-05-14 02:50:19.982007'),(45,'pbkdf2_sha256$600000$sRtBtzVJitW7z1seqJIUD3$zArwyVZGyTn3uH8F33Cys7zblzQgBtfFJeQRTs1vJnk=','2023-05-14 03:20:21.255981',1,'sela','','','sela@caisedu.com',1,1,'2023-05-14 03:19:52.182036');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:39

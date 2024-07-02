-- MariaDB dump 10.19  Distrib 10.4.22-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: manjar
-- ------------------------------------------------------
-- Server version	10.4.22-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_desc` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Bebidas'),(2,'Alimentos');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(60) NOT NULL,
  `product_desc` varchar(155) NOT NULL,
  `product_image_path` varchar(255) DEFAULT NULL,
  `product_price` decimal(10,2) DEFAULT NULL,
  `product_cat_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `fk_cat_id` (`product_cat_id`),
  CONSTRAINT `fk_cat_id` FOREIGN KEY (`product_cat_id`) REFERENCES `category` (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Coca-Cola','Refresco carbonatado','../static/img/coca-cola.jpg',2.50,1),(2,'Sprite','Gaseosa de lim├│n y lima','../static/img/sprite.jpg',2.50,1),(3,'Jugo de Naranja','Jugo de naranja 100% puro','../static/img/citric.jpg',3.00,1),(4,'Caf├®','Caf├® caliente reci├®n hecho','../static/img/cafe.jpg',2.00,1),(5,'T├®','T├® caliente reci├®n hecho','../static/img/te.png',2.00,1),(6,'Hamburguesa','Hamburguesa de carne con lechuga, tomate y cebolla','../static/img/burguer.jpg',5.99,2),(7,'Pizza','Salsa de tomate, queso y toppings sobre una base de masa','../static/img/pizza.jpg',7.99,2),(8,'Ensalada','Mezcla de verduras, hortalizas y aderezo','../static/img/ensalada.jpg',4.99,2),(9,'Pasta','Pasta cocida con salsa y toppings','../static/img/pasta.jpg',6.99,2),(10,'Frutas','Surtido de frutas frescas','../static/img/fruta.jpg',3.99,2),(11,'Milanesa con fritas','milanesa de ternera con fritas','../img/img.jpg',5.00,2),(17,'Fanta','Bebida carbonatada','../static/img/fanta.jpg',3.50,1),(19,'Fanta Light','Fanta sin az├║car','../static/img/fanta.jpg',3.85,1);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `USER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_NAME` varchar(60) NOT NULL,
  `USER_MAIL` varchar(255) NOT NULL,
  `USER_PASSWORD` varchar(60) NOT NULL,
  PRIMARY KEY (`USER_ID`),
  UNIQUE KEY `USER_NAME` (`USER_NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'gustavo','gustaboin@gmail.com','123456'),(2,'Eleonora','eleonora@gmail.com','789654');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-30 22:05:42

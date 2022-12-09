drop database plat_streaming;

CREATE DATABASE plat_streaming;

use plat_streaming;


-- MAESTROS DE LOS ARCHIVOS CARGADOS

DROP TABLE IF EXISTS plataformas;

CREATE TABLE plataformas (
	idStream varchar(30) NOT NULL,
	category varchar(50) NOT NULL,
	title varchar(120) NOT NULL,
	release_year INTEGER(20) NOT NULL,
    duration_len INTEGER(10) NOT NULL,
    duration_type varchar(20) NOT NULL,
    platform  varchar(20) NOT NULL
    
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
 DROP TABLE IF EXISTS `genero`;

CREATE TABLE genero (
  idStream varchar(30) ,
  genre varchar(80) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
 
 DROP TABLE IF EXISTS `actores`;
CREATE TABLE actores (
  idStream varchar(30),
  cast varchar(120) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 10-07-2020 a las 19:46:55
-- Versión del servidor: 5.7.30
-- Versión de PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `wally`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clubs`
--
DROP TABLE IF EXISTS `clubs`;

CREATE TABLE `clubs` (
  `id` int(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `ciudad` varchar(600) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clubs`
--

INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('Estudiantes de La Plata', 'La Plata', 1);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('Boca Juniors', 'Buenos Aires', 2);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('River Plate', 'Buenos Aires', 3);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('Racing Club', 'Avellaneda', 4);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('Independiente', 'Avellaneda', 5);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('San Lorenzo', 'Flores', 6);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('Vélez Sarsfield', 'Liniers', 7);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('Newells Old Boys ', 'Rosario', 8);
INSERT INTO `clubs` (`nombre`, `ciudad`, `id`) VALUES
('flag', '1', 37);
-- --------------------------------------------------------
--
-- Indices de la tabla `clubs`
--
ALTER TABLE `clubs`
  ADD UNIQUE KEY `id` (`id`);



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

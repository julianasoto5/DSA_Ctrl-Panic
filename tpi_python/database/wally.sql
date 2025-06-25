- phpMyAdmin SQL Dump
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
-- Estructura de tabla para la tabla `accounts`
--

CREATE TABLE `accounts` (
  `username` varchar(100) NOT NULL,
  `password` varchar(600) NOT NULL,
  `club` varchar(100) NOT NULL,
  `id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `accounts`
--

INSERT INTO `accounts` (`username`, `password`, `id`) VALUES
('admin', '111fca2d52def4c33f4d8f1be7e74d14b65d365e5ddb91610c3c0dbecc192073b0b0df28213e3828cc0321f6286baf94449a4f8803203be3293595f4d67ff7e2', estudiantes, 1);

-- --------------------------------------------------------
--
-- Indices de la tabla `accounts`
--
ALTER TABLE `accounts`
  ADD UNIQUE KEY `id` (`id`);



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

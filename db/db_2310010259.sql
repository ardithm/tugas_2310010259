-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 10, 2025 at 11:54 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_2310010259`
--

-- --------------------------------------------------------

--
-- Table structure for table `lahan`
--

CREATE TABLE `lahan` (
  `id_lahan` int NOT NULL,
  `id_petani` int NOT NULL,
  `lokasi` varchar(100) DEFAULT NULL,
  `luas_lahan` double DEFAULT NULL,
  `jenis_tanah` varchar(50) DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lahan`
--

INSERT INTO `lahan` (`id_lahan`, `id_petani`, `lokasi`, `luas_lahan`, `jenis_tanah`, `keterangan`) VALUES
(202, 102, 'Blok B3', 99, 'Gembur', 'Lahan subur cocok sayuran'),
(203, 103, 'Blok C2', 99, 'Berpasir', 'Cocok untuk palawija'),
(204, 101, 'Blok A1', 20, 'Lempung', 'Bagus');

-- --------------------------------------------------------

--
-- Table structure for table `panen`
--

CREATE TABLE `panen` (
  `id_panen` int NOT NULL,
  `id_petani` int NOT NULL,
  `id_tanaman` int NOT NULL,
  `tanggal_panen` date DEFAULT NULL,
  `jumlah_hasil` double DEFAULT NULL,
  `kualitas` varchar(20) DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `panen`
--

INSERT INTO `panen` (`id_panen`, `id_petani`, `id_tanaman`, `tanggal_panen`, `jumlah_hasil`, `kualitas`, `keterangan`) VALUES
(501, 101, 301, '2025-05-25', 1800, 'Bagus', 'Panen sesuai rencana'),
(502, 102, 302, '2025-06-10', 250, 'Sedang', 'Beberapa terkena hama');

-- --------------------------------------------------------

--
-- Table structure for table `pemupukan`
--

CREATE TABLE `pemupukan` (
  `id_pemupukan` int NOT NULL,
  `id_petani` int NOT NULL,
  `id_tanaman` int NOT NULL,
  `jenis_pupuk` varchar(50) DEFAULT NULL,
  `tanggal_pupuk` date DEFAULT NULL,
  `jumlah_kg` double DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pemupukan`
--

INSERT INTO `pemupukan` (`id_pemupukan`, `id_petani`, `id_tanaman`, `jenis_pupuk`, `tanggal_pupuk`, `jumlah_kg`, `keterangan`) VALUES
(401, 101, 301, 'Urea', '2025-02-10', 25, 'Pemupukan awal tanam'),
(402, 101, 301, 'NPK', '2025-03-15', 20, 'Pemupukan susulan'),
(403, 102, 302, 'Organik', '2025-04-01', 15.5, 'Pupuk kompos alami');

-- --------------------------------------------------------

--
-- Table structure for table `petani`
--

CREATE TABLE `petani` (
  `id_petani` int NOT NULL,
  `nama_petani` varchar(100) NOT NULL,
  `alamat` text,
  `no_hp` varchar(15) DEFAULT NULL,
  `jenis_kelamin` varchar(10) DEFAULT NULL,
  `umur` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `petani`
--

INSERT INTO `petani` (`id_petani`, `nama_petani`, `alamat`, `no_hp`, `jenis_kelamin`, `umur`) VALUES
(101, 'Budi Santosos', 'Desa Sukamaju, Cianjur', '081234567890', 'Laki-Laki', 42),
(102, 'Siti Aminah', 'Desa Cibeber, Cianjur', '081298765432', 'Perempuan', 37),
(103, 'Rahmat Hidayat', 'Desa Bojong, Cianjur', '082112233445', 'Perempuan', 30);

-- --------------------------------------------------------

--
-- Table structure for table `tanaman`
--

CREATE TABLE `tanaman` (
  `id_tanaman` int NOT NULL,
  `nama_tanaman` varchar(100) NOT NULL,
  `jenis_tanaman` varchar(50) DEFAULT NULL,
  `masa_tanam` int DEFAULT NULL,
  `musim_tanam` varchar(20) DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tanaman`
--

INSERT INTO `tanaman` (`id_tanaman`, `nama_tanaman`, `jenis_tanaman`, `masa_tanam`, `musim_tanam`, `keterangan`) VALUES
(301, 'Padi Ciherang', 'Palawija', 99, 'Hujan', 'Varietas unggul tahan hama'),
(302, 'Cabai Merah', 'Sayuran', 90, 'Kemarau', 'Perawatan intensif diperlukan'),
(303, 'Singkong', 'Palawija', 20, 'Hujan', 'Bagus');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lahan`
--
ALTER TABLE `lahan`
  ADD PRIMARY KEY (`id_lahan`),
  ADD KEY `id_petani` (`id_petani`);

--
-- Indexes for table `panen`
--
ALTER TABLE `panen`
  ADD PRIMARY KEY (`id_panen`),
  ADD KEY `id_petani` (`id_petani`),
  ADD KEY `id_tanaman` (`id_tanaman`);

--
-- Indexes for table `pemupukan`
--
ALTER TABLE `pemupukan`
  ADD PRIMARY KEY (`id_pemupukan`),
  ADD KEY `id_petani` (`id_petani`),
  ADD KEY `id_tanaman` (`id_tanaman`);

--
-- Indexes for table `petani`
--
ALTER TABLE `petani`
  ADD PRIMARY KEY (`id_petani`);

--
-- Indexes for table `tanaman`
--
ALTER TABLE `tanaman`
  ADD PRIMARY KEY (`id_tanaman`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `lahan`
--
ALTER TABLE `lahan`
  ADD CONSTRAINT `lahan_ibfk_1` FOREIGN KEY (`id_petani`) REFERENCES `petani` (`id_petani`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `panen`
--
ALTER TABLE `panen`
  ADD CONSTRAINT `panen_ibfk_1` FOREIGN KEY (`id_petani`) REFERENCES `petani` (`id_petani`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `panen_ibfk_2` FOREIGN KEY (`id_tanaman`) REFERENCES `tanaman` (`id_tanaman`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pemupukan`
--
ALTER TABLE `pemupukan`
  ADD CONSTRAINT `pemupukan_ibfk_1` FOREIGN KEY (`id_petani`) REFERENCES `petani` (`id_petani`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pemupukan_ibfk_2` FOREIGN KEY (`id_tanaman`) REFERENCES `tanaman` (`id_tanaman`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

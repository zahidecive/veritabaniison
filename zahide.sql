-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 01 Oca 2024, 20:08:26
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `zahide`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `eser`
--

CREATE TABLE `eser` (
  `eser_id` int(11) NOT NULL,
  `eser_adi` text DEFAULT NULL,
  `eser_basim` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `eser`
--

INSERT INTO `eser` (`eser_id`, `eser_adi`, `eser_basim`) VALUES
(1, 'Satranc', '2019'),
(2, '1984', '2019'),
(3, 'Simyaci', '2018'),
(4, 'Yabanci', '2018'),
(5, 'Seker Portakali', '2017');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `konu`
--

CREATE TABLE `konu` (
  `konu_id` int(11) NOT NULL,
  `tur` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `konu`
--

INSERT INTO `konu` (`konu_id`, `tur`) VALUES
(1, 'Suç'),
(2, 'Kültürel Çatışma'),
(3, 'Toplumsal Eleştiri'),
(4, 'Totaliterizm'),
(5, 'Romantik Bilim Kurgu');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yayinevi`
--

CREATE TABLE `yayinevi` (
  `yayinevi_id` int(11) NOT NULL,
  `yayinevi_adi` text DEFAULT NULL,
  `yayinevi_adres` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `yayinevi`
--

INSERT INTO `yayinevi` (`yayinevi_id`, `yayinevi_adi`, `yayinevi_adres`) VALUES
(1, 'Iletisim Yayinlari', 'Istanbul'),
(2, 'Can Yayinlari', 'Istanbul'),
(3, 'Pegasus Yayinlari', 'Istanbul'),
(4, 'Yapı Kredi Yayinlari', 'Istanbul'),
(5, 'Cem Yayinevi', 'Izmir');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yazar`
--

CREATE TABLE `yazar` (
  `yazar_id` int(11) NOT NULL,
  `yazar_adi` text DEFAULT NULL,
  `yazar_soyadi` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `yazar`
--

INSERT INTO `yazar` (`yazar_id`, `yazar_adi`, `yazar_soyadi`) VALUES
(1, 'Stefan', 'Zweig'),
(2, 'George', 'Orwell'),
(3, 'Paulo', 'Coelho'),
(4, 'Albert', 'Camus'),
(5, 'Jose Mauro de', 'Vasconceles');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `eser`
--
ALTER TABLE `eser`
  ADD PRIMARY KEY (`eser_id`);

--
-- Tablo için indeksler `konu`
--
ALTER TABLE `konu`
  ADD PRIMARY KEY (`konu_id`);

--
-- Tablo için indeksler `yayinevi`
--
ALTER TABLE `yayinevi`
  ADD PRIMARY KEY (`yayinevi_id`);

--
-- Tablo için indeksler `yazar`
--
ALTER TABLE `yazar`
  ADD PRIMARY KEY (`yazar_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `eser`
--
ALTER TABLE `eser`
  MODIFY `eser_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Tablo için AUTO_INCREMENT değeri `konu`
--
ALTER TABLE `konu`
  MODIFY `konu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Tablo için AUTO_INCREMENT değeri `yayinevi`
--
ALTER TABLE `yayinevi`
  MODIFY `yayinevi_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Tablo için AUTO_INCREMENT değeri `yazar`
--
ALTER TABLE `yazar`
  MODIFY `yazar_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

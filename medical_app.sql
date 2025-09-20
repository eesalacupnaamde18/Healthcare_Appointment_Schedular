-- Create Database
CREATE DATABASE IF NOT EXISTS medical_app;
USE medical_app;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50) NOT NULL
);

-- Appointments Table
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'scheduled',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
);

-- Optional: Insert Sample Data
INSERT INTO users (name, email, password) VALUES
('Anvit', 'anvit@example.com', 'hashedpassword1'),
('Alice', 'alice@example.com', 'hashedpassword2');

INSERT INTO doctors (name, specialty) VALUES
('Dr. Smith', 'Cardiology'),
('Dr. John', 'Neurology');

INSERT INTO appointments (user_id, doctor_id, appointment_time, status) VALUES
(1, 1, '2025-09-25 10:00:00', 'scheduled'),
(2, 2, '2025-09-26 14:30:00', 'scheduled');

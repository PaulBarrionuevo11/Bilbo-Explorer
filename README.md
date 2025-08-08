# Bilbo explorer
Bilbo is an innovative, curious quadcopter designed to explore the aerial spaces of mars, embracing adventure as it learns and grows.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Hardware](#hardware)
  - [Components](#components)
  - [Assembly Instructions](#assembly-instructions)
- [Software](#software)
  - [Firmware](#firmware)
  - [Control Software](#control-software)
- [Usage](#usage)
  - [Flight Modes](#flight-modes)
  - [Safety Guidelines](#safety-guidelines)
- [Development](#development)
  - [Contributing](#contributing)
  - [Debugging and Troubleshooting](#debugging-and-troubleshooting)
- [Community](#community)
  - [Discussion Forums](#discussion-forums)
  - [Contributors](#contributors)
- [Documentation](#documentation)
  - [API Reference](#api-reference)
  - [Tutorials](#tutorials)
- [License](#license)
- [Acknowledgments](#acknowledgments)


# Introduction
Bilbo is a curious tricopter that wants to fly the autonomously and learn from its environment. With the combination of a strong design, computer architecture and the understanding of the laws of physics, this project aspires to be open source and/or divert to any other multirotor project that can fly in adverse condition of low air density and strong wind gusts.

# Project Overview
The Idea is to work with relative out of the shelf components to build the flight controller. Then move it to a testing face and ultimately to a real environment. 
The Goal is to launch a prototype demo to validate: design (mechanic and embedded system), aerodynamics and power systems. 
Documentation will be updated in this file accordingly.

# Getting Started
## Prerequisites
* Access to Internet
* Access to Ethernet (recommended)

## Installation
* Your desired IDE (recommend Visual Studio)
* Arduino IDE or PlatformIO to code and debug the microcontroller
* Jetson Nano Developer Kit SD Card Image: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write
* Using Rpanion: https://www.docs.rpanion.com/software/rpanion-server (page to download the server image. THIS PART IS NOT REQUIRED)
* Download the necessary code from this repo

# Hardware
## Components
The electonic components used in this project are (as of now) the following:
* A microcontroller: ESP32 or Arduino family. 
* The project its been worked on Windows and MAC operating system.
* A microcomputer: NVIDIA Jetson Nano (Possibility of adding changes to be used with Raspberry Pi)
* MPU 6050: IMU
* BMP280: Barometric Pressure & Altitude Sensor
* HC-SR04: Ultrasonic sensor
* Brushless motors (x2)
* ESC (x2)
* Lipo Battery or Power Supply (Recommend lipo battery to use for outdoor flights)

## PID STATION
The PID station will be controlled with the Flight Server (FS) containe in this repo. The intention is to read values from the sensors and start two motors remotely to stabilize the the front part of the vehicle and obtained the values for calibration.

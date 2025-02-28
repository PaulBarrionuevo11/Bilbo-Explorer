# Bilbo explorer
Bilbo is an innovative, curious bi-rotor drone designed to explore the aerial spaces of any planet, embracing adventure as it learns and grows.

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
Bilbo is the aspiration of drones flying the airspace of the planet Earth and maybe one day Mars. With the combination of a strong design, computer architecture and the understanding of the laws of physics, Bilbo tries to motivate an ambitious project that can be share with others.

# Project Overview
The Idea is to work with relative out of the shelf components and the set up a flight controller and adjust PID controllers from a bench. Then move it to a real drone and validate the calibrated parameters. 
The Goal is to launch a prototype deom to validate: design, aerodynamics and power systems. 
Documentation will be updated in this file accordingly.

# Getting Started
## Prerequisites
* Access to Internet
* Access to Ethernet (recommended)

## Installation
* Your desired IDE (recommend Visual Studio)
* Arduino IDE or PlatformIO to code and debug the microcontroller
* Jetson Nano Developer Kit SD Card Image: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write
* Using Rpanion: https://www.docs.rpanion.com/software/rpanion-server (page to download the server image)
* Download the code from this repo

# Hardware
## Components
The electonic components used in this project are (as of now) the following:
* A microcontroller: ESP32 or Arduino family. 
* The project its been worked on Windows and MACOS.
* A microcomputer: NVIDIA Jetson Nano (Possibility of adding changes to be used with Raspberry Pi)
* MPU 6050: IMU
* BMP280: Barometric Pressure & Altitude Sensor
* HC-SR04: Ultrasonic sensor
* Brushless motors (x2)
* ESC (x2)
* Lipo Battery or Power Supply (Recommend lipo battery to use for outdoor flights)

## PID STATION

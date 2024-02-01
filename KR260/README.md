## Required Hardware Components
1. Kria KR260 board
2. Resistors (4.7K and 100 Ohms)
3. Push Button
4. LED
5. Bread board and connecting wires

## Software requirements
1. Ubuntu 22.04 for Kria KR260 board
2. AWS account
Further details and download links are available at /documents/KR260 to AWS Greengrass IoT - GPIO-(Ubuntu/Petalinux).pdf of this repo.

## Quick Start
For setting up hardware and software for KR260 connect to AWS IoT , refer the document available at /documents/KR260 to AWS Greengrass IoT - GPIO-(Ubuntu/Petalinux).pdf of this repo.

## KR260 to AWS IoT Greengrass Architecture

![KR260 to AWS IoT Greengrass Architecture](https://github.com/LogicTronix/kria-cloud-certifications-private/blob/main/KR260/AWS/ubuntu/documents/KR260_AWS_IoT_updated.png)
This diagram shows the software and hardware architecture used in this tutorial. 
Kria KR260 board consists of Programmable Logic (PL) Fabric (FPGA)  hardware overlay for interfacing LED, switch and I2C sensor. 
Further it runs AWS Greengrass Core Device Application which publish and subscribe message topics for actuating LED and monitoring sensors and switches. 
From AWS IoT MQTT Test Client KR260 LED will be controlled through subscribed topic and also publish Switch pressed event to AWS IoT cloud.

Here is the image of KR260 board and hardware used in this tutorial:
![KR260 Board - GPIO](https://github.com/LogicTronix/kria-cloud-certifications-private/blob/main/KR260/AWS/ubuntu/documents/kr260_gpio.jpg)



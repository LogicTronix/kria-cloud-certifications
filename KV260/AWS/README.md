## Required Hardware Components
1. Kria KV260 board
2. Resistors (4.7K and 100 Ohms)
3. Push Button
4. LED
5. Bread board and connecting wires

## Software requirements
1. Ubuntu 22.04 for Kria KV260 board
2. AWS account
Further details and download links are available at /documents/KV260 to AWS Greengrass IoT - GPIO-(Ubuntu/Petalinux).pdf of this repo.

## Quick Start
For setting up hardware and software for KV260 connect to AWS IoT , refer the document available at /documents/KV260 to AWS Greengrass IoT - GPIO-(Ubuntu/Petalinux).pdf of this repo.

## KV260 to AWS IoT Greengrass Architecture

![KV260 to AWS IoT Greengrass Architecture](https://github.com/LogicTronix/kria-cloud-certifications-private/blob/main/KV260/AWS/ubuntu/documents/KV260_AWS_IoT.png)
This diagram shows the software and hardware architecture used in this tutorial. 
Kria KV260 board consists of Programmable Logic (PL) Fabric (FPGA)  hardware overlay for interfacing LED, switch and I2C sensor. 
Further it runs AWS Greengrass Core Device Application which publish and subscribe message topics for actuating LED and monitoring sensors and switches. 
From AWS IoT MQTT Test Client KV260 LED will be controlled through subscribed topic and also publish Switch pressed event to AWS IoT cloud.

Here is the image of KV260 board and hardware used in this tutorial:
![KV260 Board - GPIO](https://github.com/LogicTronix/kria-cloud-certifications-private/blob/main/KV260/AWS/ubuntu/documents/kv260-gpio.jpg)



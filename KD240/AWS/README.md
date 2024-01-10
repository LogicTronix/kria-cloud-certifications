## Required Hardware Components
1. Kria KD240 board
2. Resistors (4.7K and 100 Ohms)
3. Push Button
4. LED
5. Bread board and connecting wires

## Software requirements
1. Ubuntu 22.04 for Kria KD240 board
2. AWS account
Further details and download links are available at /documents/KD240 to AWS Greengrass IoT - GPIO-(Ubuntu/Petalinux).pdf of this repo.

## Quick Start
For setting up hardware and software for KD240 connect to AWS IoT , refer the document available at /documents/KD240 to AWS Greengrass IoT - GPIO-(Ubuntu/Petalinux).pdf of this repo.

## KD240 to AWS IoT Greengrass Architecture

![KD240 to AWS IoT Greengrass Architecture](https://github.com/LogicTronix/kria-cloud-certifications-private/blob/main/KD240/AWS/ubuntu/documents/KD240-aws-iot.png)
This diagram shows the software and hardware architecture used in this tutorial. 
Kria KD240 board consists of Programmable Logic (PL) Fabric (FPGA)  hardware overlay for interfacing LED, switch and I2C sensor. 
Further it runs AWS Greengrass Core Device Application which publish and subscribe message topics for actuating LED and monitoring sensors and switches. 
From AWS IoT MQTT Test Client, LED connected to KD240 will be controlled through subscribed topic. Further, on button press, publish Switch pressed event to AWS IoT cloud .

Here is the image of KD240 board and hardware used in this tutorial:
![KD240 Board - GPIO](https://github.com/LogicTronix/kria-cloud-certifications-private/blob/main/KD240/AWS/ubuntu/documents/kd240-gpio.jpg)



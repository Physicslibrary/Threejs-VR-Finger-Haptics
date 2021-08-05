# Threejs-VR-Finger-Haptics
Explore finger haptics with Raspberry Pi, Threejs, and Oculus Quest.<br>

image

Unlike other projects (eg. Threejs-VR-Sensors, Threejs-VR-Carbon-Dioxide-Sensor) where sensors send data to a web browser, this one sends data from a web browser to an output haptic device. This repository is for experimenters interested in interfacing I2C devices from Raspberry Pi to wifi devices (eg. Oculus Quest).<br>

## Hardware

Pi Zero W (model 3B+ works)<br>

The author uses Pi Zero W because of its small form factor and low power. A small form factor allows it to hide from an Oculus Quest for more reliable hand tracking in WebXR. The deep neural networks in Oculus Quest hand tracking are probably not trained for hands with circuit boards attached.<br>

A low power Pi Zero W uses ~150mA at 5V that it runs >60min on NiMH AA batteries.<br>

https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md

The first image shows, left of Pi, an Adafruit PowerBoost 1000 which is a DC-to-DC converter that converts ~2.4V from two NiMH AA batteries to give a stable 5V for Pi Zero W.<br>

Pimoroni DRV2605L Linear Actuator Haptic Breakout:<br>

The breakout has both TI DRV2605L haptic driver chip and ELV1411A linear resonant actuator built in. Unlike using ULN2803A and square waves to drive LRA motors (eg. Raspberry-Pi-Time-of-Flight-Haptics), the DRV2605L has circuits to vibrate a LRA motor at its natural frequency and the driving force is an analog sinusoidal wave. LRA is like a tuning fork that vibrate in a narrow range of frequency. It is a mass-on-a-spring (or magnet-on-a-spring) driven by a magnetic coil.<br>

This experiment uses one finger so one haptic driver with a fixed I2C address 0x5a is fine.<br>

## Software

Raspberry Pi OS Lite (tested May 7, 2021 release)<br>

https://www.raspberrypi.org/software/operating-systems/

https://github.com/pimoroni/drv2605-python

sudo pip install drv2605

(if pip or i2c-detect not on Pi OS Lite)<br>

sudo apt-get update<br>
sudo apt-get install python-pip<br>
sudo install i2c-tools<br>

## Programming Pimoroni DRV2605L Linear Actuator Haptic Breakout



## References

Pi Zero W:<br>

https://www.raspberrypi.org/

https://www.raspberrypi.org/documentation/usage/gpio/

Pimoroni DRV2605L Linear Actuator Haptic Breakout:<br>

https://shop.pimoroni.com/products/drv2605l-linear-actuator-haptic-breakout

https://github.com/pimoroni/drv2605-python

https://ai.facebook.com/blog/hand-tracking-deep-neural-networks/

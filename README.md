# Threejs-VR-Finger-Haptics
Explore finger haptics with Raspberry Pi, Threejs, and Oculus Quest.<br>

<img src="1.jpg" width="512">

Unlike other projects (eg. Threejs-VR-Sensors, Threejs-VR-Carbon-Dioxide-Sensor) where sensors send data to a web browser, this one sends data from a web browser to an output haptic device. This repository is for experimenters interested in interfacing I2C devices from Raspberry Pi to wifi devices (eg. Oculus Quest).<br>

(The green wires are wire wrap wires. Flexible at 30AWG and useful for rapid prototyping.)<br>

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

In a Terminal, "sudo i2cdetect -y 1" displays the hex addresses of I2C devices connected to the Pi. Properly wired, the Pimoroni DRV2605L breakout appears at hex address 0x5a.<br>

On the side, the author has noticed Melexis MLX90614, in earlier project (https://github.com/Physicslibrary/Threejs-VR-Sensors), has the same address 0x5a. This could be an issue if two devices with the same address are connected to the same bus. The author may investigate what will happen if two 0x5a are connected. However, MLX90614 I2C address can be reconfigured.<br>

## Programming Pimoroni DRV2605L Linear Actuator Haptic Breakout

Pimoroni's python scripts tap-tap-tap.py and test-waveform.py in https://github.com/pimoroni/drv2605-python/tree/master/examples are excellent examples to learn from. The script morse.py is modeled from tap-tap-tap.py.<br>

<img src="2.jpg" width="800">

A terminal running "python morse.py" and its output. Once that is working, morse code dit "0" and dash "1" are converted to vibrations with drv2605.go(), time.sleep(), and drv2605.stop().<br>

The terminal is running in "Raspberry Pi OS with desktop" on a Raspberry Pi 3B+. A full linux desktop is useful because a terminal is used to ssh into Pi Zero W, wget software, and a Chromium web browser to debug javascript codes (ctrl-shift-i). Chromium will output error messages about not able to run WebXR specific codes but will run enough for debugging.<br>

(to finish)<br>

threejs_vr_finger_haptics.html is meant to run on a Raspberry Pi with websocketd and morse.py.<br>

Need to generate two files key.pem and cert.pem because WebXR will only run with https://.<br>

openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem<br>

./websocketd --port=8000 --ssl --sslkey=key.pem --sslcert=cert.pem --staticdir=. python morse.py<br>

threejs_vr_finger_haptics.html in threejs examples directory<br>

in examples directory, "mv index.html index1.html" to allow browser to "see" threejs_vr_finger_haptics.html file<br>

"Enter VR" and poke at "hello world". If a finger is detected near "hello world", javascript ws.send("hello world") to websocketd to stdin in morse.py to convert to haptic morse code.<br>


## References

Pi Zero W:<br>

https://www.raspberrypi.org/

https://www.raspberrypi.org/documentation/usage/gpio/

https://github.com/joewalnes/websocketd

Pimoroni DRV2605L Linear Actuator Haptic Breakout:<br>

https://shop.pimoroni.com/products/drv2605l-linear-actuator-haptic-breakout

https://github.com/pimoroni/drv2605-python

https://ai.facebook.com/blog/hand-tracking-deep-neural-networks/

https://en.wikipedia.org/wiki/Wire_wrap

<br>Copyright (c) 2021 Hartwell Fong

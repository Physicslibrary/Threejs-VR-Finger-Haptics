#!/usr/bin/python

from drv2605 import DRV2605, PlayWaveform, WaitMillis
import sys
import time

# morse.py

# https://github.com/Physicslibrary/Threejs-VR-Finger-Haptics

# MIT License

# Copyright (c) 2021 Hartwell Fong

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# August 2021.

# Explore Raspberry Pi and Pimoroni DRV2605L python library to convert words, letters,
# and numbers to haptic morse code from python stdin (eg. raw_input()).

enable_calibration = False

drv2605 = DRV2605()
drv2605.reset()

drv2605.set_feedback_mode('LRA')
drv2605.set_library('LRA')

pattern = 118

drv2605.set_sequence(PlayWaveform(pattern))

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ']

morse = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110',' ']

# dit-dash is international morse
# dit = 0
# dash = 1
# space between characters is 3 dits
# space between words is 7 dits
# space between 0 and 1 is 1 dit

# experimental morse.py does not implement wpm

# uncomment the 2 print() below to see output or debugging
# comment them out when using with threejs_vr_finger_haptic.html and websocketd

while True:
        
        y = raw_input()
        # y = raw_input("enter letters: ")
        if(y == 'exit'):
                break
        y = ','.join(y)
        y = y.split(',')
        # print(y)

        for i in y:
                for j in range(len(letter)):
                        if(i == letter[j]):
                                # print(morse[j])
                                time.sleep(0.3)
                      
                                for k in morse[j]:
                                        
                                        if(k == '0'):
                                                drv2605.go()
                                                time.sleep(0.1)
                                                drv2605.stop()
                                                time.sleep(0.1)
                                                
                                        if(k == '1'):
                                                drv2605.go()
                                                time.sleep(0.3)
                                                drv2605.stop()
                                                time.sleep(0.1)
                                        
                                        if(k == ' '):
                                                time.sleep(0.7)

drv2605.set_realtime_input(0)
drv2605.stop()
sys.exit()

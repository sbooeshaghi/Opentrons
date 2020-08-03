# Opentrons

How to control the OT-1 lab robot?
This file explains how to write protocols and how to run them with the Opentrons app. The repository furthermore contains additional example protocols and hardware ... files.

## Overview
The following steps summarize how to write and test protocol code and subsequently upload it to the opentrons robot for running . (These will be explained more elaborately further on):

1. Write the code in jupyter notebook and test if it runs without errors. To be clear, at this point you are not running on the robot, you are simply simulating a run to see if the code doesn’t contain errors.
2. Once you designed the desired protocol and the code runs without errors, you transform the notebook to a python script 
3. Upload the python script to the Opentrons-One App
4. Calibrate the instruments on the deck of the opentrons robot (the pipette and the position of the tipracks, wells,...)
5. Run the protocol (by pressing the Run Job button in the Opentrons App)

If you want to run the same protocol again at a later time, repeat steps 3-5. One remark on recalibration (step 4): once you calibrate for a specific script, the app stores this calibration data, however it is good practice to check if all instruments still line up as expected.

## Before starting: Connect robot and install OT App.
First things first, before we start writing a protocol, let’s try to simply move the robot using the OT-1 App. First, we have to power and connect the robot. Plug the power cable into the power outlet and the usb cable into your laptop. Then press the power button.

<img src="media/powerUsb.png" width="300"> *Connect to the power outlet and plug the usb cable in your laptop. Press the power button.*

Secondly, download the Opentrons 1 App from the opentrons site: https://opentrons.com/ot-app/. *Remark: Make sure you download the OT-1 and not the OT-2 app.
Opentrons made 2 lab robots: The opentrons 1 and the opentrons 2. Opentrons 1 was, it seems, intended to be the prototype of opentrons 2. So most documentation you find on the opentrons website is on OT-2.* 
When you open the app you get a screen that looks like this: 

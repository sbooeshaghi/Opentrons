# Opentrons

How to control the OT-1 lab robot?
This file explains how to write protocols and how to run them with the Opentrons app. The repository furthermore contains additional example protocols and hardware ... files.

<img src="media/OT1LabRobot.png" width="300"> *The OT-1 Lab robot*
## Overview
The following steps summarize how to write and test protocol code and subsequently upload it to the opentrons robot for running . (These will be explained more elaborately further on):

1. Write the code in jupyter notebook and test if it runs without errors. To be clear, at this point you are not running on the robot, you are simply simulating a run to see if the code doesn’t contain errors.
1. Once you designed the desired protocol and the code runs without errors, you transform the notebook to a python script 
1. Upload the python script to the Opentrons-One App
1. Calibrate the instruments on the deck of the opentrons robot (the pipette and the position of the tipracks, wells,...)
1. Run the protocol (by pressing the Run Job button in the Opentrons App)

If you want to run the same protocol again at a later time, repeat steps 3-5. One remark on recalibration (step 4): once you calibrate for a specific script, the app stores this calibration data, however it is good practice to check if all instruments still line up as expected.

## Before starting: Connect robot and install OT App.
First things first, before we start writing a protocol, let’s try to simply move the robot using the OT-1 App. First, we have to power and connect the robot. Plug the power cable into the power outlet and the usb cable into your laptop. Then press the power button.

<img src="media/powerUsb.png" width="300"> *Connect to the power outlet and plug the usb cable in your laptop. Press the power button.*

Secondly, download the Opentrons 1 App from the opentrons site: https://opentrons.com/ot-app/. *Remark: Make sure you download the OT-1 and not the OT-2 app.
Opentrons made 2 lab robots: The opentrons 1 and the opentrons 2. Opentrons 1 was, it seems, intended to be the prototype of opentrons 2. So most documentation you find on the opentrons website is on OT-2.* 
When you open the app you get a screen that looks like this:
<img src="media/OT1App.png" width="700">
*The layout of the OT-1 App.*

You want to select the port that has a name similar to:
  */dev/tty.usbmodemFD121*
Then the app will suggest to home the robot. If you press ok, the robot will move to its home position.

If all went well, you can now play with the buttons and move the robot around. X,Y and Z coordinates are controlled through the Pipette Jog buttons. The Plunger Jog buttons are responsible for moving the pipette plunger following a system as shown in gif below:

<img src="media/Jog.gif" width="400"> *Controlling the plunger.*

## Step 1: write protocol
We will consider a simple test code which uses an 8-channel 200 µl pipette to transfer 100 µl of liquid from the first to the second row of a 200 µl 96-wells plate.

<img src="media/theDeckDrawing.png" width="300">*Illustration of the example protocol*

~~~

## Use the Opentrons API's containers and instruments
from opentrons import containers, instruments


## PART I: Add containers and pipettes:
# containers:
# Add a 96 well plate of 20 mm deep, and place it in slot 'C3'
plate = containers.load('96-well-plate-20mm', 'C3', 'plate')
# Add a 200uL tip rack, and place it in slot 'B3'
tiprack = containers.load('tiprack-200ul', 'B3','tiprack')

# pipettes:
# Add a 200uL 8 channel pipette to axis 'a', and tell it to use that tip rack
pipette = instruments.Pipette(
    axis='a',
    channels=8,
    max_volume=200, tip_racks=[tiprack])
    
    
## PART II: Specify protocol
# commands:
# Transfer 100uL from the plate's first row of wells to it's second row of wells.
pipette.transfer(100, plate.rows[0], plate.rows[1])

~~~

*Code of the example protocol*

### Testing in jupyter notebooks

To make sure you are using correct commands when writing the code, it is a good idea to use the opentrons python package and run the code in e.g. jupyter notebooks to see if you get any errors (the robot won’t work, but you can at least see if the code runs).

To install the package run:
~~~
>> pip install opentrons == 2.5.2
~~~
Once the package is installed you can start writing protocols. The example shown in Snippet 1 already contains the most important commands and the typical structure of a protocol:
* Adding the containers
* Adding the pipette(s)
* Specifying the commands

A good overview of the opentrons API (for OT1) can be found here: https://docs.opentrons.com/ot1/index.html. Taking a look at these pages is probably the easiest method to go a long way in writing protocols.

*Remark: When adding a container it is important to choose a container that has the exact right dimensions to avoid collisions with the robot. E.g. The '96-well-plate-20mm' is well specified because ‘96-well’ plates have standard well positions and the depth is in this case 20 mm. The dimensions of this plate correspond exactly to the dimensions of the physical plate used in the example.  A list of all built in containers can be found here: https://docs.opentrons.com/ot1/containers.html#labware-library. It is also possible to make your own custom containers.
* 

### Adding print commands
While testing the protocol you can add some print statements to get additional feedback on the code. A useful tool is the robot package from which you can print the robot commands. 

<pre>

<b>from opentrons import robot
robot.clear_commands()</b>

## Use the Opentrons API's containers and instruments
from opentrons import containers, instruments


## PART I: Add containers and pipettes:
# containers:
# Add a 96 well plate of 20 mm deep, and place it in slot 'C3'
plate = containers.load('96-well-plate-20mm', 'C3', 'plate')
# Add a 200uL tip rack, and place it in slot 'B3'
tiprack = containers.load('tiprack-200ul', 'B3','tiprack')

<b> print(plate,tiprack) </b>

# pipettes:
# Add a 200uL 8 channel pipette to axis 'a', and tell it to use that tip rack
pipette = instruments.Pipette(
    axis='a',
    channels=8,
    max_volume=200, tip_racks=[tiprack])
<b> print(pipette.max_volume)  </b>   
    
## PART II: Specify protocol
# commands:
# Transfer 100uL from the plate's first row of wells to it's second row of wells.
pipette.transfer(100, plate.rows[0], plate.rows[1])

<b> for c in robot.commands():
    print(c) </b>
</pre>
*Code of the example protocol with additional print statements*

These print statements can be removed in the eventual protocol (the robot just ignores them when running the protocol) but are a good first check of your code.  For this code the output becomes:

<pre>
<Container plate> <Container tiprack>
200
Picking up tip from <WellSeries: <Well A1><Well B1><Well C1><Well D1><Well E1><Well F1><Well G1><Well H1>>
Aspirating 100.0 at <WellSeries: <Well A1><Well B1><Well C1><Well D1><Well E1><Well F1><Well G1><Well H1>>
Dispensing 100.0 at <WellSeries: <Well A2><Well B2><Well C2><Well D2><Well E2><Well F2><Well G2><Well H2>>
Returning tip
Drop_tip at <WellSeries: <Well A1><Well B1><Well C1><Well D1><Well E1><Well F1><Well G1><Well H1>>
</pre>
*Output of code with additional print statements using jupyter notebooks*

## Step 2: convert protocol to script
Once your protocol runs on jupyter notebooks, you make it into a python script. (I just paste it into a plain text document and add .py extension). The script has been uploaded in the folder


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

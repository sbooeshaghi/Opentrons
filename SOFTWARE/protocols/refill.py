## Use the Opentrons API's containers and instruments
from opentrons import containers, instruments

## PART I: Add containers and pipettes:
# containers
# Add a 96 well plate of 20 mm deep, and place it in slot 'C3'
plate = containers.load('96-well-plate-20mm', 'C3', 'plate')
# Add a refill reservoir in slot 'D3'
refillres = containers.load('point', 'D3', 'refillres')
# Add a 200uL tip rack, and place it in slot 'B3'
tiprack = containers.load('tiprack-200ul', 'B3','tiprack')
# Add a trash container in slot 'B2'
trash = containers.load('point', 'B2', 'trash')

# pipettes
# Add a 200uL 8 channel pipette to axis 'a', and tell it to use that tip rack and trash container
pipette = instruments.Pipette(
    axis='a', # weird difference between a and b
    channels=8, 
    max_volume=200, tip_racks=[tiprack],
    trash_container=trash)

## PART II: Specify protocol
# commands
# Transfer 200uL from the refill reservoir to the plate's first row of wells.
pipette.transfer(200, refillres, plate.rows[0])


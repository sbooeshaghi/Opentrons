#SPLIT POOL BARCODING PROTOCOL

from opentrons import containers, instruments


# containers
hairpinres = containers.load('PCR-strip-tall', 'C3', 'hairpinres')
beadres1 = containers.load('PCR-strip-tall', 'C2', 'beadres1')
beadres2 = containers.load('PCR-strip-tall', 'D2', 'beadres2')
tiprack = containers.load('tiprack-200ul', 'B3','tiprack')
trash = containers.load('point', 'B2', 'trash')

# pipettes
pipette = instruments.Pipette(
    axis='a',
    channels=8, 
    max_volume=200, tip_racks=[tiprack],
    trash_container=trash)

# commands
pipette.transfer(200, hairpinres.rows[0:6], beadres1.rows[0:12:2],
                 new_tip='always',mix_after=(2, 75))
pipette.transfer(200, hairpinres.rows[6:12], beadres2.rows[0:12:2],
                 new_tip='always',mix_after=(2, 75))  # mix 2 times with 75uL after dispensing

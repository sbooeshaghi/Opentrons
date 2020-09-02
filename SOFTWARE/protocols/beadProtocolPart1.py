from opentrons import containers, instruments


#BEADPROTOCOL PART 1!



from opentrons import containers, instruments


# containers
hairpinres = containers.load('96-PCR-flat', 'C3', 'hairpinres')
beadres1 = containers.load('96-PCR-flat', 'C1', 'beadres1')
beadres2 = containers.load('96-PCR-flat', 'D1', 'beadres2')
tiprack = containers.load('tiprack-200ul', 'B3','tiprack')
trash = containers.load('point', 'B2', 'trash')
print(hairpinres,beadres1,beadres2,tiprack,trash)

# pipettes
pipette = instruments.Pipette(
    axis='a', # weird difference between a and b
    channels=8, 
    max_volume=200, tip_racks=[tiprack],
    trash_container=trash)

# strange: extra commands needed?
#print('max_volume = ', pipette.max_volume)
pipette.max_volume = 200
#print('max_volume = ', pipette.max_volume)
#print('channels = ', pipette.channels)
#print('wells hairpin reservoir', hairpinres.rows[0:2])

# commands

pipette.transfer(200, hairpinres.rows[0:6], beadres1.rows[0:12:2], new_tip='always',mix_after=(2, 75)) # how many mul to mix?
pipette.transfer(200, hairpinres.rows[6:12], beadres2.rows[0:12:2], new_tip='always',mix_after=(2, 75))  # mix 2 times with 75uL after dispensing


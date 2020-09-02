from opentrons import containers, instruments


# containers
hairpinres = containers.load('96-PCR-flat', 'C3', 'hairpinres')
refillstation = containers.load('96-PCR-flat', 'D3', 'refillstation')
tiprack = containers.load('tiprack-200ul', 'B3','tiprack')
trash = containers.load('point', 'B2', 'trash')
#print(hairpinres,refillstation,tiprack,trash)

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
#print('wells reservoir 1', reservoir1.rows[0:2])

# commands

pipette.transfer(200, refillstation.rows[0], hairpinres.rows[0:12])


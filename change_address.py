import smbus
import time

current_address = 0x70  # default

i2c = smbus.SMBus(1)

# Write commands for changing the address
new_address = 0x71
command_seq = (0xA0, 0xAA, 0xA5, new_address)

for command in command_seq:
    i2c.write_byte_data(current_address, 0, command)
    print "run {0}, {1}, {2}".format(current_address, 0, command)
    time.sleep(0.08)


print "Change address to: {0}".format(new_address) 

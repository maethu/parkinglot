import smbus
import time
import json

class ParkingSlot():

    def __init__(self, address=0x70):
        self.i2c = smbus.SMBus(1)
        self.address = address

    def get_distance(self):
        """Returns distance in cm"""
        self.i2c.write_byte_data(self.address, 0, 81)  # 81 result in cm
        time.sleep(0.08)  # 80ms snooze whilst it pings

        #it must be possible to read all of these data in 1 i2c transaction
        #buf[0] software version. If this is 255, then the ping has not yet returned
        #buf[1] unused
        #buf[2] high byte range
        #buf[3] low byte range
        #buf[4] high byte minimum auto tuned range
        #buf[5] low byte minimum auto tuned range

        distance = self.i2c.read_word_data(self.address, 2) / 255
        return distance

    def has_car(self, distance):
        """Returns bool if a car is in the slot"""

        return distance > self.get_distance()


class ParkingSlotObserver(object):

    def __init__(self, addresses=[0x70], distance=400):
        """
        Params:
        addresses = list of sensor addresses, default is 0x70
        distance = distance in cm, defines if a car is there or not
        """

        self.addresses = addresses
        self.slots = [ParkingSlot(addr) for addr in addresses]
        self.distance = distance

    def get_slot_informations(self):
        result = []
        for i, slot in enumerate(self.slots):
            data =  "Slot {0}: {1}".format(i, slot.has_car(self.distance))
            print data
            result.append(data)
        return result

    def get_json(self):
        result = []
        for i, slot in enumerate(self.slots):
            data = dict(parkinglot=i, has_car=slot.has_car(self.distance))
            result.append(data)
        return json.dumps(result)


#app = ParkingSlotObserver(distance=20)
#app.get_slot_informations()

import spidev

LED_T0 = 0b11100000
LED_T1 = 0b11111100

GREEN = (0xFF, 0x00, 0x00)
RED = (0x00, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)

class NeoPixel(object):
    def __init__(self, bus=0):
        self._bus = spidev.SpiDev()
        # the neopixel must be the only device on the bus
        self._bus.open(bus, 0)
        # this will work with videocore frequency 200~500 MHz
        self._bus.max_speed_hz = 13000000

    # turn off LEDs on deletion
    def __del__(self):
        self.write([(0,0,0)])

    # data is formatted as a list of tuples:
    # [ (g0,r0,b0), (g1,r1,b1), ... (gn,rn,bn) ]
    def write(self, data):
        prepared_data = []
        for grb in data:
            for color in grb:
                for bit in range(8):
                    if color & (1<<bit):
                        prepared_data.insert(0, LED_T1)
                    else:
                        prepared_data.insert(0, LED_T0)
        self._bus.xfer(prepared_data)

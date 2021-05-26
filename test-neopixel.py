#!/usr/bin/python3

import argparse
from neopixel import NeoPixel, RED, GREEN, BLUE
import signal
from time import sleep, time

parser = argparse.ArgumentParser(description='neopixel test')
parser.add_argument('--output', action='store', type=str, default=None)
parser.add_argument('--frequency', action='store', type=int, default=1)
parser.add_argument('--pixels', action='store', type=int, default=1)
args = parser.parse_args()

neopixel = NeoPixel()

outfile = None

if args.output:
    outfile = open(args.output, "w")

def cleanup(_signo, _stack):
    if outfile:
        outfile.close()
    exit(0)


signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

while True:
    for color in [RED, GREEN, BLUE]:
        # output the same color to all leds
        neopixel.write([color]*args.pixels)
        output = f"{time()} {args.pixels} {color}"
        print(output)
        if outfile:
            outfile.write(output)
            outfile.write('\n')

        # give the viewer some time to appreciate it
        sleep(1.0/args.frequency)

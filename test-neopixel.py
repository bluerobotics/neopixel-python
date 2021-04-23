#!/usr/bin/python3

import argparse
from neopixel import NeoPixel, RED, GREEN, BLUE
from time import sleep, time

parser = argparse.ArgumentParser(description='neopixel test')
parser.add_argument('--output', action='store', type=str, default=None)
parser.add_argument('--frequency', action='store', type=int, default=1)
parser.add_argument('--pixels', action='store', type=int, default=1)
args = parser.parse_args()

neopixel = NeoPixel()

if args.output:
    outfile = open(args.output, "w")

while True:
    for color in [RED, GREEN, BLUE]:
        # output the same color to all leds
        neopixel.write([color]*args.pixels)
        output = f"{time()} {args.pixels} {color}"
        print(output)
        if args.output:
            outfile.write(output)
            outfile.write('\n')

        # give the viewer some time to appreciate it
        sleep(1.0/args.frequency)

# this is never reached, but works anyway in practice
# todo handle KeyboardInterrupt for ctrl+c
if args.output:
    outfile.close()

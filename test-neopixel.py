#!/usr/bin/python3

import argparse
from neopixel import NeoPixel, RED, GREEN, BLUE
import llog
from pathlib import Path
from time import sleep, time


device = "neopixel"
defaultMeta = Path(__file__).resolve().parent / f"{device}.meta"

parser = argparse.ArgumentParser(description=f'{device} test')
parser.add_argument('--output', action='store', type=str, default=None)
parser.add_argument('--meta', action='store', type=str, default=defaultMeta)
parser.add_argument('--frequency', action='store', type=int, default=1)
parser.add_argument('--pixels', action='store', type=int, default=1)
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    neopixel = NeoPixel()

    while True:
        for color in [RED, GREEN, BLUE]:
            # output the same color to all leds
            neopixel.write([color]*args.pixels)
            # extract RGB components (neopixel uses G/R/B control order)
            g, r, b = color
            log.log(llog.LLOG_DATA, f"{args.pixels} {r} {g} {b}")

            # give the viewer some time to appreciate it
            sleep(1.0/args.frequency)

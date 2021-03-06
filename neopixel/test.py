#!/usr/bin/python3

def main():
    from neopixel import NeoPixel, RED, GREEN, BLUE
    from llog import LLogWriter
    import time


    device = "neopixel"
    parser = LLogWriter.create_default_parser(__file__, device, default_frequency=256)
    parser.add_argument('--pixels', action='store', type=int, default=1)
    args = parser.parse_args()


    with LLogWriter(args.meta, args.output, console=args.console) as log:
        neopixel = NeoPixel()

        if args.frequency:
            delay = 1 / args.frequency

        start_time = time.time()
        while time.time() < start_time + args.duration:
            for color in [(1,0,0), (0,1,0), (0,0,1)]:
                for brightness in range(256):

                    try:
                        c = [i*brightness for i in color]
                        # output the same color to all leds
                        neopixel.write([c]*args.pixels)
                        # extract RGB components (neopixel uses G/R/B control order)
                        g, r, b = c
                        log.log_data(f"{args.pixels} {r} {g} {b}")
                    except Exception as e:
                        log.log_error(e)
                        if args.stop_on_error:
                            return

                    if args.frequency:
                        # give the viewer some time to appreciate it
                        time.sleep(delay)

if __name__ == '__main__':
    main()

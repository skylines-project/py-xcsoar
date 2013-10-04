from collections import namedtuple
from subprocess import Popen, PIPE
from itertools import imap

FlightPathFix = namedtuple('FlightPathFix', [
    'seconds_of_day',
    'latitude',
    'longitude',
    'altitude',
    'enl',
])


def flight_path(path, start=None, end=None, max_points=None):
    args = ['FlightPath']

    if start:
        args.append('--start={:d}'.format(start))

    if end:
        args.append('--end={:d}'.format(end))

    if max_points:
        args.append('--max-points={:d}'.format(max_points))

    args.append(path)

    def line_to_fix(line):
        line = line.split()
        return FlightPathFix(
            int(line[0]),
            float(line[1]),
            float(line[2]),
            int(line[3]),
            int(line[4])
        )

    return imap(line_to_fix, Popen(args, stdout=PIPE).stdout)



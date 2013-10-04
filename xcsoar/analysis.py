try:
    import simplejson as json
except ImportError:
    import json

from subprocess import Popen, PIPE


def analyse_flight(path, full_points=None, triangle_points=None, sprint_points=None, popen_kwargs=None):
    args = ['AnalyseFlight']

    if full_points:
        args.append('--full-points={:d}'.format(full_points))

    if triangle_points:
        args.append('--triangle-points={:d}'.format(triangle_points))

    if sprint_points:
        args.append('--sprint-points={:d}'.format(sprint_points))

    args.append(path)

    output = Popen(args, stdout=PIPE, **(popen_kwargs or {})).stdout
    return json.load(output)

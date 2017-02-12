from os.path import dirname, abspath, join
from collections import namedtuple

from pytest import approx

FIXTURES_PATH = join(dirname(abspath(__file__)), 'fixtures')

Fix = namedtuple('Fix', [
    'datetime',
    'clock',
    'location',
    'gps_altitude',
    'pressure_altitude',
    'enl',
    'trt',
    'gsp',
    'tas',
    'ias',
    'siu',
    'elevation',
    'level'
])


def test_something():
    from xcsoar import Flight

    flight = Flight(join(FIXTURES_PATH, '654g6ng1.igc'))
    path = flight.path()
    assert len(path) == 9762

    second_fix = Fix(*path[1])
    assert second_fix.datetime.isoformat() == '2016-05-04T08:10:50'
    assert second_fix.clock == 29450
    assert second_fix.location['latitude'] == approx(50.82191666668235)
    assert second_fix.location['longitude'] == approx(6.181650000001908)
    assert second_fix.gps_altitude == 230
    assert second_fix.pressure_altitude == 48
    assert second_fix.enl == None
    assert second_fix.trt == None
    assert second_fix.gsp == 0
    assert second_fix.tas == None
    assert second_fix.ias == None
    assert second_fix.siu == 8
    assert second_fix.elevation == None
    assert second_fix.level == 0

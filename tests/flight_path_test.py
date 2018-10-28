from os.path import dirname, abspath, join
from collections import namedtuple

from pytest import approx

FIXTURES_PATH = join(dirname(abspath(__file__)), "fixtures")

Fix = namedtuple(
    "Fix",
    [
        "datetime",
        "clock",
        "location",
        "gps_altitude",
        "pressure_altitude",
        "enl",
        "trt",
        "gsp",
        "tas",
        "ias",
        "siu",
        "elevation",
        "level",
    ],
)


def test_path():
    from xcsoar import Flight

    flight = Flight(join(FIXTURES_PATH, "654g6ng1.igc"))
    path = flight.path()
    assert len(path) == 9762

    second_fix = Fix(*path[1])
    assert second_fix.datetime.isoformat() == "2016-05-04T08:10:50"
    assert second_fix.clock == 29450
    assert second_fix.location["latitude"] == approx(50.82191666668235)
    assert second_fix.location["longitude"] == approx(6.181650000001908)
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

    other_fix = Fix(*path[4321])
    assert other_fix.datetime.isoformat() == "2016-05-04T12:59:46"
    assert other_fix.clock == 46786
    assert other_fix.location["latitude"] == approx(49.510716666681944)
    assert other_fix.location["longitude"] == approx(9.105166666669477)
    assert other_fix.gps_altitude == 2050
    assert other_fix.pressure_altitude == 1913
    assert other_fix.enl == None
    assert other_fix.trt == 19
    assert other_fix.gsp == 143
    assert other_fix.tas == None
    assert other_fix.ias == None
    assert other_fix.siu == 10
    assert other_fix.elevation == None
    assert other_fix.level == 0


def test_path_of_path():
    from xcsoar import Flight

    flight = Flight(join(FIXTURES_PATH, "654g6ng1.igc"))
    path = flight.path()
    assert len(path) == 9762

    flight2 = Flight(path)
    path2 = flight2.path()
    assert len(path2) == 9762

    fix = Fix(*path2[4321])
    assert fix.datetime.isoformat() == "2016-05-04T12:59:46"
    assert fix.clock == 46786
    assert fix.location["latitude"] == approx(49.510716666681944)
    assert fix.location["longitude"] == approx(9.105166666669477)
    assert fix.gps_altitude == 2050
    assert fix.pressure_altitude == 1913
    assert fix.enl == None
    assert fix.trt == 19
    assert fix.gsp == 143
    assert fix.tas == None
    assert fix.ias == None
    assert fix.siu == 10
    assert fix.elevation == None
    assert fix.level == 0


def test_reduce():
    from xcsoar import Flight

    flight = Flight(join(FIXTURES_PATH, "654g6ng1.igc"))
    assert len(flight.path()) == 9762

    flight.reduce(threshold=0, max_points=5000)
    assert len(flight.path()) < 5000

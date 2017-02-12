from os.path import dirname, abspath, join
from datetime import datetime

from pytest import approx

FIXTURES_PATH = join(dirname(abspath(__file__)), 'fixtures')


def test_times():
    from xcsoar import Flight

    flight = Flight(join(FIXTURES_PATH, '654g6ng1.igc'))
    times = flight.times()
    assert times == [{
        'takeoff': {
            'time': datetime(2016, 5, 4, 8, 12, 46),
            'location': {
                'latitude': approx(50.822250),
                'longitude': approx(6.183766),
            },
        },
        'release': {
            'time': datetime(2016, 5, 4, 8, 18, 6),
            'location': {
                'latitude': approx(50.8224),
                'longitude': approx(6.173383),
            },
        },
        'landing': {
            'time': datetime(2016, 5, 4, 18, 59, 42),
            'location': {
                'latitude': approx(50.82215),
                'longitude': approx(6.189316),
            },
        },
        'power_states': [],
    }]


def test_enl_times():
    from xcsoar import Flight

    flight = Flight(join(FIXTURES_PATH, '2016-09-29-tri-x9z-01.igc'))
    times = flight.times()
    assert times == [{
        'takeoff': {
            'location': {
                'latitude': approx(49.95428333334875),
                'longitude': approx(8.973000000002768)
            },
            'time': datetime(2016, 9, 29, 11, 49, 57),
        },
        'release': {
            'location': {
                'latitude': approx(49.89760000001539),
                'longitude': approx(8.939000000002759)
            },
            'time': datetime(2016, 9, 29, 11, 55, 26),
        },
        'landing': {
            'location': {
                'latitude': approx(49.952733333348746),
                'longitude': approx(8.969233333336101)
            },
            'time': datetime(2016, 9, 29, 14, 30, 10),
        },
        'power_states': [{
            'time': datetime(2016, 9, 29, 11, 47, 53),
            'powered': True,
            'location': {
                'latitude': approx(49.95466666668209),
                'longitude': approx(8.974033333336102)
            },
        }, {
            'time': datetime(2016, 9, 29, 11, 56, 19),
            'powered': False,
            'location': {
                'latitude': approx(49.8889000000154),
                'longitude': approx(8.944816666669427)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 2, 55),
            'powered': True,
            'location': {
                'latitude': approx(49.89323333334873),
                'longitude': approx(8.94906666666943)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 6, 32),
            'powered': False,
            'location': {
                'latitude': approx(49.882933333348724),
                'longitude': approx(8.91540000000275)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 21, 16),
            'powered': True,
            'location': {
                'latitude': approx(49.83453333334871),
                'longitude': approx(8.857000000002731)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 25, 40),
            'powered': False,
            'location': {
                'latitude': approx(49.80421666668204),
                'longitude': approx(8.805150000002715)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 31, 39),
            'powered': True,
            'location': {
                'latitude': approx(49.76806666668203),
                'longitude': approx(8.731766666669362)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 35, 24),
            'powered': False,
            'location': {
                'latitude': approx(49.75056666668202),
                'longitude': approx(8.679766666669346)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 47, 20),
            'powered': True,
            'location': {
                'latitude': approx(49.604516666681974),
                'longitude': approx(8.660016666669339)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 50, 46),
            'powered': False,
            'location': {
                'latitude': approx(49.58675000001531),
                'longitude': approx(8.650300000002668)
            },
        }, {
            'time': datetime(2016, 9, 29, 12, 56, 42),
            'powered': True,
            'location': {
                'latitude': approx(49.492666666681934),
                'longitude': approx(8.67593333333601)
            },
        }, {
            'time': datetime(2016, 9, 29, 13, 0, 47),
            'powered': False,
            'location': {
                'latitude': approx(49.44688333334859),
                'longitude': approx(8.706983333336021)
            },
        }, {
            'time': datetime(2016, 9, 29, 13, 5, 3),
            'powered': True,
            'location': {
                'latitude': approx(49.50903333334861),
                'longitude': approx(8.680666666669346)
            },
        }, {
            'time': datetime(2016, 9, 29, 13, 16, 11),
            'powered': False,
            'location': {
                'latitude': approx(49.5882500000153),
                'longitude': approx(9.023900000002785)
            },
        }],
    }]

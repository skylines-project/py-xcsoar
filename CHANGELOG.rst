CHANGELOG
=========

0.6.3
-----

- Fix wheel compatibility tags


0.6.2
-----

- Update to XCSoar 6.8.11


0.6.1
-----

- Adjusted wheel distribution


0.6
---

- Add Python 3 support


0.5
---

Use XCSoar 6.8.2 codebase.


0.4.2
-----

- Fix installation on Mac OSX


0.4.1
-----

Update xcsoar source to latest 6.8 development version:

- adding RMZ airspaces

- fixing a endless loop bug in the replay code


0.4
---

Add interface to XCSoar's airspace warning code.


0.3
-----

- update XCSoar source to the latest 6.8 development version

- add QNH processing


0.2.1
-----

Update XCSoar source to fix some issues:

- fix double free due to incorrect DECREF in Flight.encode()

- fix two other improbable memory leaks

- conversion to RoughAltitude rounds fixed/double numbers before casting to
  short to prevent wrong rounding

0.2
---
First version with c++ python interface to XCSoar.

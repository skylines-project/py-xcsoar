CHANGELOG
=========

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

py-xcsoar
=========

XCSoar flight analysis tools


Contents
--------

AnalyseFlight
  The AnalyseFlight tool will run an IGC file through the XCSoar flight
  analysis engine and return the results in JSON format. It expects the path
  to the IGC file as a command line parameter and returns its output on stdout.

FlightPath
  The FlightPath utility reads an IGC file and extracts the relevant
  information into an easily parsable format including the seconds since
  midnight, location, altitude and engine noise level. Like AnalyseFlight it
  also expects the IGC filename on the command line and returns its output on
  stdout.

XCSoar python package
  The XCSoar python package contains python wrapper for the above utilities.
  Import the ``xcsoar`` package to take advantage of the ``flight_path`` and
  ``analyse_flight`` functions.


Installation
------------

You can install the XCSoar tools like any other python script by calling
``python setup.py install``. It will automatically compile the tools and
install them to an appropriate location.

You will most likely need to install a few of XCSoar's build dependencies.
On a standard Ubuntu machine calling ``apt-get install make
libcurl4-openssl-dev`` should get you started. Please read the XCSoar
documentation if there are more libraries missing.


License
-------

::

  XCSoar Glide Computer - http://www.xcsoar.org/
  Copyright (C) 2000-2013 The XCSoar Project
  A detailed list of copyright holders can be found in the file "AUTHORS".

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

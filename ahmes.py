#!/usr/bin/python3

#    Ahmes.py - makes worksheets for students to study from
#    Copyright (C) 2018  Derek Klinge
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys

from Scribe.scribe import Scribe
from Scribe.live_scribe import LiveScribe

def main():
	if len(sys.argv) < 2:
		ahmes = LiveScribe()
		ahmes.main_loop()
	elif len(sys.argv) == 3:
		ahmes = Scribe()
		ahmes.write(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
	main()

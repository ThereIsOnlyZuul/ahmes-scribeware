#!/usr/bin/python3

import sys

from Scribe.scribe import Scribe

def main():
	ahmes = Scribe()
	ahmes.write(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
	main()
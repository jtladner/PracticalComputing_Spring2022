#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--num", help="Number of hits to report")

args = parser.parse_args()
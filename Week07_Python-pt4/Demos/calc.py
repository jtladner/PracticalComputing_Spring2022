#!/usr/bin/env python

import argparse



parser = argparse.ArgumentParser()
parser.add_argument("a", type=float, help="First number to use in calculation")
parser.add_argument("b", type=float, help="Second number to use in calculation")
parser.add_argument("-o", "--operation", default="+", choices=["+", "-", "*", "/", "**", "%"], help="Operation to perform")
args = parser.parse_args()

if args.operation == "+":
    print(args.a+args.b)
elif args.operation == "-":
    print(args.a-args.b)
elif args.operation == "*":
    print(args.a*args.b)
elif args.operation == "/":
    print(args.a/args.b)
elif args.operation == "**":
    print(args.a**args.b)
elif args.operation == "%":
    print(args.a%args.b)

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:21:59 2020

@author: achoud3
"""


import argparse
import sys

parser = argparse.ArgumentParser(
		description=__doc__,
		formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('date', help='',default='YYYY-MM-DD')
	args = parser.parse_args()
	a=datetime.datetime.now()
print (parser)
print (a)
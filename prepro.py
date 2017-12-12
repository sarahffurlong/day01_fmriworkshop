#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:00 2017

@author: Sarah
"""

#always load modules at beginning, helpful for others using your script
import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    #something
    print('Hello data in the path '+basedir)
def main():
    #load in all global variables prepro needs, right now this is just the path to the data
    basedir='/Users/Sarah/desktop/fmri_workshop/'
    prepro(basedir) #call prepro to do stuff
    
main()#call main to execute all our globals then run our prepro function
        



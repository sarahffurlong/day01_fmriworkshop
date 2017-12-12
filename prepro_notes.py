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
        
#for preprocessing, want skull stripping, motion correction (creating motion regressors, creating framewise displacement
# regressor - easy to read html, re-orient? trime extra TRs? we won't do these two here, but Grace's github has that script)

#anything that is variable in main, it will be a parameter for prepro() function

#with os system can wrap a linux command and execute it through python

#need input, that is usually path to where data is
#for example, input='/Users/gracer/Desktop/data/<subject number>/func/<nifiti_file>'
#this is BIDS format

#glob module can find everything with a similar path:
# input=glob.glob('/Users/gracer/Desktop/data/sub-*/func/sub-*.nii.gz')
# print(input[0:10])
# * is a wildcard can be anything that can be exchanged for anything else
# glob.glob is module glob and then function glob tha thappens to have the same name
#glob produces a list, which can have booleans, strings, etc.

#to get more specfic, input=glob.glob('/Users/gracer/Desktop/data/sub-*/func/sub-*bart*.nii.gz'), or copy whole path and replace any sub number with *
# this creates a list made up entirely of strings
# often we want to parse those strings apart so that we could just pull out the subj number

##x=input[1]
#print('my path is '+x)
#y=x.split('/')
#here the split command splits apart the string whenever there is a /
#first slash is 0th slash
# nice two lines for this:

sub=input[1].split('/')[5]
print(sub)

path=os.path.join(basedir,'sub-*','func','sub-*.nii.gz')
#i=os.path,join formats the path for you!


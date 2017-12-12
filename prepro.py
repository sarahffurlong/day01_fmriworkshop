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
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*.nii.gz')):
        input=item
        print item
        output_path=item.strip('.nii.gz')
        output=output_path+('_brain')
        print output
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
        #pdb.set_trace()
def main():
    basedir='/Users/Sarah/desktop/data/ds000030_R1.0.5/'
    prepro(basedir)

main()
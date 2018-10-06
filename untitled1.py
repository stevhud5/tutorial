# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:45:10 2018

@author: cna2
"""
import sys
sys.path.append('L:\NIST_Projects\FluidSuspensionsEmulsions\Software\InstrumentPyFiles')

from qmixsdkpy import CetoniCore
import logging
import time
from ElveFlowDev import*
from NIDAQPressure import NIDAQPressure
import numpy as np
from DataSteady import DataSteady
from pythics.lib import GrowableArray
import matplotlib.pyplot as plt
from UserDB import*

import os

class Private(object):
    pass

private = Private()

Pcalib = np.load("L:\\NIST_Projects\FluidSuspensionsEmulsions\Software\InstrumentCalibrations\PSensorCalibrations\\tests\ReRun.A.180313\Data0.npy")
#timedata = np.load(load_data_filename.value+'timedata.npy')
#private.data.clear()
private.PressureCalib=Pcalib

print Pcalib
print 'offset: ',private.PressureCalib['offset'][0],' ',private.PressureCalib['offset'][1]
print 'slope: ', private.PressureCalib['slope'][0],' ',private.PressureCalib['slope'][1]
   
        

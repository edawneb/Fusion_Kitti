#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:52:55 2021

@author: ben
"""

'''
TO DO: 
    Path Directory Reference Files - done
    Sequence Object - done
    Individual file object - done
        Validity checks
        robustness testing
    Bounding box Model object
        input shape/format
            resize smaller
            maintain rgb
            3d(left, right, velo)
                calib velo/images for overlap
        Conifuruation file
        init object
    Bounding Box Cache Obejct-> probably can be done end to end with RNN/self attention
        config file
        init object
    Bounding Box Prediction Object
        configurable
        init
        execution
    Bounding Box cut method
    Communication socket
        protocol type
        optimization methods
    classification model
        configurable
    Data analysis util
    Data presentation util



'''

import DataInputUtils
import DataPaths
import SocketUtils
import models

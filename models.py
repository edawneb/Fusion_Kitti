#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:49:58 2021

@author: ben
"""

from torch.distributed.pipeline.sync import Pipe, pipeline, batchnorm
from torch.nn import LSTM, RNN, Transformer, TransformerEncoder, TransformerDecoder, Dropout, Dropout2d, Dropout3d, Softmax, Softmax2d, Maxpool1d, Maxpool2d, Conv2d, Conv3d
import torch.cuda
import torch.nn.functional as F
import tensorflow as tf



assert torch.cuda.is_available()
gpu = torch.device('cuda')



'''
Set up for an ablation study, each module is
established independently
'''
class Input_Module(nn.Module):#output is BB coords
    

class Classification_Module(nn.Module):#output is classification labels
    

class Projection_Module(nn.Module):#output is BB predictions for future frames
    

    
'''Here we combine the input sensor fusion layer with
the bb projection layer to try to train them end to end
but still send the classification task to an edge server
'''
class Input_Projection_Combined_Module(nn.Module):#output is prodeictions for future frames 
    

    
    
'''
This module combines all three so we can compare runtime differences with
locally run system
'''
class Unified_Module(nn.Module):#output is classification labels
    
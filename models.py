#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:49:58 2021

@author: ben
"""

from torch.distributed.pipeline.sync import Pipe, pipeline, batchnorm
from torch.nn import Module, LSTM, RNN, Transformer, TransformerEncoder, TransformerDecoder, Dropout, Dropout2d, Dropout3d, Softmax, Softmax2d, Maxpool1d, Maxpool2d, Conv2d, Conv3d
from torchvision.ops import nms, roi_pool
import torch.cuda
import torch.nn.functional as F
import tensorflow as tf
import os
 

assert torch.cuda.is_available()
gpu = torch.device('cuda')

'''
Set up for an ablation study, each module is
established independently

MAIN PROBLEMS: Getting suite of BB's and parsing them. Find a way to inherit stuff.
    SOL: Output vector of 2x2xn with nms

'''

#TODO: Get each to output multiple bounding boxes rather than 1
class Parent_Module(Module):
    class Input_Module(Module):#output is BB coords
        def __init__(self):
            self.path = './Input_Module.pth'
        
        class YOLO_Input(Module):#construction yolo but leave out class dimension in output layer
            def __init__(self):
                self.path = './YOLO_Input.pth'
                
                self.layer_1 = Conv2d(448, 448, 7)
                self.layer_2 = Conv2d(448, 448, 7)
                self.layer_3 = Maxpool2d(2, 2, 2)
                self.layer_4 = Conv2d(11)
    
    
            #output = [tx, ty, tw, th, obj score, class prob]->get rid of class prob.
            
        class FAST_YOLO_Input(Module):#construct fast yolo but leave out class dimension in output layer
            def __init__(self):
                self.path= './FAST_YOLO_Input.pth'


    class Classification_Module(Module):#output is classification labels
        def __init__(self):
            self.path = './Classification_Module.pth'

    class Projection_Module(Module):#output is BB predictions for future frames
        def __init__(self):    
            self.path = './Projection_Module.pth'
##Here we combine the input sensor fusion layer with
##the bb projection layer to try to train them end to end
##but still send the classification task to an edge server

    class Input_Projection_Combined_Module(Module):#output is prodeictions for future frames 
        def __init__(self):
            self.path = './Input_Projetion_Combined_Module.pth'
  
   

##This module combines all three so we can compare runtime differences with
##locally run system

    class Unified_Module(Module):#output is classification labels
        def __init__(self):
            self.path = './Unified_module.pth'
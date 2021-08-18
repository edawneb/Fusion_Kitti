#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:49:58 2021

@author: ben
"""

from torch.distributed.pipeline.sync import Pipe, pipeline, batchnorm
from torch.nn import ReLU, Sequential, DataParallel, Module, Linear, LSTM, RNN, Transformer, TransformerEncoder, TransformerDecoder, Dropout, Dropout2d, Dropout3d, Softmax, Softmax2d, MaxPool1d, MaxPool2d, Conv2d, Conv3d
from torchvision.ops import nms, roi_pool
from torchvision.models import resnet18, resnet34, resnet50, resnet101, resnet152, resnext50_32x4d, resnext101_32x8d, wide_resnet50_2, wide_resnet101_2
import torch.cuda
import torch.optim
import torch.nn.functional as F
#import tensorflow as tf
import os
import numpy as np
 

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
        def __init__(self, Attribute_Num = 5, Max_Objects = 20, confidence_threshold = .75, epochs = 10, loss_rate = 0.001, momentum = .9):
            self.path = './Input_Module.pth'
            self.Attribute_Num = Attribute_Num
            self.Max_Objects = Max_Objects
            self.IoU_Thresh = confidence_threshold
            self.epochs = epochs
            self.loss_rate = loss_rate
            self.momentum = momentum
            self.bbvector = np.array()
            self.scorevector = np.array()

            self.model = None
        
        def Deploy_Non_Max(self, bbvector, scorevector, IoU_Thresh):
            bbvector = nms(bbvector, scorevector, IoU_Thresh)
        
        class Psuedo_YOLO_Input(Module):#construction yolo but leave out class dimension in output layer
            
            
            def __init__(self):
                self.model
                self.path = './YOLO_Input.pth'
                #the idea is to separate each set of convolutions by a maxpool, but didn't want to declare the same
                #thing over and over (objects)
                self.layer_1 = Conv2d(in_channels = 4,out_channels = 3, kernel_size = 7)
                self.layer_2 = MaxPool2d(2, stride = 2)
                self.layer_3 = Conv2d(in_channels = 3, out_channels = 192, kernel_size = 3)
                self.layer_4 = Conv2d(in_channels = 192, out_channels = 256, kernel_size = 3)
                self.layer_5 = Conv2d(in_channels = 256, out_channels = 512, kernel_size = 3)
                self.layer_6 = Conv2d(in_channels = 512, out_channels = 1024, kernel_size = 3)
                self.layer_7 = Conv2d(in_channels = 1024, out_channels = 1024, kernel_size = 3)
                
                
                self.model = Sequential(
                        self.layer_1,
                        ReLU(),
                        self.layer_2,
                        self.layer_3,
                        ReLU(),
                        self.layer_2,
                        self.layer_4,
                        ReLU(),
                        self.layer_2,
                        self.layer_5,
                        ReLU(),
                        self.layer_2,
                        self.layer_6,
                        ReLU(),
                        self.layer_2,
                        self.layer_7,
                        ReLU(),
                        Softmax2d(),
                        self.decision_layer,
                )
            #output = [tx, ty, tw, th, obj score, class prob]->get rid of class prob.
                self.model = DataParallel(self.model, gpu)
            
            def forward(self, x):
                returner = self.model(x)
                return returner

        class ResNet(Module):
            
            
            def __init__(self, version):
                self.model
                self.switch = { 
                    0: resnet18(pretrained = False),
                    1: resnet34(pretrained = False),
                    2: resnet50(pretrained = False),
                    3: resnet101(pretrained = False),
                    4: resnet152(pretrained = False),
                    5: resnext50_32x4d(pretrained = False),
                    6: resnext101_32x8d(pretrained = False),
                    7: wide_resnet50_2(pretrained = False),
                    8: wide_resnet101_2(pretrained = False),
                    }
            
                if(isinstance(version, int)==False):
                    print("You did something wrong. There isn't a resnet version with that code")
                else:
                    self.model = self.switch.get(version, print("invalid entry"))
                
                self.model = DataParallel(self.model, gpu)

            def forward(self, x):
                returner = self.model(x)
                return returner



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
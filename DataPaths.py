#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:59:03 2021

@author: ben
"""
import os

class sequence:

    
    def __init__(self, path, length, Mr_List):
        self.path     = path
        self.length   = length
        self.lists    = Mr_List



    
class KITTIData:
    def __init__(self):
        self.BaseDir            = "/media/ben/New Volume/KITTI"
        self.Im_2_Dir_dat_test  = sequence("/data_tracking_image_2/testing/image_02", 0, self.Get_Im_2_dat_test()) 
        self.Im_2_Dir_dat_train = sequence("/data_tracking_image_2/training/image_02", 0, self.Get_Im_2_dat_train())
        self.Im_2_Dir_lab_test  = sequence("/data_tracking_label_2/testing/image_02", 0, self.Get_Im_2_lab_test())
        self.Im_2_Dir_lab_train = sequence("/data_tracking_label_2/training/image_02", 0, self.Get_Im_2_lab_train())
        self.Im_3_Dir_dat_test  = sequence("/data_tracking_image_3/testing/image_03", 0, self.Get_Im_3_dat_test())
        self.Im_3_Dir_dat_train = sequence("/data_tracking_image_3/training/image_03", 0, self.Get_Im_3_dat_train())
        self.Im_3_Dir_lab_test  = sequence("/data_track_image_3/testing/image_03", 0, self.Get_Im_3_lab_test())
        self.Im_3_Dir_lab_train = sequence("/data_track_image_3/training/image_03", 0, self.Get_Im_3_lab_train())
        self.Velo_dat_test      = sequence("/data_tracking_velodyne/testing/velodyne", 0, self.Get_velo_dat_test())
        self.Velo_dat_train     = sequence("/data_tracking_velodyne/training/velodyne", 0, self.Get_velo_dat_train())
        self.Velo_lab_test      = sequence("/data_tracking_det_2_regionlets/testing/det_02", 0, self.Get_velo_lab_test())
        self.Velo_lab_train     = sequence("/data_tracking_det_2_regionlets/training/det_02", 0, self.Get_velo_lab_train())          
        
        

        
        
        
        
        
        #Unused
        self.calib        = "data_tracking_calib"
        self.oxts         = "data_tracking_oxts"
        self.lsvm         = "data_tracking_det_2_lsvm"
        
        
    def GetDir(self, directory):
        ret = os.listdir(directory)
        for x in ret:
            x = os.path.join(directory, x)
        return ret
            
            
    def Get_Im_2_dat_test(self):
        ret = self.GetDir(self.Im_2_Dir_dat_test.path)
        self.Im_2_Dir_dat_test.length = len(ret)
        return ret

    def Get_Im_2_dat_train(self):
        ret = self.GetDir(self.Im_2_Dir_dat_train.path)
        self.Im_2_Dir_dat_train.length = len(ret)
        return ret
            
    def Get_Im_2_lab_test(self):
        ret = self.GetDir(self.Im_2_lab_test.path)
        self.Im_2_lab_test.length = len(ret)
        return ret
                
    def Get_Im_2_lab_train(self):
        ret = self.GetDir(self.Im_2_lab_train.path)
        self.Im_2_lab_train.length = len(ret)
        return ret
        
    def Get_Im_3_dat_test(self):
        ret = self.GetDir(self.Im_3_Dir_dat_test.path)
        self.Im_3_Dir_dat_test.length = len(ret)
        return ret

    def Get_Im_3_dat_train(self):
        ret = self.GetDir(self.Im_3_Dir_dat_train.path)
        self.Im_3_Dir_dat_train.length = len(ret)
        return ret
            
    def Get_Im_3_lab_test(self):
        ret = self.GetDir(self.Im_3_lab_test.path)
        self.Im_3_Dir_lab_test.length = len(ret)
        return ret
                
    def Get_Im_3_lab_train(self):
        ret = self.GetDir(self.Im_3_lab_train.path)
        self.Im_3_lab_test.length = len(ret)
        return ret
        
    def Get_velo_dat_test(self):
        ret = self.GetDir(self.Velo_dat_test.path)
        self.Velo_dat_test.length = len(ret)
        return ret
        
    def Get_velo_dat_train(self):
        ret = self.GetDir(self.Velo_dat_train.path)
        self.Velo_dat_test.length = len(ret)
        return ret
        
    def Get_velo_lab_test(self):
        ret = self.GetDir(self.Velo_lab_test.path)
        self.Velo_lab_test.length = len(ret)
        return ret
        
    def Get_velo_lab_train(self):
        ret = self.GetDir(self.Velo_lab_train.path)
        self.Velo_lab_train.length = len(ret)
        return ret
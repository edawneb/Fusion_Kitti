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

    def GetPath(self):
        ret = self.path
        return ret
    
    def GetLength(self):
        ret = self.length
        return ret

    #this is a list of directories, not the actual data
    #would pull all data into memory simulatenously, which would suck
    def GetList(self):
        ret = self.lists
        return ret
    
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
        self.test_calib        = sequence("data_tracking_calib/testing/calib", 0, self.get_test_calib())
        self.train_calib       = sequence("data_tracking_calib/training/calib", 0, self.get_train_calib())
        #unsused
        self.oxts         = "data_tracking_oxts"
        self.lsvm         = "data_tracking_det_2_lsvm"
        
    #gets a list of all files directories in a given 
    def GetDir(self, directory):
        #todo join the index to the directory
        ret = os.listdir(directory)
        for x in ret:
            x = os.path.join(directory, x)
        return ret
            
    def Get_test_calib(self):
        ret = self.GetDir(self.test_calib.path)
        self.test_calib.length = len(ret)
        return ret
            
    def Get_train_calib(self):
        ret = self.GetDir(self.train_calib.path)
        self.train_calib.length = len(ret)
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
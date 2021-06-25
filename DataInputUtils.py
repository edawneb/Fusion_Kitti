# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:08:57 2021

@author: bentw
"""
import sys,os,copy,math
import numpy as np
import PIL as Image
import DataPaths.py


#one of these per sequence of frames. If you load all sequences at once
#the pc will run out of mem

#TODO: ReadCalibs->read in the file types
class FrameSeqence:
    def init(self, root, frame_num, training_bool, set_indexer):
        self.frame_num = frame_num
        self.root = root
        self.PathPool = KITTIData 
        self.TrainingBool = training_bool
        self.SetIndex = set_indexer

        #self.IM2
        #self.IM3
        #self.velo
        self.directory = PathPool.BaseDir
        self.length = self.SetLength()    
        #calibs matrix
        self.calibs = self.ReadCalibs(self.SetIndex)
        self.Kitti_Data = LoadAll()

        #RectifyAll() Done on object call
    
    def SetLength(self):
        if(self.TrainingBool):
            length = PathPool.Im_2_Dir_dat_train.GetLength()
        else:
            length = PathPool.Im_2_Dir_dat_test.GetLength()
    
    def ReadCalibs(self, indexer):
        ret = np.zeros(4, 4)
        
        if(self.TrainingBool):
            #read the calibs from the indexer
            path = PathPool.Get_train_calib(self.index)
        else:
            path = PathPool.Get_test_calib(self.index)
        return
    
    def FileToArray(self, img):
        img.load()
        data = np.asarray(img, dtype="int32")
        return data
        

    def LoadAll(self):
        DataList = []
        Im2
        Im3
        velo
        for x in range(0, self.length):
            if(TrainingBool):
                Im2 = Image.open(self.PathPool.Im_2_Dir_train.lists[x])
                Im3 = Image.open(self.PathPool.Im_3_Dir_train.lists[x])
                velo = np.fromfile(self.PathPool.Velo_dat_train.lists[x], dtype=np.float32).reshape((-1,4))
               
            else:
                Im2 = Image.open(self.PathPool.Im_2_Dir_test.lists[x])
                Im3 = Image.open(self.PathPool.Im_3_Dir_test.lists[x])
                velo = np.fromfile(self.PathPool.Velo_dat_test.lists[x], dtype = np.float32).reshape((-1,4))
                            
            Im2 = self.FileToArray(Im2)
            Im3 = self.FileToArray(Im3)
            velo = velo[:, 0:3] # lidar xyz (front, left, up)
            
            #load the data into a tData object
            datum = Kitti_tData(image_2 = Im2, image_3 = Im3, velomap = velo, calibs = self.calibs)
            DataList.append(datum)
            
        return DataList
        
    def RectifyAll(self):
        
        for x in range(0, self.length): #length of set of images in index:
            self.Kitti_Data[x].RectifyImagesLeft()
        
        return
        
    #TODO: Rectify Images-> Follow from proj_velo2cam.py. Only rectify left. Left/right = redundant and not possible
class Kitti_tData:
    """
        Utility class to load data.
    """
    
    def __init__(self, image_2, image_3, velomap, frame_id=-1,obj_type="unset",truncation=-1,occlusion=-1,\
                 obs_angle=-10,x1=-1,y1=-1,x2=-1,y2=-1,w=-1,h=-1,l=-1,\
                 X=-1000,Y=-1000,Z=-1000,yaw=-10,score=-1000,track_id=-1, observation = False, calibs):
        """
            Constructor, initializes the object given the parameters.
        """
        
        # init object data
        self.image_2    = image_2
        self.image_3    = image_3
        self.velomap    = velomap
        self.IM_Combo   = []
        self.frame_id   = frame_id
        self.track_id   = track_id
        self.obj_type   = obj_type
        self.truncation = truncation
        self.occlusion  = occlusion
        self.obs_angle  = obs_angle
        self.x1         = x1
        self.y1         = y1
        self.x2         = x2
        self.y2         = y2
        self.w          = w
        self.h          = h
        self.l          = l
        self.X          = X
        self.Y          = Y
        self.Z          = Z
        self.yaw        = yaw
        self.score      = score
        self.ignored    = False
        self.valid      = False
        self.tracker    = -1
        self.eval_2d    = False
        self.eval_3d    = False
        self.valid      = False
        self.GroundTruth = observation
        self.shape      = []
        self.calibs     = calibs
        self.imwidth    = 1242
        self.imheight   = 345
        self.velowidth  = self.imwidth
        self.veloheight = 64        
        self.LoadData()
        self.check2d()
        self.check3d()
        self.setshape()
        self.RectifyImagesLeft()
        
    def __str__(self):
        
        #Print read data.
        
        
        attrs = vars(self)
        return '\n'.join("%s: %s" % item for item in attrs.items())

    def check2d(self):
        el2d = True
        if (self.x1==-1 or self.x2==-1 or self.y1==-1 or self.y2==-1):
            el2d = False
        self.eval_2d = el2d
                
    def check3d(self):
        el3d = True
        if (self.X==-1000 or self.Y==-1000 or self.Z==-1000):
            el3d = False
        self.eval_3d = el3d
    
    def isValid(self):
        val = False
        if self.track_id is -1 and self.obj_type != "dontcare":
            val = True
        self.isValid = val
    
    def setshape(self):
        self.shape = image_1.shape()
        
    #loads whole label file. need a line by line dealio. so we can have a sequence 
    #of each from velodyne, left, right, and groundtruth that is ennumerable
    
    #TODO take out the parameters from the function call. take that from the object data
    def LoadData(self, root, sequence_name, frame):
        filename = os.path.join(root, "%s.txt" %sequence_name)
        f = open(filename, "r")
        for i, line in enumerate(f):
            if(i == frame):
                line = line.strip()
                fields = line.split(" ")
                self.frame      = int(float(fields[0]))
                self.track_id   = int(float(fields[1]))
                self.obj_type   = fields[2].lower()
                self.truncation = int(float(fields[3]))
                self.occlusion  = int(float(fields[4]))
                self.obs_angle  = float(fields[5])
                self.x1         = float(fields[6])
                self.y1         = float(fields[7])
                self.x2         = float(fields[8])
                self.y2         = float(fields[9])
                self.h          = float(fields[10])
                self.w          = float(fields[11])
                self.l          = float(fields[12])
                self.X          = float(fields[13])
                self.Y          = float(fields[14])
                self.Z          = float(fields[15])
                self.yaw        = float(fields[16])
            
                self.check2d()
                self.check3d()
                
    def RectifyImagesLeft(self):
        #To project a point from Velodyne coordinates into the left color image,
        #you can use this formula: x = P2 * R0_rect * Tr_velo_to_cam * y
        #For the right color image: x = P3 * R0_rect * Tr_velo_to_cam * y    
        Im1 = self.image_1
        velo = self.velomap
        
        # P2 (3 x 4) for left eye
        P2 = np.matrix([float(x) for x in self.calibs[2].strip('\n').split(' ')[1:]]).reshape(3,4)
        R0_rect = np.matrix([float(x) for x in self.calibs[4].strip('\n').split(' ')[1:]]).reshape(3,3)
        # Add a 1 in bottom-right, reshape to 4 x 4
        R0_rect = np.insert(R0_rect,3,values=[0,0,0],axis=0)
        R0_rect = np.insert(R0_rect,3,values=[0,0,0,1],axis=1)
        Tr_velo_to_cam = np.matrix([float(x) for x in self.calibs[5].strip('\n').split(' ')[1:]]).reshape(3,4)
        Tr_velo_to_cam = np.insert(Tr_velo_to_cam,3,values=[0,0,0,1],axis=0)
        
        
        
        velo = np.insert(velo,3,1,axis=1).T
        velo = np.delete(velo,np.where(velo[0,:]<0),axis=1)
        cam = P2 * R0_rect * Tr_velo_to_cam * velo
        cam = np.delete(cam,np.where(cam[2,:]<0)[1],axis=1)
        
        #TODO ->get the now rectified velo map into the same array as the image. but we're much closer now.
        
        
        

def loadData(self, root_dir, cls, min_score=-1000, loading_groundtruth=False):
        """
            Generic loader for ground truth and tracking data.
            Use loadGroundtruth() or loadTracker() to load this data.
            Loads detections in KITTI format from textfiles.
        """
        # construct objectDetections object to hold detection data
        t_data  = Kitti_tData()
        data    = []
        eval_2d = True
        eval_3d = True

        seq_data           = []
        n_trajectories     = 0
        n_trajectories_seq = []
        for seq, s_name in enumerate(self.sequence_name):
            i              = 0
            filename       = os.path.join(root_dir, "%s.txt" % s_name)
            f              = open(filename, "r")
            f_data         = [[] for x in xrange(self.n_frames[seq])] # current set has only 1059 entries, sufficient length is checked anyway
            ids            = []
            n_in_seq       = 0
            id_frame_cache = []
            for line in f:
                # KITTI tracking benchmark data format:
                # (frame,tracklet_id,objectType,truncation,occlusion,alpha,x1,y1,x2,y2,h,w,l,X,Y,Z,ry)
                line = line.strip()
                fields            = line.split(" ")
                # classes that should be loaded (ignored neighboring classes)
                if "car" in cls.lower():
                    classes = ["car","van"]
                elif "pedestrian" in cls.lower():
                    classes = ["pedestrian","person_sitting"]
                else:
                    classes = [cls.lower()]
                classes += ["dontcare"]
                if not any([s for s in classes if s in fields[2].lower()]):
                    continue
                # get fields from table
                t_data.frame        = int(float(fields[0]))     # frame
                t_data.track_id     = int(float(fields[1]))     # id
                t_data.obj_type     = fields[2].lower()         # object type [car, pedestrian, cyclist, ...]
                t_data.truncation   = int(float(fields[3]))     # truncation [-1,0,1,2]
                t_data.occlusion    = int(float(fields[4]))     # occlusion  [-1,0,1,2]
                t_data.obs_angle    = float(fields[5])          # observation angle [rad]
                t_data.x1           = float(fields[6])          # left   [px]
                t_data.y1           = float(fields[7])          # top    [px]
                t_data.x2           = float(fields[8])          # right  [px]
                t_data.y2           = float(fields[9])          # bottom [px]
                t_data.h            = float(fields[10])         # height [m]
                t_data.w            = float(fields[11])         # width  [m]
                t_data.l            = float(fields[12])         # length [m]
                t_data.X            = float(fields[13])         # X [m]
                t_data.Y            = float(fields[14])         # Y [m]
                t_data.Z            = float(fields[15])         # Z [m]
                t_data.yaw          = float(fields[16])         # yaw angle [rad]
                if not loading_groundtruth:
                    if len(fields) == 17:
                        t_data.score = -1
                    elif len(fields) == 18:
                        t_data.score  = float(fields[17])     # detection score
                    else:
                        self.mail.msg("file is not in KITTI format")
                        return

                # do not consider objects marked as invalid
                if t_data.track_id is -1 and t_data.obj_type != "dontcare":
                    continue

                idx = t_data.frame
                # check if length for frame data is sufficient
                if idx >= len(f_data):
                    print ("extend f_data", idx, len(f_data))
                    f_data += [[] for x in xrange(max(500, idx-len(f_data)))]
                try:
                    id_frame = (t_data.frame,t_data.track_id)
                    if id_frame in id_frame_cache and not loading_groundtruth:
                        self.mail.msg("track ids are not unique for sequence %d: frame %d" % (seq,t_data.frame))
                        self.mail.msg("track id %d occured at least twice for this frame" % t_data.track_id)
                        self.mail.msg("Exiting...")
                        #continue # this allows to evaluate non-unique result files
                        return False
                    id_frame_cache.append(id_frame)
                    f_data[t_data.frame].append(copy.copy(t_data))
                except:
                    print (len(f_data), idx)
                    raise

                if t_data.track_id not in ids and t_data.obj_type!="dontcare":
                    ids.append(t_data.track_id)
                    n_trajectories +=1
                    n_in_seq +=1

                # check if uploaded data provides information for 2D and 3D evaluation
                if not loading_groundtruth and eval_2d is True and(t_data.x1==-1 or t_data.x2==-1 or t_data.y1==-1 or t_data.y2==-1):
                    eval_2d = False
                if not loading_groundtruth and eval_3d is True and(t_data.X==-1000 or t_data.Y==-1000 or t_data.Z==-1000):
                    eval_3d = False

            # only add existing frames
            n_trajectories_seq.append(n_in_seq)
            seq_data.append(f_data)
            f.close()

        if not loading_groundtruth:
            self.tracker=seq_data
            self.n_tr_trajectories=n_trajectories
            self.eval_2d = eval_2d
            self.eval_3d = eval_3d
            self.n_tr_seq = n_trajectories_seq
            if self.n_tr_trajectories==0:
                return False
        else:
            # split ground truth and DontCare areas
            self.dcareas     = []
            self.groundtruth = []
            for seq_idx in range(len(seq_data)):
                seq_gt = seq_data[seq_idx]
                s_g, s_dc = [],[]
                for f in range(len(seq_gt)):
                    all_gt = seq_gt[f]
                    g,dc = [],[]
                    for gg in all_gt:
                        if gg.obj_type=="dontcare":
                            dc.append(gg)
                        else:
                            g.append(gg)
                    s_g.append(g)
                    s_dc.append(dc)
                self.dcareas.append(s_dc)
                self.groundtruth.append(s_g)
            self.n_gt_seq=n_trajectories_seq
            self.n_gt_trajectories=n_trajectories
        return True
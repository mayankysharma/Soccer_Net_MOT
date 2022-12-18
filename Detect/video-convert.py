import cv2
import numpy as np
import os
from os.path import isfile, join
from tqdm import tqdm


def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort()
    # print(files)
    for i in tqdm(range(len(files))):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        # print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in tqdm(range(len(frame_array))):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
    
def main():
    pathIn= './results/yolov7-w6-t5-ep20/exp5/'
    pathOut = './results/test4.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)
if __name__=="__main__":
    main()
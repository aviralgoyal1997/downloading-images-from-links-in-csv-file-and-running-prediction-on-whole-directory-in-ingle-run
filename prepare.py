import os 
import glob
import numpy as np
import csv

image_path="/home/spartan/Desktop/allimages"
filenames=glob.glob(image_path+"/*.jpg")
s=[]
with open('names.csv','w') as csvfile:
          
     fieldnames=['name','prediction']
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
     writer.writeheader()
     for f in filenames:
         writer.writerow({'name':'%s'% f,'prediction': (str(os.popen('python classify_image.py --image %s'% f).readlines()).split('(',1)[0])})
    




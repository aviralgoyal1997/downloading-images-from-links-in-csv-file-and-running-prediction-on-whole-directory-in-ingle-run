import pandas as pd
import numpy as np
import urllib



df=pd.read_csv('/home/spartan/Desktop/exportSrilanka.csv')





a=df['attImage']
i=0





while(i<=3217):
    urllib.urlretrieve(a[i], "/home/spartan/Desktop/allimage/%s.jpg"%i)
    i=i+1


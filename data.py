import pandas as pd 


# import OS module
import os
 
# Get the list of all files and directories
path = "/home/asif/anchorblock/quant-finance-lectures/data/minute"
dir_list = os.listdir(path)


for i in dir_list:
    df = pd.read_csv(path+"/"+i)
    df2 = df.loc[df["timestamp"].between("2022-05-02", "2022-10-28")]
    df2 = df2.set_index(['timestamp'])
    df2.to_csv(i)
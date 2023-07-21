# IMPORT THE RELEVANT LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# LOAD DATASET
athletes = pd.read_csv('D:/Self Study/Olympic dataset/athlete_events.csv')
regions = pd.read_csv('D:/Self Study/Olympic dataset/noc_regions.csv')

# D:\Self Study\Olympic 

# CHECK THE FIRST 5 ROWS OF ATHELETES AND REGIONS DATASETS
print(athletes.head())
print(regions.head())

# MERGE THE BOTH DATAFRAMES
athletes_df = athletes.merge(regions, how ='left',on = 'NOC')
print(athletes_df)

# CHECK THE SIZE OF THE DATA FRAME
print (athletes_df.shape)


# COLUMN NAMES CONSISTENT 
    # ALL THE COLUMN NAMES ARE NOT STARTS IN CAPTAL LETTERS

print(athletes_df.rename(columns={'region':'Region','notes':'Notes'},inplace = True))

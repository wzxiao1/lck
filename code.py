import numpy as np 
import pandas as pd 
from raw2csv import pos
sm24_df = pd.read_csv("2024summer.csv")


sm24_df = sm24_df.drop(columns=["Country"])

# print(sm24_df.head())

high = sm24_df.sort_values(by="Win_rate", ascending=False)


# print(high.head())
print([pos])

# create lambda function to split the df into the multiple positions
# win rate most important, find the features related to each group with mutual information
# for row in data, put player's name in dictionary check, place them in the attribute's bucket

# no need for lambda function, just use a evaluator

support = sm24_df[pos[sm24_df["Player"]] == "Support"]
print(support)
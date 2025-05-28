import pandas as pd
#open file
#iterate each line remove blank and replace with ,

# with open("2024summer.txt", "r") as f, open("2024summer.csv", "w") as fout:
#     for line in f:
#         new = line.strip().split()
#         if new:
#             fout.write(",".join(new) + '\n')


with open("2024positions.txt", "r") as f, open("2024positions.csv", "w") as fout:
    for line in f:
        new = line.strip().split()
        if new:
            fout.write(",".join(new) + '\n')

# get position, add positioning to every future 


# create dictionary instead
positions_df = pd.read_csv("2024positions.csv", usecols=["Player", "Position"])
pos = positions_df.set_index('Player')["Position"].to_dict()

print(pos)





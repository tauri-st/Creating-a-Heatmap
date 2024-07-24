import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csvfile:
  tips = pd.read_csv(csvfile)

#define the dataframe
tips_pivoted = tips.pivot_table(values="tip", index=["size"], columns=["time"])


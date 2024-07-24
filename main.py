import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csvfile:
  tips = pd.read_csv(csvfile)

#define the dataframe
tips_pivoted = tips.pivot_table(values="tip", index=["size"], columns=["time"])

#creat a heat map using the dataframe with annotations and a coolwarm color palette
fig = sns.heatmap(tips_pivoted, annot=True, cmap="coolwarm")

fig.set_ylim(0,5)

plt.xlabel("Meal Time")
plt.ylabel("Size of Group")

plt.title("Average Tips by Group Size and Meal Time")

plt.savefig("tips-by-group-and-time.png")
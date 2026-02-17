import seaborn as sns
import matplotlib.pyplot as plt
marks=[50,60,70,80,90,95]

sns.set_style("whitegrid")
sns.histplot(marks,bins=5)
plt.title("marks")

plt.show()
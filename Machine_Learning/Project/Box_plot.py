import seaborn as sns
df = sns.load_dataset("tips")
import matplotlib.pyplot as plt 
sns.boxplot(x="day", y="total_bill", data=df,palette="pastel",hue="day",legend=False)
plt.title("Box Plot")
plt.show()

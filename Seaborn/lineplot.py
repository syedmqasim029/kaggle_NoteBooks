import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('penguins')
plt.style.use('fivethirtyeight')
sns.lineplot(x="bill_length_mm",y='bill_depth_mm',data=data,hue="sex",style='sex',palette='Accent')
plt.show()
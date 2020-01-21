from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")



PHI_errors = [39, 10, 7, 25]
departments = ['Reception', 'Scheduling', 'Image Library', 'Stenography'] # to be used as labels
explode = [0.1, 0, 0 , 0] #emphasis on first item = reception


colors = ['#5DADE2', '#58D68D', '#CD6155', '#F7DC6F']


plt.pie(PHI_errors, labels=departments, colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, autopct='%.1f%%')
plt.title("PHI Error Pie Chart")

plt.tight_layout()
plt.show()


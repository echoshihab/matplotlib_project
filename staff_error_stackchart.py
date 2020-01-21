#this data explores PHI errors by month from different departments

from matplotlib import pyplot as plt


plt.style.use("bmh")


months = [i for i in range(1,13)]

rec_errors= [39, 41, 61, 45, 44, 51, 39, 44, 37, 32, 27, 33]
sch_errors = [27, 24, 29, 18, 21, 33, 23, 26, 18, 11, 21, 19]
il_errrors = [9, 7, 12, 9, 5, 11, 4, 9, 7, 6, 11, 11]

labels = ['Reception', 'Scheduling', 'Image Library']


plt.stackplot(months, rec_errors, sch_errors, il_errrors, labels=labels)

plt.legend()

plt.title("PHI errors by month")

plt.tight_layout()
plt.show()

import csv
import numpy as numpy
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("seaborn-deep")

with open('sampleModalityCount.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    modality_counter = Counter()

    for row in csv_reader:
        modality_counter.update(row['exams'].split(','))


prepare_lists = [list(item) for item in zip(*modality_counter.most_common(5))]

#most_common method creates a list of tuples [(modality, demand), (modality, demand)...]
#zip(*arg) separates out the (modality, demand) tuple into list of tuples of modality and demand - [(modality, modality..), (demand, demand...)]
#list comprehension creates list of modality and demands [[modality, modality..], [demand, demand..] ]

modality = (prepare_lists[0])
demand = (prepare_lists[1])

plt.barh(modality, demand)  #barh for horizotal bar

plt.title("Modality demand Jan 04, 2019")


plt.ylabel("Modality")
plt.xlabel("Demand")



plt.tight_layout()

plt.show()
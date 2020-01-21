# this file explores a csv with patientID and exam modality(s) of their visit and highlights modalities with higher demand

import csv
import numpy as numpy
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("seaborn-deep")

#with open('sampleModalityCount.csv') as csv_file:
 #   csv_reader = csv.DictReader(csv_file)

csv_data = pd.read_csv('sampleModalityCount.csv')

modality_count = csv_data['exams']

modality_counter = Counter()

for response in modality_count:
    modality_counter.update(response.split(','))


#prepare_lists = [list(item) for item in zip(*modality_counter.most_common(5))]  - removing this version for more readable version
#most_common method creates a list of tuples [(modality, demand), (modality, demand)...]
#zip(*arg) separates out the (modality, demand) tuple into list of tuples of modality and demand - [(modality, modality..), (demand, demand...)]
#list comprehension creates list of modality and demands [[modality, modality..], [demand, demand..] ]

#modality = prepare_lists[0]
#demand = prepare_lists[1]

modality = []
demand = []

for item in modality_counter.most_common(5):
    modality.append(item[0])
    demand.append(item[1])

modality.reverse()
demand.reverse()

plt.barh(modality, demand)  #barh for horizontal bar

plt.title("Modality demand Jan 04, 2019")


plt.ylabel("Modality")
plt.xlabel("Demand")



plt.tight_layout()

plt.show()
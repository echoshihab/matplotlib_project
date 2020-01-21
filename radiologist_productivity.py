from matplotlib import pyplot as plt

plt.style.use('seaborn-darkgrid')  # print(plt.style.available to see all)
# months
rad_ids = ['Ben13', 'Kel48', 'Gar92', 'How44', 'Isl99', 'Koz19', 'Kas94']

# of exams in Jan 13-20
dictated_exam_count = [1, 19, 62, 44, 293, 12, 115]
# of exams in 2019

plt.bar(rad_ids, dictated_exam_count, color='#000080')


plt.xlabel('Radiologist IDs')
plt.ylabel('# of Dictated Exams')

plt.title('Radiologist Productivity Jan 13-20, 2019')


plt.tight_layout()  # for padding

plt.show()

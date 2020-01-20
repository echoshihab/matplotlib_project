from matplotlib import pyplot as plt 

plt.style.use('seaborn-darkgrid') #print(plt.style.available to see all)
#months 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#of exams in 2018
num_of_exams_18 = [9122, 9941, 8033, 9010, 8015, 9090, 8994, 8015 , 9745, 8320, 9511, 9501]
#of exams in 2019
num_of_exams_19 = [8522, 7941, 9033, 9060, 10015, 8090, 7994, 9015 , 10745, 9320, 10511, 9521]


plt.plot(months, num_of_exams_18, color='m', linestyle='--', label='2018')
plt.plot(months, num_of_exams_19, color='k', linestyle='-', label='2019')

plt.xlabel('Months')
plt.ylabel('# of Exams')

plt.title('Exam count trend by month')

plt.legend()

plt.tight_layout() #for padding

plt.show()
from matplotlib import pyplot as plt 

#months 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#of exams in 2019
num_of_exams = [8522, 7941, 9033, 9060, 10015, 8090, 7994, 9015 , 10745, 9320, 10511, 9521]

plt.plot(months, num_of_exams)

plt.xlabel('Months')
plt.ylabel('# of Exams')

plt.title('Exam count trend by month')

plt.show()
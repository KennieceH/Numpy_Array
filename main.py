import numpy as np
"""
CAP 4784: Lab 4 – Analyzing BRFSS 
<p>
This program reads in the data from the brfss.csv file and loads it 
into a numpy array. The first five rows of the data, weight change statistics,
and the first five rows of the data with weight changes using the statistics 
class.

@author <Kenniece Harris>
@version <2/14/2023>
"""


def statistics(original_arr, new_arr, gender):
    sum_arr = (new_arr[:, 2] - new_arr[:, 3])
    sum_og_arr = (original_arr[:, 2] - original_arr[:, 3])
    weight_arr = np.column_stack((original_arr, sum_og_arr))
    mean_arr = np.sum(sum_og_arr, dtype=np.float32) / 20000
    median_arr = np.median(sum_og_arr)
    std_dev_arr = np.std(sum_og_arr)
    iqr_arr = (np.percentile(sum_og_arr, 75) - np.percentile(sum_og_arr, 25))
    if(gender == "yes"):
        print(weight_arr[0:5, :])
        print('Shape of the data: ', weight_arr.shape, '\n')
        print('Descriptive Statistics for Weight Change Data:')
        print('Mean: %.2f' % mean_arr)
        print('Median: %.1f' % median_arr)
        print('Standard Deviation: %.2f' % std_dev_arr)
        print('Interquartile Range: %.1f' % iqr_arr, '\n')

    else:
        print(new_arr)
        print('Shape of the data: ', original_arr.shape, '\n')
        print('Descriptive Statistics for Weight Change Data:')
        print('Mean: %.2f' % mean_arr)
        print('Median: %.1f' % median_arr)
        print('Standard Deviation: %.2f' % std_dev_arr)
        print('Interquartile Range: %.1f' % iqr_arr, '\n')
        print('First Five Rows of the Data with Weight Changes: ')
        print(weight_arr[0:5, :])
        print('Shape of the data: ', weight_arr.shape, '\n', '\n')


my_data = np.genfromtxt('C:\\Users\\kikic\Downloads\\brfss-cdc.csv', delimiter=',', skip_header=1)
nparray1 = my_data[0:5, :]
y = [my_data[my_data[:,5] ==k] for k in np.unique(my_data[:,5])]

print('First Five Rows of the Data:')
statistics(my_data, nparray1, "no")


print('First Five Rows of the Data relevant to Males:')
statistics(y[0], nparray1, "yes")

print('First Five Rows of the Data relevant to Females:')
statistics(y[1], nparray1, "yes")

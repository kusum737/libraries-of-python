import numpy as np


a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a.shape)



#taks 16
import numpy as np


a=np.array([[10,20,30],[40,50,60]])

print(a.shape)
print(a[0][1])


#task5
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr+10)


#task6
import numpy as np
arr=np.array([2,4,6,8])
print(arr*5)

#task7
import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr*arr)

#task8 to 10
import numpy as np
arr=np.array([80,70,90,60,85])
print("total",np.sum(arr))
print("Average",np.mean(arr))
arr=np.array([45,90,23,67,88])
print("higest",np.max(arr))
print("lowest",np.min(arr))


#task15
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)


#task 16
import numpy as np
arr=np.array([[10,20,30],
             [40,50,60]])
print(arr[0][1])
print(arr[1][2])

#task18  to 19 Real-life student marks
marks=np.array([78,85,92,67,88])
"""print("Total Marks",np.sum(marks))
print("Average Marks",np.mean(marks))
print("Highest Marks",np.min(marks))
print("Lowest Marks",np.max(marks))
print(marks+5)"""

print(marks[marks>80])

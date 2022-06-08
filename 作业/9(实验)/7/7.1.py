import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(sum(a))
for i in a:
    print(sum(i) / 3)
for i in range(len(a)):
    print(sum(a[i]) / 3)

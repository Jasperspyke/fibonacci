import numpy as np
import matplotlib.pyplot as plt

xaxis = np.array([1, 2, 3, 4, 5])
arr = np.array([5, 3, 2, 1, 0])
indexes = np.array([0, 1])

def compare_and_swap(arr, i, j):
    if arr[i] > arr[j]:
        print("swapping", arr[i], arr[j])

for i in range(10):
    barchart = plt.bar(xaxis, arr)

    def check_sorted(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        plot_and_show()
        return True

    def compare_and_swap(arr, indexes):

        i, j = indexes
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        plot_and_show(hightlighted=j)

    def plot_and_show(hightlighted=None):

        barchart = plt.bar(xaxis, arr, color='b')
        if hightlighted:
            barchart[hightlighted].set_color('r')
        plt.ylim(0, 10)
        plt.show()

while not check_sorted(arr):
    while max(indexes) < len(arr) and not check_sorted(arr):
        compare_and_swap(arr, indexes)
        indexes += 1
    indexes = np.array([0, 1])
print('done')
print(arr)


#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile("salaries.txt", dtype=int, sep="\n")
names = np.genfromtxt("names.txt", dtype='str', delimiter="\n")

x = np.arange(len(names))

plt.bar(x, salary)

plt.xticks(x, names)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")

plt.show()

print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

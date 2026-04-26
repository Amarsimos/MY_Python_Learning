import matplotlib.pyplot as plt

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

plt.scatter(
    x_values,
    y_values,
    edgecolors='none',
    c=y_values,
    cmap=plt.cm.Reds,

    s = 40)

plt.axis([0,5001,0,125000000000])

plt.title("Squares",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square",fontsize=14)

plt.tick_params(axis='both',which='major', labelsize=14)

plt.show()
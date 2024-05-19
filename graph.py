import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015]
students = {
    "Maty": [20, 30, 25, 30, 40, 50],
    "Dan": [30, 40, 35, 40, 50, 60],
    "Luke": [40, 50, 45, 50, 60, 70]
}
def graphify(x_values: list, y_values: dict, color_scheme=("blue","red","green","yellow"), legend=False):
    for student in students:
        plt.plot(years,students[student],label=student,color=color_scheme[list(students.keys()).index(student)])
    if legend: plt.legend()
    plt.savefig("output")

graphify(years,students,legend=True)

plt.show()
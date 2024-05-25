import matplotlib.pyplot as plt

data = [{'name': 'Daniel', 'points': [5, 2, 3]},
        {'name': 'Matyáš', 'points': [10, 4, 5]},
        {'name': 'Tomáš', 'points': [3, 5, 7]},
        {'name': 'Lukáš', 'points': [9, 5, 4]},
        {'name': 'Kuba', 'points': [5, 2, 8]}
        ]
names = [d['name'] for d in data]
points = [d['points'] for d in data]
disciplines = ['kliky','shyby','dřepy']

print(points)

for i in range(3):
    plt.bar(names, [p[i] for p in points], label=disciplines[i])

plt.legend()
plt.show()

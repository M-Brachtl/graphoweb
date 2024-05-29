import matplotlib.pyplot as plt
from json import loads as jloads

request_body = '[[{"name":"Daniel","points":["1","2","2"]},{"name":"Matyáš","points":["8","7","4"]},{"name":"Tomáš","points":["4","2","7"]},{"name":"Lukáš","points":["4","6","2"]},{"name":"Kuba","points":["7","5","8"]}],["Sedy-lehy","Skok daleký","Shyby"]]'
disciplines = jloads(request_body)[1]
data = jloads(request_body)[0]
names = [d['name'] for d in data]
points = [d['points'] for d in data]

widy = 0.25
# plt.cla()
for i in range(len(disciplines)):
    plt.bar([tick+widy*(i-1) for tick in (range(len(names)))], [int(p[i]) for p in points], width=widy, label=disciplines[i])

plt.xticks([t+1/(1/widy - 1)/2-0.035 for t in range(len(names))],names)
plt.legend()
plt.show()

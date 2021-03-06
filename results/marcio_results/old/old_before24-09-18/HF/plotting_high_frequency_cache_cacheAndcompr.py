import matplotlib
import matplotlib.pyplot as plt
import json


#var prepping
list = []
yValues = []
xValues = []
xController = 0

yValues2 = []
xValues2 = []
xController2 = 0


#getting data


file2 = open("Results_HF_Cache_6RemoteApps.data", "r") 
for line2 in file2: 
	j2 = json.loads(line2)
	xValues2.append(xController2)
	yValues2.append(j2['metrics'][0]['value']/j2['metrics'][0]['count'])
	xController2 = xController2 + 5



file4 = open("Results_HF_CacheAndCompression_6RemoteApps.data", "r") 
for line4 in file4: 
	j4 = json.loads(line4)
	xValues4.append(xController4)
	yValues4.append(j4['metrics'][0]['value']/j4['metrics'][0]['count'])
	xController4 = xController4 + 5


#plotting graph
fig, ax = plt.subplots()

ax.plot(xValues2, yValues2, label='Cache')

ax.plot(xValues4, yValues4, label='CacheAndCompression')
ax.legend()
ax.set(xlabel='Time (s)', ylabel='Response time (ms)', title='High-Frequency (only) cache_cache/compression Workload')
ax.grid()
fig.savefig("high_frequency_cache_cache-and-compression.png")
plt.show()

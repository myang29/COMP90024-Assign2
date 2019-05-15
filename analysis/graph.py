import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
import scipy
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator, FuncFormatter

### wrath


# prepare for data
data_dict = {}

def get_percentage(count):
    return float(count[0]/count[1])
    
with open('rate.json') as f:
    data = json.load(f)
    for line in data['rows']:
        data_dict[line['key']] = get_percentage(line['value'])

sorted_data = sorted(data_dict.items(), key=lambda kv: kv[1])
print (sorted_data)

x = []
y = []
for city,value in sorted_data:
    x.append(city)
    y.append(value)

sns.set(style="white")

# Set up the matplotlib figure
f, ax1 = plt.subplots(figsize=(7, 5))

# Generate some sequential data
x = []
y = []
for city,value in sorted_data:
    x.append(city)
    y.append(value)
print (x)
print (y)
sns.barplot(x=x, y=y, palette="OrRd", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Wrath Percentage")

# Finalize the plot
sns.despine(bottom=True)
plt.tight_layout(h_pad=2)
plt.savefig("wrath_bar.png")


### religion and wrath
plt.clf()
religion_data=defaultdict(dict)
with open('main_religions.json') as f:
    data2 = json.load(f)
    for line in data2['rows']:
        religion_data[line['key']] = line['value']

wrath = []
Total_religion = []
Christianity = []
Islam = []
Buddhism = []

for city in religion_data.keys():
    wrath.append(data_dict[city])
    Total_religion.append(religion_data[city]['Religious Total'])
    Christianity.append(religion_data[city]['Christianity'])
    Islam.append(religion_data[city]['Islam'])
    Buddhism.append(religion_data[city]['Buddhism'])

X = list(range(8))
fig, ax = plt.subplots(figsize=(10,6))
# multiple line plot
majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%s')
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)


plt.plot(X, wrath, marker='o', markersize=6,color = "r", label = "Wrath Percentage")
plt.plot(X, Total_religion,marker='v', markersize=6, label = "Total religious Percentage %f"%scipy.stats.pearsonr(wrath,Total_religion)[0])
plt.plot(X, Christianity, marker='D', markersize=6, label = "Christianity Percentage %f"%scipy.stats.pearsonr(wrath,Christianity)[0])
plt.plot(X, Islam, marker='X', markersize=6, label = "Islam Percentage %f"%scipy.stats.pearsonr(wrath,Islam)[0])
plt.plot(X, Buddhism, marker='P', markersize=6,color = '#FFDE33',label = "Buddhism Percentage %f"%scipy.stats.pearsonr(wrath,Buddhism)[0])
ax.tick_params(axis='both', which='major', labelsize= 10, pad = 10)
plt.xticks(X,x)

#plt.text(4,max(Y2)/2,'The pearson correlation is %f'%scipy.stats.pearsonr(Y1,Y2)[0],horizontalalignment='right')
# background grid setting
ax.xaxis.grid(color ='grey', linewidth=0.1, alpha=0.4) # alpha: soft color
ax.yaxis.grid(color ='grey', linewidth=0.2, alpha=0.4) # alpha: soft color
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.title("Religion VS Wrath",fontsize =18)
plt.legend(loc='best')
plt.savefig("Religion VS Wrath.png")



### volunteer and wrath
plt.clf()
volunteer_data={}
with open('volunteer.json') as f:
    data3 = json.load(f)
    for line in data3['rows']:
        volunteer_data[line['key']] = line['value']['v_rate']


volunteer = []

for city in volunteer_data.keys():
    volunteer.append(volunteer_data[city])

    
fig, ax = plt.subplots(figsize=(10,6))

majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%s')
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)
plt.plot(X, wrath, marker='o', markersize=6, label = "Wrath Percentage")
plt.plot(X, volunteer,marker='v', markersize=6, label = "Volunteer percentage%f"%scipy.stats.pearsonr(wrath,volunteer)[0])

plt.xticks(X,x)

#plt.text(4,max(Y2)/2,'The pearson correlation is %f'%scipy.stats.pearsonr(Y1,Y2)[0],horizontalalignment='right')
# background grid setting
ax.xaxis.grid(color ='grey', linewidth=0.1, alpha=0.4) # alpha: soft color
ax.yaxis.grid(color ='grey', linewidth=0.2, alpha=0.4) # alpha: soft color
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.title("Volunteer VS Wrath",fontsize =18)
plt.legend(loc='best')
plt.savefig("volunteer VS Wrath.pdf")


### grouped bar chart
plt.clf()
ind = np.arange(len(X))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10,6))

rects1 = ax.bar(ind - width/2, wrath, width,
                color='salmon', label='Wrath')
rects2 = ax.bar(ind + width/2, volunteer, width,
                color='lightskyblue', label='volunteer')

# title
plt.title("Percentage by Wrath and Volunteer",fontsize = 16,loc='center', pad=10)

# legend
# labelpad: Spacing in points between the label and the x-axis.
#plt.xlabel('X_label', labelpad=10)
plt.ylabel('percentage', labelpad=10)


# tick
ax.set_xticks(ind)
ax.set_xticklabels(x)

# legend
ax.legend()

# background grid setting
ax.xaxis.grid(color ='grey', linewidth=0.1, alpha=0.4) # alpha: soft color
ax.yaxis.grid(color ='grey', linewidth=0.2, alpha=0.4) # alpha: soft color


plt.savefig('grouped_volunteer.pdf') # save plot as png
plt.show()
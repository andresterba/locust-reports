import matplotlib.pyplot as plt
import csv
import sys
from matplotlib.ticker import MaxNLocator

x=[]
nodes=[]
pods=[]

programName = sys.argv[0]

def help():
    helpMessage = f"""
        Usage:
            {programName} csv-name startTimestamp

        Output:
            csv-name-nodes-pods-per-time.png
        """
    print(helpMessage)

def exitMessage():
    print(f"Created {filename}-nodes-pods-per-time.png")

if (len(sys.argv) != 3):
    help()
    exit

filename = sys.argv[1]
startTimestamp = sys.argv[2]

with open(f"{filename}.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)

    for row in reader:
        if (row[0] < startTimestamp):
            continue

        x.append(int(row[0]))
        nodes.append(float(row[1]))
        pods.append(float(row[2]))



start_timestamp = x[0]
for iterator, timestamp in enumerate(x):
    x[iterator] = timestamp - start_timestamp



fig, ax1 = plt.subplots()
color = 'tab:blue'
color2 = 'tab:green'
plt.xlabel('Time (s)')
plt.ylabel('Nodes', color=color)
ax1.plot(x,nodes, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 15)
ax1.legend(['Nodes'], loc=0)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Pods', color=color)
ax2.plot(x, pods, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 60)
ax2.legend(['Pods'], loc=2)
fig.tight_layout()
plt.xlim(0, max(x))
plt.grid(True)

plt.savefig(f"{filename}-nodes-pods-per-time.pdf")

exitMessage()

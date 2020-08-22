import matplotlib.pyplot as plt
import csv
import sys

x=[]
y=[]
y2=[]
user=[]

programName = sys.argv[0]

def help():
    helpMessage = f"""
        Usage:
            {programName} csv-name max-user

        Output:
            csv-name-median-per-time.png
        """
    print(helpMessage)

def exitMessage():
    print(f"Created {filename}-median-per-time.png")

if (len(sys.argv) != 3):
    help()
    exit

filename = sys.argv[1]
maxUser = sys.argv[2]

with open(f"{filename}.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)

    for row in reader:
        # Users = 0
        if (row[1] == "0"):
            continue

        if (row[2] == "0") or ("N/A" in row):
            continue

        if (row[3] != "Aggregated"):
            continue

        x.append(int(row[0]))
        y.append(float(row[13]))
        y2.append(float(row[20]))
        user.append(float(row[1]))



start_timestamp = x[0]
for iterator, timestamp in enumerate(x):
    x[iterator] = timestamp - start_timestamp



fig, ax1 = plt.subplots()

color = 'tab:blue'
color2 = 'tab:green'
plt.xlabel('Time (s)')
plt.ylabel('Latency (ms)', color=color)
ax1.plot(x,y2, color=color2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 1200)
ax1.legend(['Median'], loc=2)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('User', color=color)
ax2.plot(x, user, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, int(maxUser))
ax2.legend(['User'], loc=0)

fig.tight_layout()

plt.xlim(0, max(x))
plt.grid(True)

plt.savefig(f"{filename}-median-per-time.pdf")

exitMessage()

print(f"StartTimestamp: {start_timestamp}")

import matplotlib.pyplot as plt
import csv
import sys

x=[]
y=[]

programName = sys.argv[0]

def help():
    helpMessage = f"""
        Usage:
            {programName} csv-name

        Output:
            csv-name-rps-per-user.png
        """
    print(helpMessage)

def exitMessage():
    print(f"Created {filename}-rps-per-user.png")

if (len(sys.argv) != 2):
    help()
    exit

filename = sys.argv[1]

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

        x.append(float(row[0]))
        y.append(float(row[4]))



start_timestamp = x[0]
for iterator, timestamp in enumerate(x):
    x[iterator] = timestamp - start_timestamp



fig, ax1 = plt.subplots()
plt.plot(x,y)
plt.xlabel('Time (s)')
plt.ylabel('Latency (ms)')
plt.grid(True)
plt.xlim(0, max(x))
plt.ylim(0, max(y))

plt.savefig(f"{filename}-rps-per-user.pdf")

exitMessage()

print(f"StartTimestamp: {start_timestamp}")

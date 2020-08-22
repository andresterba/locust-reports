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
            csv-name-user-per-time.png
        """
    print(helpMessage)

def exitMessage():
    print(f"Created {filename}-user-per-time.png")

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

        if (row[2] == 0) or ("N/A" in row):
            continue

        if (row[3] != "Aggregated"):
            continue

        x.append(int(row[0]))
        y.append(float(row[1]))


start_timestamp = x[0]
for iterator, timestamp in enumerate(x):
    x[iterator] = timestamp - start_timestamp

plt.plot(x,y, marker='o')

plt.xlabel('Time (s)')
plt.ylabel('User')
plt.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
plt.xlim(0, max(x))

plt.savefig(f"{filename}-user-per-time.pdf")

exitMessage()



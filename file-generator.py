import time
import matplotlib.pyplot as plt

error = 0
success = 0

def loadFile(path):
    with open(path, "r") as file:
        for f in file:
            yield f

# Enable interactive mode
plt.ion()

# Create the figure ONCE
fig, ax = plt.subplots()
scatter = ax.scatter(success, error, color='green', s=100)
ax.set_title('Success vs Error')
ax.set_xlabel('Success')
ax.set_ylabel('Error')

for line in loadFile("log-data.txt"):
    content = line.lower()

    # small delay to simulate live stream
    time.sleep(0.1)

    if "error" in content:
        error += 1
    elif "success" in content:
        success += 1

    print(f"Success: {success}, Errors: {error}")

    # Update scatter point
    scatter.set_offsets([[success, error]])

    # Update plot
    plt.draw()
    plt.pause(0.01)   # required for live update

plt.ioff()
plt.show()

print("\nStatus....")
print(f"Total Success:{success}, Total Errors: {error}")

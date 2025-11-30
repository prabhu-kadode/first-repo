import time
import matplotlib.pyplot as plt
error = 0
success = 0

def loadFile(path):
    with open(path, "r") as file:
        for f in file:
            yield f

# For graph data over time (index is time step)
success_values = []
error_values = []

# Enable interactive mode
plt.ion()
fig, ax = plt.subplots(figsize=(8,5))

line_success, = ax.plot([], [], label="Success", color="green")
line_error, = ax.plot([], [], label="Error", color="red")

ax.set_title("Success/Error Count Over Time")
ax.set_xlabel("Time Step")
ax.set_ylabel("Count")
ax.legend()

time_step = 0

for line in loadFile("log-data.txt"):
    content = line.lower()
    # time.sleep(0.1)  # simulating streaming data

    if "error" in content:
        error += 1
    elif "success" in content:
        success += 1

    print(f"Success: {success}, Errors: {error}")

    # Append new values
    success_values.append(success)
    error_values.append(error)

    time_step += 1

    # Update line data
    line_success.set_data(range(time_step), success_values)
    line_error.set_data(range(time_step), error_values)

    # Autoscale axes
    ax.relim()
    ax.autoscale_view()

    # Refresh plot
    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.show()

print("\nStatus....")
print(f"Total Success: {success}, Total Errors: {error}")

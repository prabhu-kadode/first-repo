import time
import matplotlib.pyplot as plt

error = 0
success = 0

def loadFile(path):
    with open(path, "r") as file:
        for f in file:
            yield f

# --- Data arrays ---
success_list = []
error_list = []
time_steps = []

# --- Live dashboard setup ---
plt.ion()
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 1. Success over time
line_success, = axs[0, 0].plot([], [], color="green")
axs[0, 0].set_title("Success Over Time")
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Success Count")

# 2. Error over time
line_error, = axs[0, 1].plot([], [], color="red")
axs[0, 1].set_title("Error Over Time")
axs[0, 1].set_xlabel("Time")
axs[0, 1].set_ylabel("Error Count")

# 3. Scatter plot
scatter = axs[1, 0].scatter(success, error, color='purple')
axs[1, 0].set_title("Success vs Error")
axs[1, 0].set_xlabel("Success")
axs[1, 0].set_ylabel("Error")

# 4. Bar chart
bar_success = axs[1, 1].bar(["Success", "Error"], [success, error], color=["green", "red"])
axs[1, 1].set_title("Current Status")

plt.tight_layout()

# --- Streaming loop ---
step = 0

for line in loadFile("log-data.txt"):
    content = line.lower()
    time.sleep(0.1)

    if "error" in content:
        error += 1
    elif "success" in content:
        success += 1

    step += 1
    time_steps.append(step)
    success_list.append(success)
    error_list.append(error)

    print(f"Success:{success}, Errors:{error}")

    # --- Update Line Charts ---
    line_success.set_data(time_steps, success_list)
    line_error.set_data(time_steps, error_list)

    axs[0, 0].relim(); axs[0, 0].autoscale_view()
    axs[0, 1].relim(); axs[0, 1].autoscale_view()

    # --- Update Scatter Chart ---
    scatter.set_offsets([[success, error]])

    # --- Update Bar Chart ---
    axs[1, 1].clear()
    axs[1, 1].bar(["Success", "Error"], [success, error], color=["green", "red"])
    axs[1, 1].set_title("Current Status")

    # Refresh dashboard
    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.show()

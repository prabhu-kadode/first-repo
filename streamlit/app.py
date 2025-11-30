import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Interactive Matplotlib Dashboard")

# Sidebar controls
st.sidebar.header("Plot Controls")
num_points = st.sidebar.slider("Number of points", 10, 100, 50)
amplitude = st.sidebar.slider("Amplitude", 1, 10, 5)
frequency = st.sidebar.slider("Frequency", 0.1, 5.0, 1.0)

# Generate data
x = np.linspace(0, 10, num_points)
y = amplitude * np.sin(frequency * x)

# Display data
st.subheader("Data Table")
st.dataframe({"x": x, "y": y})

# Create Matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y, marker='o', linestyle='-', color='blue')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Interactive Sine Wave")

# Display plot
st.subheader("Matplotlib Plot")
st.pyplot(fig)

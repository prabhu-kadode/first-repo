import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample user DataFrame

df = pd.read_csv("./../users.csv")

st.title("User Data Dashboard")

# Sidebar - select plot type
plot_type = st.sidebar.selectbox(
    "Select Plot Type",
    ["Bar Chart", "Horizontal Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Histogram"]
)

# Sidebar - select numeric column (for applicable plots)
numeric_column = None
if plot_type in ["Bar Chart", "Horizontal Bar Chart", "Line Chart", "Scatter Plot", "Histogram"]:
    numeric_column = st.sidebar.selectbox("Select Numeric Column", ["age", "salary"])

# Sidebar - select x and y for scatter plot
if plot_type == "Scatter Plot":
    x_col = st.sidebar.selectbox("X-axis", ["age", "salary"])
    y_col = st.sidebar.selectbox("Y-axis", ["age", "salary"])

# Plotting
fig, ax = plt.subplots()

if plot_type == "Bar Chart":
    ax.bar(df['name'], df[numeric_column], color='skyblue')
    ax.set_xlabel("Name")
    ax.set_ylabel(numeric_column.title())
    ax.set_title(f"{numeric_column.title()} of Users")

elif plot_type == "Horizontal Bar Chart":
    ax.barh(df['name'], df[numeric_column], color='lightgreen')
    ax.set_xlabel(numeric_column.title())
    ax.set_ylabel("Name")
    ax.set_title(f"{numeric_column.title()} of Users")

elif plot_type == "Line Chart":
    ax.plot(df['name'], df[numeric_column], marker='o', linestyle='-', color='red')
    ax.set_xlabel("Name")
    ax.set_ylabel(numeric_column.title())
    ax.set_title(f"{numeric_column.title()} of Users")

elif plot_type == "Scatter Plot":
    ax.scatter(df[x_col], df[y_col], color='purple', s=100)
    ax.set_xlabel(x_col.title())
    ax.set_ylabel(y_col.title())
    ax.set_title(f"{y_col.title()} vs {x_col.title()}")

elif plot_type == "Pie Chart":
    city_counts = df['city'].value_counts()
    ax.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Users by City")

elif plot_type == "Histogram":
    ax.hist(df[numeric_column], bins=5, color='orange', edgecolor='black')
    ax.set_xlabel(numeric_column.title())
    ax.set_ylabel("Count")
    ax.set_title(f"{numeric_column.title()} Distribution")

# Show plot in Streamlit
st.pyplot(fig)

# Show DataFrame
st.subheader("User Data")
st.dataframe(df)

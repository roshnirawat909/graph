import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Employee Data Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Data Visualization")
st.write("Explore employee details, salary patterns, and department-wise insights.")

file_path = Path(__file__).parent / "employee_data.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error("employee_data.csv was not found. Upload it to the same folder as graph.py.")
    st.stop()

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(df))
col2.metric("Departments", df["Department"].nunique())
col3.metric("Average Salary", f"{df['Salary'].mean():,.2f}")

st.subheader("Dataset Information")
st.write("Missing values:")
st.dataframe(df.isnull().sum().rename("Missing Values"))

st.subheader("Statistical Summary")
st.dataframe(df.describe())

st.subheader("Average Salary by Department")
average_salary = df.groupby("Department")["Salary"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=average_salary, x="Department", y="Salary", ax=ax)
ax.set_title("Average Salary by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
plt.xticks(rotation=30)
st.pyplot(fig)

st.subheader("Salary Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Salary"], bins=5, kde=True, ax=ax)
ax.set_title("Salary Distribution")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")
st.pyplot(fig)

st.subheader("Experience vs Salary")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department",
    s=100,
    ax=ax
)
ax.set_title("Experience vs Salary")
ax.set_xlabel("Experience (Years)")
ax.set_ylabel("Salary")
st.pyplot(fig)

st.subheader("Salary Outliers")
fig, ax = plt.subplots(figsize=(6, 5))
sns.boxplot(data=df, y="Salary", ax=ax)
ax.set_title("Salary Outliers")
ax.set_ylabel("Salary")
st.pyplot(fig)

st.subheader("Correlation Matrix")
corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Correlation Matrix")
st.pyplot(fig)

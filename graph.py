
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# 1. LOAD DATASET
# ==========================================

# Find employee_data.csv in the same folder as this Python file
file_path = Path(__file__).parent / "employee_data.csv"

df = pd.read_csv(file_path)


# ==========================================
# 2. DISPLAY DATASET
# ==========================================

print("\n========== FIRST 5 ROWS ==========")
print(df.head())


# ==========================================
# 3. DATASET INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")
df.info()


# ==========================================
# 4. STATISTICAL SUMMARY
# ==========================================

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# ==========================================
# 5. CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ==========================================
# 6. CHECK DUPLICATE RECORDS
# ==========================================

print("\n========== DUPLICATE RECORDS ==========")
print(df.duplicated().sum())


# ==========================================
# 7. DEPARTMENT-WISE AVERAGE SALARY
# ==========================================

print("\n========== AVERAGE SALARY BY DEPARTMENT ==========")

average_salary = df.groupby("Department")["Salary"].mean()

print(average_salary)


# ==========================================
# 8. EMPLOYEE COUNT BY DEPARTMENT
# ==========================================

print("\n========== EMPLOYEE COUNT BY DEPARTMENT ==========")

employee_count = df["Department"].value_counts()

print(employee_count)


# ==========================================
# 9. CORRELATION
# ==========================================

print("\n========== CORRELATION MATRIX ==========")

corr = df.corr(numeric_only=True)

print(corr)


# ==========================================
# 10. BAR PLOT
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x="Department",
    y="Salary",
    data=df
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()


# ==========================================
# 11. HISTOGRAM
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Salary"],
    bins=5,
    kde=True
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()


# ==========================================
# 12. SCATTER PLOT
# ==========================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Experience",
    y="Salary",
    hue="Department",
    data=df
)

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()


# ==========================================
# 13. BOX PLOT
# ==========================================

plt.figure(figsize=(6, 5))

sns.boxplot(
    y="Salary",
    data=df
)

plt.title("Salary Outliers")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()


# ==========================================
# 14. HEATMAP
# ==========================================

plt.figure(figsize=(8, 5))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()


# ==========================================
# END
# ==========================================
5
print("\n========== ANALYSIS COMPLETED ==========")



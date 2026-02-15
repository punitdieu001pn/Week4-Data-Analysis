import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

print("Available Columns:")
print(df.columns)

# -----------------------------
# TOTAL SALES
# -----------------------------
total_sales = df["Total_Sales"].sum()
print("\nTotal Sales:", total_sales)

# -----------------------------
# SALES BY REGION (BAR CHART)
# -----------------------------
sales_by_region = df.groupby("Region")["Total_Sales"].sum()
print("\nSales by Region:")
print(sales_by_region)

plt.figure()
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/bar_chart.png")
plt.show()

# -----------------------------
# MONTHLY SALES TREND (LINE CHART)
# -----------------------------
# Convert Date column to datetime
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract month number and name
df["Month_Number"] = df["Date"].dt.month
df["Month"] = df["Date"].dt.month_name()

# Group and sort by month number
monthly_sales = df.groupby(["Month_Number", "Month"])["Total_Sales"].sum().reset_index()
monthly_sales = monthly_sales.sort_values("Month_Number")

plt.figure()
plt.plot(monthly_sales["Month"], monthly_sales["Total_Sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/line_chart.png")
plt.show()


print("\nProject Completed Successfully ✅")






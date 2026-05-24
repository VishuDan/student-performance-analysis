import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Vikas"],
    "Math": [85, 78, 92, 88, 76],
    "Science": [90, 74, 89, 95, 80],
    "English": [88, 82, 91, 87, 79]
}

df = pd.DataFrame(data)

# Calculate Average
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Find Topper
topper = df.loc[df["Average"].idxmax()]

print("Top Performer:")
print(topper)

# Plot Average Marks
plt.figure()
plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.show()
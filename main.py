import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from excel
df = pd.read_excel(r"C:\Users\UTTAM SINGH\OneDrive\Documents\four_probe_data.xlsx")

print("Data Loaded:\n", df)

# Input constants
current = float(input("Enter current: "))
s = float(input("Enter probe distance: "))
error = float(input("Enter error value: "))

# Calculations
df["tempK"] = df["tempC"] + 273
df["resistance"] = ((df["vcool"] + df["vheat"]) / 2) / current
df["sample_resistivity"] = df["resistance"] * 2 * np.pi * s
df["resistivity"] = df["sample_resistivity"] / error
df["t_inverse"] = (1 / df["tempK"]) * 1000
df["log10p"] = np.log10(df["resistivity"])

# Save output
df.to_excel(r"C:\Users\UTTAM SINGH\OneDrive\Documents\output.xlsx", index=False)

print("\nProcessed Data:\n", df)

# Plot graph
plt.plot(df["t_inverse"], df["log10p"], marker="o")
plt.xlabel("1/T * 1000")
plt.ylabel("log10(resistivity)")
plt.title("Four Probe Method Graph")
plt.gca().set_facecolor("lightblue")
plt.grid()

# To find slope of line
slope, intercept = np.polyfit(df["t_inverse"], df["log10p"], 1)
print("Slope:", slope)

# Save image
plt.savefig(r"C:\Users\UTTAM SINGH\OneDrive\Pictures\Screenshots\graph.png")


print("hello")
eg = 0.3960 * slope
print("Energy gap is :" ,eg)

# Save image
plt.savefig(r"C:\Users\UTTAM SINGH\OneDrive\Pictures\Screenshots\graph.png")
plt.show()

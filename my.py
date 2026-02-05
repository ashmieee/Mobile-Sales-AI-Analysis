import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Data Load Karein
try:
    df = pd.read_csv("Sales.csv")
    print("--- Data Loaded Successfully! ---")
except FileNotFoundError:
    print("Error: Sales.csv file nahi mili. Check karein ki file sahi folder mein hai.")

# 2. Data Cleaning (Khali values ko bharna)
# Rating aur Memory mein kuch cells khali ho sakte hain
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
df['Selling Price'] = df['Selling Price'].fillna(0)

# 3. Basic Analysis (Top 5 Brands by Average Price)
brand_analysis = df.groupby('Brands')['Selling Price'].mean().sort_values(ascending=False).head(5)
print("\n--- Top 5 Brands by Avg Selling Price ---")
print(brand_analysis)

# 4. Simple Machine Learning (Predicting Selling Price)
# Hum Rating aur Discount ke aadhar par Price predict karenge
X = df[['Rating', 'Discount']] # Input Features
y = df['Selling Price']        # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Ek dummy prediction: Agar Rating 4.5 ho aur Discount 2000 ho toh price kya hoga?
sample_pred = model.predict([[4.5, 2000]])
print(f"\nPredicted Selling Price for 4.5 Rating & 2000 Discount: {sample_pred[0]:.2f}")

# 5. Visualization (Save for PowerBI/Report)
plt.figure(figsize=(10, 6))
sns.barplot(x=brand_analysis.index, y=brand_analysis.values)
plt.title("Top 5 Expensive Brands")
plt.ylabel("Average Selling Price")
plt.savefig("brand_report.png") # Graph save ho jayega
print("\nGraph saved as 'brand_report.png'")

# Cleaned data ko save karein PowerBI ke liye
df.to_csv("Cleaned_Mobile_Sales.csv", index=False)
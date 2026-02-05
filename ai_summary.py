import pandas as pd
from google import genai

# 1. Setup - v1 version ke sath
client = genai.Client(
    api_key="AIzaSyAl5V9cHHC5j_K69bl6sNhYpaEYSddEmSM",
    http_options={'api_version': 'v1'}
)

# 2. Data Load
try:
    df = pd.read_csv("Cleaned_Mobile_Sales.csv")
    top_brand = df.groupby('Brands')['Discount'].mean().idxmax()
    avg_price = df['Selling Price'].mean()
except Exception as e:
    print(f"Data load error: {e}")

# 3. AI Summary Generate Karein (Latest Model ke sath)
try:
    prompt = f"""
    I have mobile sales data.
    The brand giving the highest average discount is {top_brand}.
    The average selling price is {avg_price:.2f}.
    Write a 3-line professional business summary in Hinglish about this.
    """

    # Aapki list ke hisaab se naya model name:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash", # <--- Naya Model Name yahan badla hai
        contents=prompt
    )

    print("\n--- AI Business Insights ---")
    if response.text:
        print(response.text)
    else:
        print("AI ne response toh diya par text khali hai.")

except Exception as e:
    print("\n--- Final Error Log ---")
    print(f"Abhi bhi masla hai: {e}")
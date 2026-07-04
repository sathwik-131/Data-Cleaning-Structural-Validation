import pandas as pd
import numpy as np


df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df.head())


print("\nMissing Values:")
print(df.isnull().sum())


numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())


text_cols = df.select_dtypes(include='object').columns
df[text_cols] = df[text_cols].fillna("Unknown")


df = df.drop_duplicates()


for col in text_cols:
    df[col] = df[col].str.strip()
    df[col] = df[col].str.lower()

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')


if "Age" in df.columns:
    df = df[df["Age"] > 0]


df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaned successfully!")
# 🧹 Data Cleaning & Structural Validation

A Python-based data preprocessing project that demonstrates common techniques for cleaning, validating, and standardizing structured datasets before analysis or machine learning.

The project uses **Pandas and NumPy** to identify data-quality issues and produce a cleaner dataset.

---

## 📌 Project Overview

Real-world datasets frequently contain:

* Missing values
* Duplicate records
* Inconsistent text formatting
* Invalid numerical values
* Incorrect date formats
* Incomplete categorical fields

This project demonstrates a basic preprocessing pipeline to address these issues before downstream analysis.

---

## 🔄 Data Cleaning Pipeline

```text
Raw Dataset
     ↓
Load CSV
     ↓
Inspect Data
     ↓
Check Missing Values
     ↓
Handle Missing Values
     ↓
Remove Duplicates
     ↓
Standardize Text
     ↓
Convert Dates
     ↓
Validate Age
     ↓
Clean Dataset
     ↓
Export CSV
```

---

## 🧹 Cleaning Operations

### Missing Numerical Values

Numerical columns are identified automatically and missing values are replaced using the column mean.

### Missing Text Values

Missing categorical/text values are replaced with:

```text
Unknown
```

### Duplicate Removal

Duplicate records are removed using Pandas.

### Text Standardization

Text fields are:

* Stripped of unnecessary whitespace
* Converted to lowercase

### Date Conversion

If a `Date` column exists, it is converted using:

```python
pd.to_datetime()
```

Invalid date values are coerced to missing values.

### Age Validation

If an `Age` column exists, records with:

```text
Age <= 0
```

are removed.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* CSV

---

## 📂 Project Structure

```text
Data-Cleaning-Structural-Validation/
│
├── data_cleaning.py
├── raw_data.csv
├── cleaned_data.csv
└── README.md
```

---

## 🚀 Getting Started

### Clone

```bash
git clone https://github.com/sathwik-131/Data-Cleaning-Structural-Validation.git
cd Data-Cleaning-Structural-Validation
```

### Install dependencies

```bash
pip install pandas numpy
```

### Run

```bash
python data_cleaning.py
```

The cleaned dataset is saved as:

```text
cleaned_data.csv
```

---

## 🧠 Skills Demonstrated

* Data preprocessing
* Missing-value handling
* Duplicate detection/removal
* Text normalization
* Date conversion
* Basic data validation
* Pandas DataFrame operations
* NumPy-based column selection
* CSV input/output

---

## 🔮 Future Improvements

The preprocessing pipeline could be extended with:

* Outlier detection
* IQR-based validation
* Schema validation
* Data-type validation
* Range checks
* Referential integrity checks
* Automated data-quality reports
* Great Expectations / Pandera integration
* Reusable preprocessing functions
* Unit tests

---

## 📌 Why Data Cleaning Matters

Clean and structurally valid data is an important prerequisite for reliable analytics and machine-learning workflows.

This project demonstrates the preprocessing stage that can occur before exploratory data analysis, feature engineering, and model training.

---

## 👨‍💻 Author

**Sathwik B**

B.Tech — Computer Science & Machine Learning

GitHub: [@sathwik-131](https://github.com/sathwik-131)

---

## 📌 Project Status

**Completed — Foundational Data Preprocessing Project**

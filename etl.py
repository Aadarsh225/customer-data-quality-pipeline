import pandas as pd
import re

# Extract
df = pd.read_csv("data/transactions.csv")

print("Original Shape:", df.shape)

# --------------------
# Transform
# --------------------

# Remove duplicates
df = df.drop_duplicates(subset=["transaction_id"])

# Fill missing customer_id
df["customer_id"] = df["customer_id"].fillna("UNKNOWN")

# Fill missing customer_name
df["customer_name"] = df["customer_name"].fillna("Unknown User")

# Fix amount (make positive)
df["amount"] = df["amount"].abs()

# Standardize device_type
df["device_type"] = df["device_type"].str.lower().fillna("unknown")

# Standardize payment methods
df["payment_method"] = df["payment_method"].replace({
    "Cheque": "Cash"
})

# Parse dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Fraud flag
df["fraud_flag"] = df["login_attempts"] > 3

# Email validation
def valid_email(email):
    if pd.isna(email):
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, str(email)))

df["valid_email"] = df["email"].apply(valid_email)

# Phone validation
df["valid_phone"] = df["phone_number"].astype(str).str.len() == 10

# Fill city
df["city"] = df["city"].replace("", "Unknown").fillna("Unknown")

# --------------------
# Load
# --------------------
df.to_csv("output/clean_transactions.csv", index=False)

print("Cleaned Shape:", df.shape)
print(df.head())
print("Saved to output/clean_transactions.csv")
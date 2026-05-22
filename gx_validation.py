import great_expectations as gx
import pandas as pd 

df=pd.read_csv("output/clean_transactions.csv")

print("Loaded Data")

print(df.head())

# Create context
context = gx.get_context()

# -----------------------------
# Data Source
# -----------------------------
data_source = context.data_sources.add_pandas(name="my_pandas_source")

# -----------------------------
# Data Asset (CSV file)
# -----------------------------
data_asset = data_source.add_csv_asset(
    name="transactions_asset",
    filepath_or_buffer="output/clean_transactions.csv"
)

# -----------------------------
# Batch Definition
# -----------------------------
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    "transactions_batch"
)

# Get batch
batch = batch_definition.get_batch()

# -----------------------------
# Expectation Suite
# -----------------------------
suite = gx.ExpectationSuite(name="transactions_suite")

# Get Validator
validator = context.get_validator(
    batch=batch,
    expectation_suite=suite
)

# -----------------------------
# Expectations
# -----------------------------
validator.expect_column_values_to_be_unique("transaction_id")

validator.expect_column_values_to_not_be_null("customer_id")

validator.expect_column_values_to_be_between(
    "amount",
    min_value=0,
    max_value=100000
)

validator.expect_column_values_to_be_in_set(
    "payment_method",
    ["UPI", "Card", "Cash", "NetBanking"]
)

validator.expect_column_values_to_be_between(
    "login_attempts",
    min_value=0,
    max_value=10
)

validator.expect_column_values_to_not_be_null("city")

validator.expect_column_values_to_be_in_set(
    "fraud_flag",
    [True, False]
)

validator.expect_table_row_count_to_be_between(
    min_value=90,
    max_value=100
)

## Validation the phone number
validator.expect_column_values_to_be_between(
    "phone_number",
    min_value=10,
    max_value=10
)

# customer_name not null
validator.expect_column_values_to_not_be_null(
    "customer_name"
)

# email format check
validator.expect_column_values_to_match_regex(
    "email",
    r"^[\w\.-]+@[\w\.-]+\.\w+$"
)

# phone number = 10 digits
validator.expect_column_values_to_match_regex(
    "phone_number",
    r"^\d{10}$"
)

# transaction_status allowed
validator.expect_column_values_to_be_in_set(
    "transaction_status",
    ["Success", "Failed", "Pending", "Done", "Unknown"]
)

# device_type allowed
validator.expect_column_values_to_be_in_set(
    "device_type",
    ["mobile", "desktop", "tablet", "unknown"]
)

# transaction_id not null
validator.expect_column_values_to_not_be_null(
    "transaction_id"
)

# customer_id pattern
validator.expect_column_values_to_match_regex(
    "customer_id",
    r"^C\d{3}$|^UNKNOWN$"
)

# email should not be null
validator.expect_column_values_to_not_be_null(
    "email"
)

# amount mean sanity check
validator.expect_column_mean_to_be_between(
    "amount",
    min_value=0,
    max_value=50000
)

# amount not null
validator.expect_column_values_to_not_be_null(
    "amount"
)

# login_attempts not null
validator.expect_column_values_to_not_be_null(
    "login_attempts"
)

# city should not be blank
validator.expect_column_values_to_not_match_regex(
    "city",
    r"^\s*$"
)

# transaction_date not null
validator.expect_column_values_to_not_be_null(
    "transaction_date"
)

# -----------------------------
# Run Validation
# -----------------------------
results = validator.validate()

print(results) 
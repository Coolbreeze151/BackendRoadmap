import pandera as pa
from pandera import Column, DataFrameSchema
import pandas as pd
import os

# Define the schema
schema = DataFrameSchema({
    "vendor_id": Column(pa.Int),
    "pickup_datetime": Column(pa.DateTime),
    "dropoff_datetime": Column(pa.DateTime),
    "passenger_count": Column(pa.Int),
    "trip_distance": Column(pa.Float),
    "rate_code_id": Column(pa.Int),
    "store_and_fwd_flag": Column(pa.String),
    "pickup_location_id": Column(pa.Int),
    "dropoff_location_id": Column(pa.Int),
    "payment_type": Column(pa.Int),
    "fare_amount": Column(pa.Float),
    "extra": Column(pa.Float),
    "mta_tax": Column(pa.Float),
    "tip_amount": Column(pa.Float),
    "tolls_amount": Column(pa.Float),
    "improvement_surcharge": Column(pa.Float),
    "total_amount": Column(pa.Float),
    "congestion_surcharge": Column(pa.Float, nullable=True)
})

# Function to validate a CSV file
def validate_csv(file_path):
    df = pd.read_csv(file_path, parse_dates=["pickup_datetime", "dropoff_datetime"])
    validated_df = schema.validate(df)
    print(f"{file_path} is valid.")
    print(validated_df.head())

# Main function to validate all CSV files in the data directory
def main():
    data_dir = "data"
    for file_name in os.listdir(data_dir):
        if file_name.endswith(".csv"):
            file_path = os.path.join(data_dir, file_name)
            validate_csv(file_path)

if __name__ == "__main__":
    main()
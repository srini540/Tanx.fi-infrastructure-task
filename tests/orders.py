import pandas as pd
import os

def compute_revenue(filename):
   
    # Load the CSV file
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        raise SystemExit

    # Check if necessary columns exist
    necessary_columns = ['order_date', 'product_price', 'quantity', 'product_name', 'customer_id']
    for column in necessary_columns:
        if column not in df.columns:
            print(f"The following column is not present: {column}")
            raise SystemExit

    # Check for missing data
    if df.isnull().values.any():
        missing_data_rows = df[df.isnull().any(axis=1)]
        for index, row in missing_data_rows.iterrows():
            print(f"Data in the row {index} is missing. Please check, either delete the row or add the data and continue.")
        raise SystemExit

    # Convert 'order_date' to datetime format
    try:
        df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')
    except ValueError:
        print("Dates are not present in the format as specified in code. Please change them accordingly.")
        raise SystemExit

    # Compute total revenue for each month
    monthly_revenue = df.groupby(df['order_date'].dt.to_period('M')).apply(lambda x: (x['product_price'] * x['quantity']).sum())
    monthly_revenue.reset_index(name='Monthly Revenue').to_csv('/data/monthly_revenue.csv', index=False)

    # Compute total revenue for each product
    product_revenue = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    product_revenue.reset_index(name='Product Revenue').to_csv('/data/product_revenue.csv', index=False)

    # Compute total revenue for each customer
    customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    customer_revenue.reset_index(name='Customer Revenue').to_csv('/data/customer_revenue.csv', index=False)

    # Identify top 10 customers by revenue
    top_customers = customer_revenue.nlargest(10)
    top_customers.reset_index(name='Top Customers Revenue').to_csv('/data/top_customers.csv', index=False)

if __name__ == "__main__":
    compute_revenue()

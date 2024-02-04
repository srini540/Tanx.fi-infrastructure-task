import pandas as pd

def compute_revenue():
    # Load the CSV file
    try:
        df = pd.read_csv('Orders.csv')
    except FileNotFoundError:
        print("The file 'coffeesales' does not exist.")
        return

    # Convert 'order_date' to datetime format
    df['order_date'] = pd.to_datetime(df['order_date'],format='%d-%m-%Y')

    # Compute total revenue for each month
    monthly_revenue = df.groupby(df['order_date'].dt.to_period('M')).apply(lambda x: (x['product_price'] * x['quantity']).sum())

    # Compute total revenue for each product
    product_revenue = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())

    # Compute total revenue for each customer
    customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())

    # Identify top 10 customers by revenue
    top_customers = customer_revenue.nlargest(10)

    # Print the results
    print("Monthly Revenue:\n", monthly_revenue)
    print("\nProduct Revenue:\n", product_revenue)
    print("\nCustomer Revenue:\n", customer_revenue)
    print("\nTop 10 Customers:\n", top_customers)

if __name__ == "__main__":
    compute_revenue()
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px

# # Load the dataset
# @st.cache_data
# def load_data():
#     data_path = 'US_Regional_Sales_Data.xlsx'
#     return pd.read_excel(data_path)

# # Helper function for missing values
# def display_missing_values(data):
#     st.subheader("Missing Values Check")
#     missing = data.isnull().sum()
#     if missing.sum() == 0:
#         st.write("No missing values in the dataset.")
#     else:
#         st.write(missing[missing > 0])

# # Helper function for descriptive statistics
# def descriptive_stats(data):
#     st.subheader("Descriptive Statistics")
#     st.write(data.describe())

# # Plot sales trends over time
# def plot_sales_trends(data):
#     st.subheader("Sales Trends Over Time")
#     # Ensure the sales date is in datetime format
#     data['OrderDate'] = pd.to_datetime(data['OrderDate'], errors='coerce')
#     # Drop rows where the 'OrderDate' is NaT
#     data = data.dropna(subset=['OrderDate'])
    
#     # Plot revenue trends across sales channels
#     data['Revenue'] = data['Order Quantity'] * data['Unit Price']
#     fig = px.line(data, x='OrderDate', y='Revenue', color='Sales Channel', title="Revenue Trends Over Time")
#     st.plotly_chart(fig)

# # Plot sales channel performance using boxplots
# def plot_sales_channel_performance(data):
#     st.subheader("Sales Channel Performance")
#     data['Revenue'] = data['Order Quantity'] * data['Unit Price']
#     fig = plt.figure(figsize=(10, 5))
#     sns.boxplot(x='Sales Channel', y='Revenue', data=data)
#     st.pyplot(fig)

# # Product performance bar plot
# def product_performance(data):
#     st.subheader("Product Performance")
#     data['Revenue'] = data['Order Quantity'] * data['Unit Price']
#     product_summary = data.groupby('_ProductID')['Revenue'].sum().reset_index()
#     fig = px.bar(product_summary, x='_ProductID', y='Revenue', title="Revenue by Product ID")
#     st.plotly_chart(fig)

# # Profitability analysis
# def plot_profit_margin(data):
#     st.subheader("Profit Margin Analysis")
#     data['Profit Margin'] = (data['Unit Price'] - data['Unit Cost']) / data['Unit Price'] * 100
#     fig = plt.figure(figsize=(10, 5))
#     sns.boxplot(x='Sales Channel', y='Profit Margin', data=data)
#     st.pyplot(fig)

# # Main Streamlit Layout
# def main():
#     # Page selection
#     st.sidebar.title("US Regional Sales Analysis")
#     page = st.sidebar.radio("Go to", ["Overview", "Data Exploration", "Sales Trends", "Sales Channel Analysis", "Product Performance", "Profitability Analysis"])
    
#     # Load the data
#     data = load_data()

#     # Page 1: Overview
#     if page == "Overview":
#         st.title("US Regional Sales Data Analysis")
#         st.write("""
#         This Streamlit app provides a comprehensive analysis of the US Regional Sales Data. 
#         You can explore the data, identify trends, and visualize performance across sales channels and product performance.
#         """)
#         st.subheader("Dataset Overview")
#         st.write(data.head())  # Show first few rows of the dataset
#         st.write(f"Total Rows: {data.shape[0]}")
#         st.write(f"Total Columns: {data.shape[1]}")

#     # Page 2: Data Exploration
#     elif page == "Data Exploration":
#         st.title("Data Exploration")
#         st.write("This section includes initial exploration of the dataset.")
#         display_missing_values(data)
#         descriptive_stats(data)

#     # Page 3: Sales Trends
#     elif page == "Sales Trends":
#         st.title("Sales Trends")
#         st.write("Analyze sales trends over time.")
#         plot_sales_trends(data)

#     # Page 4: Sales Channel Analysis
#     elif page == "Sales Channel Analysis":
#         st.title("Sales Channel Analysis")
#         st.write("Compare sales performance across different sales channels.")
#         plot_sales_channel_performance(data)

#     # Page 5: Product Performance
#     elif page == "Product Performance":
#         st.title("Product Performance")
#         st.write("Evaluate the performance of different products based on revenue.")
#         product_performance(data)

#     # Page 6: Profitability Analysis
#     elif page == "Profitability Analysis":
#         st.title("Profitability Analysis")
#         st.write("Analyze profit margins across different sales channels.")
#         plot_profit_margin(data)

# if __name__ == "__main__":
#     main()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    data_path = 'datasheet.xlsx'
    sales_orders_df = pd.read_excel(data_path, sheet_name='Sales Orders Sheet')
    products_df = pd.read_excel(data_path, sheet_name='Products Sheet')
    regions_df = pd.read_excel(data_path, sheet_name='Regions Sheet')
    store_locations_df = pd.read_excel(data_path, sheet_name='Store Locations Sheet')
    
    # Merge relevant dataframes
    merged_df = pd.merge(sales_orders_df, products_df, left_on='_ProductID', right_on='_ProductID')
    merged_df = pd.merge(merged_df, store_locations_df, on='_StoreID')
    merged_df = pd.merge(merged_df, regions_df, on='StateCode')

    return merged_df

# Helper function for missing values
def display_missing_values(data):
    st.subheader("Missing Values Check")
    missing = data.isnull().sum()
    if missing.sum() == 0:
        st.write("No missing values in the dataset.")
    else:
        st.write(missing[missing > 0])

# Helper function for descriptive statistics
def descriptive_stats(data):
    st.subheader("Descriptive Statistics")
    st.write(data.describe())

# Plot sales trends over time
def plot_sales_trends(data):
    st.subheader("Sales Trends Over Time")
    # Ensure the sales date is in datetime format
    data['OrderDate'] = pd.to_datetime(data['OrderDate'], errors='coerce')
    # Drop rows where the 'OrderDate' is NaT
    data = data.dropna(subset=['OrderDate'])
    
    # Add filters for year and sales channel
    year_options = data['OrderDate'].dt.year.unique()
    selected_year = st.sidebar.selectbox("Select Year", year_options)
    
    channel_options = data['Sales Channel'].unique()
    selected_channels = st.sidebar.multiselect("Select Sales Channels", channel_options, default=channel_options)
    
    # Filter data based on selection
    filtered_data = data[(data['OrderDate'].dt.year == selected_year) & (data['Sales Channel'].isin(selected_channels))]

    # Plot revenue trends
    filtered_data['Revenue'] = filtered_data['Order Quantity'] * filtered_data['Unit Price']
    fig = px.line(filtered_data, x='OrderDate', y='Revenue', color='Sales Channel', title="Revenue Trends Over Time")
    st.plotly_chart(fig)

# Plot sales channel performance using boxplots
def plot_sales_channel_performance(data):
    st.subheader("Sales Channel Performance")
    data['Revenue'] = data['Order Quantity'] * data['Unit Price']
    fig = plt.figure(figsize=(10, 5))
    sns.boxplot(x='Sales Channel', y='Revenue', data=data)
    plt.title("Revenue Distribution by Sales Channel")
    st.pyplot(fig)

# Product performance bar plot
def product_performance(data):
    st.subheader("Product Performance")

    data['Revenue'] = data['Order Quantity'] * data['Unit Price']
    product_summary = data.groupby('Product Name')['Revenue'].sum().reset_index()

    # Add filter for top N products
    top_n = st.sidebar.slider("Select Top N Products", 1, 20, 10)
    top_products = product_summary.nlargest(top_n, 'Revenue')

    fig = px.bar(top_products, x='Product Name', y='Revenue', title=f"Top {top_n} Products by Revenue")
    st.plotly_chart(fig)

# Profitability analysis
def plot_profit_margin(data):
    st.subheader("Profit Margin Analysis")
    data['Profit Margin'] = ((data['Unit Price'] - data['Unit Cost']) / data['Unit Price']) * 100
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='Sales Channel', y='Profit Margin', data=data, ax=ax)
    plt.title("Profit Margin Distribution by Sales Channel")
    st.pyplot(fig)

# Main Streamlit Layout
def main():
    # Page selection
    st.sidebar.title("US Regional Sales Analysis")
    page = st.sidebar.radio("Go to", ["Overview", "Data Exploration", "Sales Trends", "Sales Channel Analysis", "Product Performance", "Profitability Analysis"])

    # Load the data
    data = load_data()

    # Page 1: Overview
    if page == "Overview":
        st.title("US Regional Sales Data Analysis")
        st.write("""
        This Streamlit app provides a comprehensive analysis of the US Regional Sales Data. 
        You can explore the data, identify trends, and visualize performance across sales channels and product performance.
        """)
        st.subheader("Dataset Overview")
        st.write(data.head())  # Show first few rows of the dataset
        st.write(f"Total Rows: {data.shape[0]}")
        st.write(f"Total Columns: {data.shape[1]}")

    # Page 2: Data Exploration
    elif page == "Data Exploration":
        st.title("Data Exploration")
        st.write("This section includes initial exploration of the dataset.")
        display_missing_values(data)
        descriptive_stats(data)

    # Page 3: Sales Trends
    elif page == "Sales Trends":
        st.title("Sales Trends")
        st.write("Analyze sales trends over time.")
        plot_sales_trends(data)

    # Page 4: Sales Channel Analysis
    elif page == "Sales Channel Analysis":
        st.title("Sales Channel Analysis")
        st.write("Compare sales performance across different sales channels.")
        plot_sales_channel_performance(data)

    # Page 5: Product Performance
    elif page == "Product Performance":
        st.title("Product Performance")
        st.write("Evaluate the performance of different products based on revenue.")
        product_performance(data)

    # Page 6: Profitability Analysis
    elif page == "Profitability Analysis":
        st.title("Profitability Analysis")
        st.write("Analyze profit margins across different sales channels.")
        plot_profit_margin(data)

if __name__ == "__main__":
    main()
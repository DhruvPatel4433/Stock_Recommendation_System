import streamlit as st
import pandas as pd
import numpy as np
import re
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Function to clean stock data
def clean_stock_data(file_path):
    stock_info = pd.read_excel(file_path)
    stock = stock_info.iloc[:, :26]

    # Function to remove special characters from column names
    def remove_char(string):
        return re.sub('[^A-Za-z0-9]+', '', string)

    # Clean column names
    stock.columns = [remove_char(column) for column in stock.columns]

    # Drop the 'Government' column if it exists
    if 'Government' in stock.columns:
        stock.drop(columns='Government', inplace=True)

    # Function to clean numeric columns
    def clean_numeric(value):
        value = re.sub(r'[^\d.]', '', str(value)).strip('.')
        return float(value) if value else np.nan

    # Clean specific columns
    stock['BookValue'] = stock['BookValue'].str.replace('₹', '', regex=False).str.replace('Cr.', '', regex=False).apply(clean_numeric)
    stock['MarketCap'] = stock['MarketCap'].str.replace('₹', '', regex=False).str.replace('Cr.', '', regex=False).apply(clean_numeric)
    columns_to_convert = ['StockPE', 'BookValue', 'DividendYield', 'ROE', 'MarketCap']
    for column in columns_to_convert:
        stock[column] = stock[column].astype(str).apply(clean_numeric)

    # Drop rows with missing values in specific columns
    stock.dropna(subset=['FIIs', 'DIIs', 'StockPE', 'OPM', 'OperatingProfit', 'Promoters', 'EPSinRs', 'ROE', 'BookValue'], inplace=True)
    
    return stock

# Example usage
file_path = r'C:/Dhruv/Streamlit_Dashboard/Stokc_clustering/stock_info.xlsx'
cleaned_stock_data = clean_stock_data(file_path)

data = cleaned_stock_data[['StockPE', 'BookValue', 'DividendYield', 'ROE', 'MarketCap']]

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Clustering
optimal_k = 10
kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(scaled_data)
labels = kmeans.labels_
cleaned_stock_data['Cluster'] = labels

# Function to find similar stocks
def find_similar_stocks(stock_name, stock_df):
    if stock_name not in stock_df['Ticker'].values:
        return []
    stock_cluster = stock_df[stock_df['Ticker'] == stock_name]['Cluster'].values[0]
    similar_stocks = stock_df[stock_df['Cluster'] == stock_cluster]['Ticker'].tolist()
    if stock_name in similar_stocks:
        similar_stocks.remove(stock_name)  # Remove the stock itself from similar stocks list
    return similar_stocks

# Function to find the closest stock based on distance
def find_closest_stock(stock_name, stock_df, scaled_data):
    if stock_name not in stock_df['Ticker'].values:
        return None
    stock_cluster = stock_df[stock_df['Ticker'] == stock_name]['Cluster'].values[0]
    stock_index = stock_df[stock_df['Ticker'] == stock_name].index[0]
    cluster_indices = stock_df[stock_df['Cluster'] == stock_cluster].index
    cluster_data = scaled_data[cluster_indices]
    distances = np.linalg.norm(cluster_data - scaled_data[stock_index], axis=1)
    closest_index = cluster_indices[np.argpartition(distances, 1)[1]]  # Find the second closest (the first one will be itself)
    return stock_df.loc[closest_index, 'Ticker']

# Streamlit UI
st.title("Stock Clustering and Recommendation App")

new_list = cleaned_stock_data['Ticker'].tolist()
result = st.selectbox('Select a Stock', new_list)

nearest_stock = find_closest_stock(result, cleaned_stock_data, scaled_data)
if nearest_stock:
    st.write(f"The closest stock to {result} is {nearest_stock}")
    nearest_stock_data = cleaned_stock_data[cleaned_stock_data['Ticker'] == nearest_stock].T
    st.write("Details of the closest stock:")
    st.dataframe(nearest_stock_data)
else:
    st.write(f"Stock '{result}' not found in the dataset.")

similar_stocks_st = find_similar_stocks(result, cleaned_stock_data)
if similar_stocks_st:
    similar_stocks_data = cleaned_stock_data[cleaned_stock_data['Ticker'].isin(similar_stocks_st)].T
    st.write("Similar stocks in the same cluster:")
    st.dataframe(similar_stocks_data)
else:
    st.write("No similar stocks found.")

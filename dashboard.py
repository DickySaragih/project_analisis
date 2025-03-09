import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
category_counts = pd.read_csv("category_counts.csv")
payment_totals = pd.read_csv("payment_totals.csv")

# Streamlit App
st.set_page_config(page_title="E-Commerce Data Dashboard", layout="wide")
st.title("📊 E-Commerce Data Analysis Dashboard")

# Sidebar Navigation
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to", ["Top Categories", "Payment Analysis"])

if option == "Top Categories":
    st.header("🛒 Top 10 Most Ordered Product Categories")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=category_counts['product_category_name'][:10], y=category_counts['order_count'][:10], palette='viridis', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Number of Orders")
    ax.set_title("Top 10 Most Ordered Product Categories")
    st.pyplot(fig)
    st.dataframe(category_counts.head(10))
    
elif option == "Payment Analysis":
    st.header("💳 Payment Method Analysis")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='payment_type', y='payment_value', data=payment_totals, palette='coolwarm', ax=ax)
    ax.set_xlabel("Payment Method")
    ax.set_ylabel("Total Transaction Value")
    ax.set_title("Total Transaction Value by Payment Method")
    st.pyplot(fig)
    st.dataframe(payment_totals)

st.sidebar.text("🚀 Powered by Streamlit")

from prophet import Prophet
from prophet.plot import plot_plotly as prophet_plot

import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Ensure environment encoding
os.environ['PYTHONUTF8'] = '1'

# Set page title and theme
st.set_page_config(page_title="Startup Ecosystem Dashboard", layout="wide")
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background: #121212;
        }
        .css-18e3th9 {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #333;
            color: white;
            border-radius: 10px;
        }
        .stDataFrame {
            background-color: #1e1e1e;
        }
        h1 {
            text-align: center;
            color: #60fc37 !important;
            font-size: 3rem;
            font-weight: 900;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.2);
        }
        h2, h3, h4 ,h5 {
            color: #ffffff !important;
            font-weight: 700;
            text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.2);
        }
        .filter-container {
            background: #1e1e1e;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .stSelectbox {
            color: white; /* Adjusted selectbox text color */
        }
        .stSelectbox > label {
            color: white; /* Adjusted selectbox label color */
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown("""
    <h1>🚀 Startup Ecosystem Dashboard</h1>
    <h4 style='text-align: center; color: #ffffff;'>Analyze startup trends using investment patterns, locations, and industries.</h4>
    """, unsafe_allow_html=True)

# Function to fetch startup data from CSV
@st.cache_data
def fetch_startup_data():
    try:
        df = pd.read_csv("startup_funding.csv")  # Ensure the file is in the same directory as app.py
        df.columns = ["Sr No", "Date", "Startup Name", "Industry Vertical", "SubVertical", "City Location", "Investors Name", "Investment Type", "Amount in USD", "Remarks"]
        df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%Y', errors='coerce')
        df["Amount in USD"] = pd.to_numeric(df["Amount in USD"].str.replace(",", ""), errors='coerce')
        return df.drop(columns=["Sr No", "Remarks"])  # Drop unnecessary columns
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return pd.DataFrame()

# Load data once and store in session state
if "startup_df" not in st.session_state:
    st.session_state.startup_df = fetch_startup_data()

startup_df = st.session_state.startup_df

if not startup_df.empty:
    st.success(f"Loaded {len(startup_df)} startups!")

    # Filter UI
    with st.container():
        st.markdown("### 🔍 Filter Startups")
        col1, col2, col3 = st.columns(3)
        industries = ["All"] + sorted(startup_df["Industry Vertical"].dropna().unique().tolist())
        cities = ["All"] + sorted(startup_df["City Location"].dropna().unique().tolist())
        years = ["All"] + sorted(startup_df["Date"].dropna().dt.year.unique().tolist())
        
        selected_industry = col1.selectbox("Select Industry", industries)
        selected_city = col2.selectbox("Select City", cities)
        selected_year = col3.selectbox("Select Year", years)

    filtered_df = startup_df.copy()
    if selected_industry != "All":
        filtered_df = filtered_df[filtered_df["Industry Vertical"] == selected_industry]
    if selected_city != "All":
        filtered_df = filtered_df[filtered_df["City Location"] == selected_city]
    if selected_year != "All":
        filtered_df = filtered_df[filtered_df["Date"].dt.year == selected_year]

    # Display Filtered Data
    st.write("### 📋 Startup Dataset")
    st.dataframe(filtered_df, use_container_width=True)

    # Interactive Investment Distribution
    st.subheader("💰 Investment Distribution by Industry")
    fig_industry = px.bar(filtered_df, x='Industry Vertical', y='Amount in USD', color='Industry Vertical', 
                          title='Investment Trends Across Industries', height=500)
    st.plotly_chart(fig_industry, use_container_width=True)

    # Investment Over Time
    st.subheader("📈 Investment Trend Over Time")
    if not filtered_df['Date'].isnull().all():
        fig_time = px.line(filtered_df, x='Date', y='Amount in USD', color='Industry Vertical', 
                           title='Investment Over Time', markers=True)
        st.plotly_chart(fig_time, use_container_width=True)

    # Top Cities by Investment Amount
    st.subheader("🌆 Top Cities by Investment Amount")
    city_investment = filtered_df.groupby("City Location")["Amount in USD"].sum().reset_index()
    fig_city = px.bar(city_investment.sort_values(by='Amount in USD', ascending=False)[:10], 
                      x='City Location', y='Amount in USD', color='City Location', 
                      title='Top Cities by Investment')
    st.plotly_chart(fig_city, use_container_width=True)

    # Startups Founded Over Time
    st.subheader("📊 Growth of Startups Over the Years")
    startup_counts = filtered_df.groupby(filtered_df['Date'].dt.year).size().reset_index(name='Startup Count')
    fig_growth = px.bar(startup_counts, x='Date', y='Startup Count', title='Number of Startups Founded Each Year', color='Startup Count')
    st.plotly_chart(fig_growth, use_container_width=True)

    # Investor Trends & Insights
    st.subheader("💼 Investor Trends & Insights")
    investor_counts = filtered_df['Investors Name'].value_counts().reset_index()
    investor_counts.columns = ['Investor', 'Number of Investments']
    fig_investors = px.bar(investor_counts.head(10), x='Investor', y='Number of Investments',
                            title='Top Investors by Number of Investments', color='Number of Investments')
    st.plotly_chart(fig_investors, use_container_width=True)

else:
    st.warning("No startup data found.")
    # Function to fetch startup data from CSV
@st.cache_data
def fetch_startup_data():
    try:
        df = pd.read_csv("startup_funding.csv")  # Ensure the file is in the same directory as app.py
        df.columns = ["Sr No", "Date", "Startup Name", "Industry Vertical", "SubVertical", "City Location", "Investors Name", "Investment Type", "Amount in USD", "Remarks"]
        df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%Y', errors='coerce')
        df["Amount in USD"] = pd.to_numeric(df["Amount in USD"].str.replace(",", ""), errors='coerce')
        return df.drop(columns=["Sr No", "Remarks"])  # Drop unnecessary columns
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return pd.DataFrame()

# Load data once and store in session state
if "startup_df" not in st.session_state:
    st.session_state.startup_df = fetch_startup_data()

startup_df = st.session_state.startup_df

if not startup_df.empty:
    st.success(f"Loaded {len(startup_df)} startups!")

    # Market Prediction using Facebook Prophet
    st.subheader("📊 Market Prediction: Future Funding Trends")
    if not startup_df["Date"].isnull().all():
        funding_data = startup_df.groupby("Date")["Amount in USD"].sum().reset_index()
        funding_data = funding_data.rename(columns={"Date": "ds", "Amount in USD": "y"})
        
        model = Prophet()
        model.fit(funding_data)
        future = model.make_future_dataframe(periods=365, freq='D')
        forecast = model.predict(future)
        
        fig_forecast = prophet_plot(model, forecast)

        st.plotly_chart(fig_forecast, use_container_width=True)
    else:
        st.warning("Not enough data for market prediction.")

else:
    st.warning("No startup data found.")

# Footer
st.write("<p style='text-align: center;'>Made with ❤️ using Streamlit, Pandas, and Plotly</p>", unsafe_allow_html=True)
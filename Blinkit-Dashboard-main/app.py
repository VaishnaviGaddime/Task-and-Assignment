import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Blinkit Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_excel("BlinkIT Grocery Data.xlsx")
    return df

df = load_data()




# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.markdown("## 🟡 Blinkit Filter Panel")

outlet_location = st.sidebar.multiselect(
    "Outlet Location Type",
    options=df["Outlet Location Type"].unique(),
    default=df["Outlet Location Type"].unique()
)

outlet_size = st.sidebar.multiselect(
    "Outlet Size",
    options=df["Outlet Size"].dropna().unique(),
    default=df["Outlet Size"].dropna().unique()
)

item_type = st.sidebar.multiselect(
    "Item Type",
    options=df["Item Type"].unique(),
    default=df["Item Type"].unique()
)

filtered_df = df[
    (df["Outlet Location Type"].isin(outlet_location)) &
    (df["Outlet Size"].isin(outlet_size)) &
    (df["Item Type"].isin(item_type))
]

# ---------------- KPI CALCULATIONS ----------------
total_sales = filtered_df["Sales"].sum()
num_items = filtered_df.shape[0]
avg_sales = filtered_df["Sales"].mean()
avg_rating = filtered_df["Rating"].mean()  # dataset has no rating column

# ---------------- KPI DISPLAY ----------------
st.markdown("## 🛒 Blinkit – India Last Minute App")

k1, k2, k3, k4 = st.columns(4)

k1.metric("💰 Total Sales", f"${total_sales/1e6:.2f}M")
k2.metric("📦 Number of Items", f"{num_items}")
k3.metric("📊 Average Sales", f"${avg_sales:.0f}")
k4.metric("⭐ Average Rating", f"{avg_rating:.1f}")

st.markdown("---")

# ---------------- OUTLET ESTABLISHMENT (AREA) ----------------
yearly_sales = (
    filtered_df.groupby("Outlet Establishment Year")["Sales"]
    .sum()
    .reset_index()
)

fig_area = px.area(
    yearly_sales,
    x="Outlet Establishment Year",
    y="Sales",
    title="Outlet Establishment Trend",
    markers=True
)
st.plotly_chart(fig_area, use_container_width=True)

# ---------------- SECOND ROW ----------------
c1, c2, c3 = st.columns([2, 1, 1])

# -------- ITEM TYPE SALES (BAR) --------
item_sales = (
    filtered_df.groupby("Item Type")["Sales"]
    .sum()
    .sort_values()
    .reset_index()
)

fig_item = px.bar(
    item_sales,
    x="Sales",
    y="Item Type",
    orientation="h",
    title="Sales by Item Type",
    color="Sales",
    color_continuous_scale="YlOrBr"
)

c1.plotly_chart(fig_item, use_container_width=True)

# -------- FAT CONTENT (DONUT) --------
fat_sales = (
    filtered_df.groupby("Item Fat Content")["Sales"]
    .sum()
    .reset_index()
)

fig_fat = px.pie(
    fat_sales,
    names="Item Fat Content",
    values="Sales",
    hole=0.5,
    title="Fat Content Contribution"
)

c2.plotly_chart(fig_fat, use_container_width=True)

# -------- OUTLET SIZE (DONUT) --------
size_sales = (
    filtered_df.groupby("Outlet Size")["Sales"]
    .sum()
    .reset_index()
)

fig_size = px.pie(
    size_sales,
    names="Outlet Size",
    values="Sales",
    hole=0.5,
    title="Outlet Size Contribution"
)

c3.plotly_chart(fig_size, use_container_width=True)

# ---------------- OUTLET LOCATION ----------------
location_sales = (
    filtered_df.groupby("Outlet Location Type")["Sales"]
    .sum()
    .reset_index()
)

fig_location = px.bar(
    location_sales,
    x="Sales",
    y="Outlet Location Type",
    orientation="h",
    title="Sales by Outlet Location",
    color="Outlet Location Type"
)

st.plotly_chart(fig_location, use_container_width=True)

# ---------------- SUMMARY TABLE ----------------
st.markdown("## 📋 Outlet Performance Summary")

summary_table = filtered_df.groupby("Outlet Type").agg(
    Total_Sales=("Sales", "sum"),
    Number_of_Items=("Sales", "count"),
    Average_Sales=("Sales", "mean"),
    Average_Visibility=("Item Visibility", "mean")
).reset_index()

summary_table["Total_Sales"] = summary_table["Total_Sales"].round(0)
summary_table["Average_Sales"] = summary_table["Average_Sales"].round(0)
summary_table["Average_Visibility"] = summary_table["Average_Visibility"].round(2)

st.dataframe(summary_table, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("📊 **Blinkit Dashboard built using Streamlit & Plotly**")
import pandas as pd
import plotly.express as px
import streamlit as st

def distribution():
    data = pd.read_csv("country_wise_latest.csv")
    st.dataframe(data)

    def barchart():
        st.subheader("Bar chart")
        numeric1 = data.select_dtypes(include=["number"]).columns.tolist()
        top_10 = data.nlargest(10, "Confirmed")
        x1_axis = "Country/Region"
        y1_axis = st.selectbox("Select a column for Bar chart", numeric1)
        # Bar chart
        fig1 = px.bar(top_10, x=x1_axis, y=y1_axis, color=x1_axis, title=f"Distribution of {y1_axis} based on {x1_axis}")
        st.plotly_chart(fig1)
    barchart()
    
    def multibarchart():
        st.subheader("Multiple bar chart")
        top_10 = data.nlargest(10, "Confirmed")
        categorical = data.select_dtypes(include=["object"]).columns.tolist()
        numeric2 = data.select_dtypes(include=["number"]).columns.tolist()
        x2_axis = st.selectbox("Select column for X-axis", categorical)
        y2_axis = st.multiselect("Select a column for Grouped Bar chart", numeric2)
        # Multibar chart
        fig2 = px.histogram(top_10, x=x2_axis, y=y2_axis, color="Country/Region", title=f"Distribution of {"".join(y2_axis)} based on {x2_axis}", barmode="group")
        st.plotly_chart(fig2)
    multibarchart()
    
    def piechart():
        st.subheader("Pie chart")
        numeric3 = data.select_dtypes(include=["number"]).columns.tolist()
        x3_axis = "WHO Region"
        y3_axis = st.selectbox("Select a column for Pie chart", numeric3)
        newly_confirmed = data.groupby("WHO Region")[y3_axis].sum().reset_index()
        # Pie chart
        fig3 = px.pie(newly_confirmed, values=y3_axis, names=x3_axis, title=f"Distribution of {y3_axis} based on {x3_axis}")
        st.plotly_chart(fig3)
    piechart()
    
    def donutchart():
        st.subheader("Donut chart")
        numeric4 = data.select_dtypes(include=["number"]).columns.tolist()
        x4_axis = "WHO Region"
        y4_axis = st.selectbox("Select a column for Donut chart", numeric4)
        newly_confirmed = data.groupby("WHO Region")[y4_axis].sum().reset_index()
        # Donut chart
        fig4 = px.pie(newly_confirmed, values=y4_axis, names=x4_axis, hole=0.5, title=f"Distribution of {y4_axis} based on {x4_axis}")
        st.plotly_chart(fig4)
    donutchart()
distribution()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st  # Added for Streamlit integration

from matplotlib.font_manager import FontProperties

"""
Take handled dataframe and generate plots
"""


def visualize_data(df: pd.DataFrame):
    # Filter expenses only (optional)
    expense_df = df[df["Type"] == "Expense"]

    # 1. Pie chart for different Category (expenses only)
    categorys = expense_df["Category"]
    values = expense_df["Amount / Cost"]

    fig = go.Figure(data=[go.Pie(labels=categorys, values=values)])
    fig.update_traces(hoverinfo='label+value', textinfo='percent')
    fig.update_layout(title="Distribution of Expenses by Category")

    st.plotly_chart(fig)

    # 2. Pie chart for different For Whom
    for_whom = expense_df["For Whom"]
    
    fig = go.Figure(data=[go.Pie(labels=for_whom, values=values)])
    fig.update_traces(hoverinfo='label+value', textinfo='percent')
    fig.update_layout(title="Distribution of Expenses by For Whom")
    
    st.plotly_chart(fig)

    # 3. Column chart showing days with different categories
    daily_category_totals = (
        expense_df.groupby(["Day", "Category"])["Amount / Cost"].sum().unstack()
    )
    daily_category_totals.fillna(0, inplace=True)  # Replace NaN with 0
    daily_category_totals = daily_category_totals.stack().reset_index()
    daily_category_totals.columns = ["Day", "Category", "Amount"]

    # Create the Plotly figure
    fig = px.bar(
        daily_category_totals,
        x="Day",
        y="Amount",
        color="Category",
    )

    for data in fig.data:
        data.width = 1

    fig.update_layout(
        title="Daily Expenses by Category",
        xaxis_tickangle=-45,
        yaxis=dict(range=[0, 10000]),
    )

    st.plotly_chart(fig)

    # 4. Line chart showing expenses/income over time (optional)
    df_by_day = df.groupby(["Day", "Type"])["Amount / Cost"].sum().unstack()
    df_by_day = df_by_day.reset_index()
    df_by_day.fillna(0, inplace=True)

    # Create the Plotly figure
    fig = px.line(
        df_by_day,
        x="Day",
        y=df_by_day.columns[1:],  # Use all columns except "Day" (assuming expenses and income)
        title="Expenses vs Income Over Time",
        markers=True,
    )

    fig.update_layout(
        legend_title="Category"
    )

    st.plotly_chart(fig)

    # # Calculate total expenses per day
    # total_expenses = expense_df.groupby('Day')['Amount / Cost'].sum()
    # # Calculate ECDF
    # x, y = np.sort(total_expenses), np.arange(len(total_expenses)) / len(total_expenses)

    # # Create the Plotly figure
    # fig = px.line(x=x, y=y, labels={'x': 'Total Expenses', 'y': 'Cumulative Probability'})
    # fig.update_layout(title='ECDF of Total Expenses')

    # st.plotly_chart(fig)



def app():
    # Load data (replace with actual data loading logic)
    df = pd.read_csv("cleaned_data.csv")

    # Title and introduction (optional)
    st.title("Expense Visualizations")
    st.write("This dashboard presents various visualizations of your expenses.")

    # Call visualize_data function
    visualize_data(df)


if __name__ == "__main__":
    app()

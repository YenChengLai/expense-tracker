import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

"""
Take handled dataframe and generate plots
"""
def visualize_data():

    # Load the cleaned data from CSV (or directly from clean_and_transform_data function)
    df = pd.read_csv('cleaned_data.csv')

    # Filter expenses only (optional)
    expense_df = df[df["Type"] == "Expense"]

    # 1. Pie chart for different Category (expenses only)
    category_totals = (
        expense_df.groupby("Category")["Amount / Cost"]
        .sum()
        .sort_values(ascending=False)
    )
    plt.rcParams["font.family"] = ["kaiu"]
    plt.figure(figsize=(8, 8))
    plt.pie(
        category_totals,
        labels=category_totals.index,
        autopct="%1.1f%%",
        textprops={
            "fontproperties": FontProperties(
                fname=os.path.join(os.path.dirname(__file__), "../resources/kaiu.ttf")
            )
        },
    )
    plt.title("Distribution of Expenses by Category")
    plt.show()

    # 2. Pie chart for different For Whom
    for_whom_totals = (
        expense_df.groupby("For Whom")["Amount / Cost"]
        .sum()
        .sort_values(ascending=False)
    )
    plt.figure(figsize=(8, 8))
    plt.pie(for_whom_totals, labels=for_whom_totals.index, autopct="%1.1f%%")
    plt.title("Distribution of Expenses by For Whom")
    plt.show()

    # 3. Column chart showing days with different categories
    daily_category_totals = (
        expense_df.groupby(["Day", "Category"])["Amount / Cost"].sum().unstack()
    )
    daily_category_totals.fillna(0, inplace=True)  # Replace NaN with 0
    daily_category_totals.plot(kind="bar", stacked=False)
    plt.xlabel("Day")
    plt.ylabel("Amount")
    plt.title("Daily Expenses by Category")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    # Apply font to legend labels and title
    prop = FontProperties(
        fname=os.path.join(os.path.dirname(__file__), "../resources/kaiu.ttf")
    )
    plt.legend(title="Category", loc="upper left", bbox_to_anchor=(1, 1), prop=prop)

    # Set y-axis limit
    plt.ylim(0, 5000)
    # Adjust legend position
    plt.subplots_adjust(bottom=0.2)  # Adjust space for x-axis labels
    plt.show()

    # 4. Line chart showing expenses/income over time (optional)
    df_by_day = df.groupby(["Day", "Type"])["Amount / Cost"].sum().unstack()
    df_by_day.fillna(0, inplace=True)  # Replace NaN with 0
    df_by_day.plot(kind="line")
    plt.xlabel("Day")
    plt.ylabel("Amount")
    plt.title("Expenses vs Income Over Time")
    plt.legend(title="Type", loc="upper left", bbox_to_anchor=(1, 1))

    # Adjust legend position
    plt.subplots_adjust(bottom=0.2)  # Adjust space for x-axis labels
    plt.show()

visualize_data()

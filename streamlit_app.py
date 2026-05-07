import streamlit as st
import pandas as pd
import numpy as np

st.title("Grocery Shopping Optimization")

st.write(
    "This app uses 0/1 Knapsack Dynamic Programming "
    "to select grocery items within a budget."
)

uploaded_file = st.file_uploader(
    "Upload Grocery Dataset CSV File",
    type=["csv"]
)

budget = st.number_input(
    "Enter grocery budget",
    min_value=1,
    value=30
)


def clean_data(df):

    needed_cols = [
        "product_name",
        "brands",
        "energy_100g",
        "proteins_100g",
        "carbohydrates_100g",
        "fat_100g",
        "fiber_100g",
        "sugars_100g",
        "salt_100g",
    ]

    df = df[needed_cols].copy()

    df = df.dropna(subset=[
        "product_name",
        "proteins_100g",
        "fiber_100g",
        "sugars_100g",
        "salt_100g"
    ])

    numeric_cols = [
        "energy_100g",
        "proteins_100g",
        "carbohydrates_100g",
        "fat_100g",
        "fiber_100g",
        "sugars_100g",
        "salt_100g"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna()

    df = df.head(200)

    return df


def create_price_and_score(df):

    np.random.seed(42)

    df["price"] = np.random.randint(
        2,
        13,
        size=len(df)
    )

    df["nutrition_score"] = (
        df["proteins_100g"] * 2
        + df["fiber_100g"] * 2
        - df["sugars_100g"] * 0.5
        - df["salt_100g"] * 2
    )

    min_score = df["nutrition_score"].min()

    if min_score < 0:
        df["nutrition_score"] += abs(min_score) + 1

    df["nutrition_score"] = (
        df["nutrition_score"]
        .round()
        .astype(int)
    )

    return df


def knapsack(items, budget):

    n = len(items)

    prices = items["price"].tolist()

    values = items["nutrition_score"].tolist()

    dp = [
        [0 for b in range(budget + 1)]
        for i in range(n + 1)
    ]

    for i in range(1, n + 1):

        item_price = prices[i - 1]

        item_value = values[i - 1]

        for b in range(budget + 1):

            if item_price <= b:

                take_item = (
                    item_value
                    + dp[i - 1][b - item_price]
                )

                skip_item = dp[i - 1][b]

                dp[i][b] = max(
                    take_item,
                    skip_item
                )

            else:
                dp[i][b] = dp[i - 1][b]

    selected_indexes = []

    b = budget

    for i in range(n, 0, -1):

        if dp[i][b] != dp[i - 1][b]:

            selected_indexes.append(i - 1)

            b = b - prices[i - 1]

    selected_indexes.reverse()

    return selected_indexes, dp[n][budget]


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df = clean_data(df)

    df = create_price_and_score(df)

    st.success("Dataset uploaded successfully!")

    if st.button("Optimize Grocery Basket"):

        selected_indexes, best_score = knapsack(
            df,
            int(budget)
        )

        selected_items = df.iloc[selected_indexes]

        st.subheader("Selected Grocery Items")

        st.dataframe(
            selected_items[
                [
                    "product_name",
                    "brands",
                    "price",
                    "proteins_100g",
                    "fiber_100g",
                    "sugars_100g",
                    "salt_100g",
                    "nutrition_score"
                ]
            ]
        )

        total_cost = selected_items["price"].sum()

        st.subheader("Summary")

        st.write("Budget:", budget)

        st.write("Total Cost:", total_cost)

        st.write(
            "Remaining Budget:",
            budget - total_cost
        )

        st.write(
            "Total Nutrition Score:",
            best_score
        )

        st.write(
            "Number of Selected Items:",
            len(selected_items)
        )

        st.subheader("Nutrition Score Graph")

        chart_data = selected_items[
            [
                "product_name",
                "nutrition_score"
            ]
        ].head(10)

        st.bar_chart(
            chart_data.set_index(
                "product_name"
            )
        )

        csv = selected_items.to_csv(index=False)

        st.download_button(
            "Download selected_items.csv",
            csv,
            "selected_items.csv",
            "text/csv"
        )

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATA_PATH = "data/en.openfoodfacts.org.products.tsv"


def load_data(path):
    df = pd.read_csv(path, sep="\t", low_memory=False)
    return df


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

    df["price"] = np.random.randint(2, 13, size=len(df))

    df["nutrition_score"] = (
        df["proteins_100g"] * 2
        + df["fiber_100g"] * 2
        - df["sugars_100g"] * 0.5
        - df["salt_100g"] * 2
    )

    min_score = df["nutrition_score"].min()

    if min_score < 0:
        df["nutrition_score"] += abs(min_score) + 1

    df["nutrition_score"] = df["nutrition_score"].round().astype(int)

    return df


def knapsack(items, budget):

    n = len(items)

    prices = items["price"].tolist()
    values = items["nutrition_score"].tolist()

    dp = [[0 for b in range(budget + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        item_price = prices[i - 1]
        item_value = values[i - 1]

        for b in range(budget + 1):

            if item_price <= b:
                take_item = item_value + dp[i - 1][b - item_price]
                skip_item = dp[i - 1][b]

                dp[i][b] = max(take_item, skip_item)

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


def main():

    print("Loading dataset...")

    df = load_data(DATA_PATH)

    print("Cleaning dataset...")

    df = clean_data(df)

    print("Creating scores...")

    df = create_price_and_score(df)

    print(df.head())

    budget = int(input("\nEnter grocery budget: "))

    selected_indexes, best_score = knapsack(df, budget)

    selected_items = df.iloc[selected_indexes]

    print("\nSelected items:\n")

    print(
        selected_items[
            [
                "product_name",
                "brands",
                "price",
                "proteins_100g",
                "fiber_100g",
                "sugars_100g",
                "salt_100g",
                "nutrition_score",
            ]
        ]
    )

    total_cost = selected_items["price"].sum()

    print("\n========== SUMMARY ==========")

    print("Budget:", budget)

    print("Total cost:", total_cost)

    print("Remaining budget:", budget - total_cost)

    print("Best nutrition score:", best_score)

    print("Number of selected items:", len(selected_items))

    selected_items.to_csv(
        "outputs/selected_items.csv",
        index=False
    )

    print("\nSaved results to outputs/selected_items.csv")

    plt.figure(figsize=(10, 6))

    plt.bar(
        selected_items["product_name"].head(10),
        selected_items["nutrition_score"].head(10)
    )

    plt.xticks(rotation=75)

    plt.xlabel("Product Name")

    plt.ylabel("Nutrition Score")

    plt.title("Selected Grocery Items vs Nutrition Score")

    plt.tight_layout()

    plt.savefig("outputs/nutrition_plot.png")

    plt.show()

    print("Saved graph to outputs/nutrition_plot.png")



if __name__ == "__main__":
    main()
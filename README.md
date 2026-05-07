# Grocery Shopping Optimization Using Dynamic Programming

## AI Usage Statement

AI tools were used only for UI guidance, debugging assistance, deployment support, and general project guidance.

The project idea, dynamic programming approach, algorithm implementation, core logic, comments, and documentation were manually developed and authored by the project team in accordance with assignment requirements.

---

# Project Overview

This project applies the **0/1 Knapsack Dynamic Programming algorithm** to solve a real-world grocery shopping optimization problem. The goal is to help users select the best combination of grocery items while staying within a fixed budget and maximizing nutritional value.

The project uses the **Open Food Facts dataset**, which contains nutritional information for real grocery products.

A Streamlit web application was also developed to allow users to upload a dataset, enter a grocery budget, and generate an optimized grocery basket dynamically.

---

# Problem Statement

When shopping for groceries, it is often difficult to compare multiple products and decide which items provide the best nutritional value while staying within budget.

This project models the grocery selection problem as a **0/1 Knapsack problem**:

- Each grocery item has:
  - a cost (price)
  - a nutritional value score
- The objective is to:
  - maximize total nutrition score
  - while keeping total cost within a fixed budget

The algorithm computes the optimal set of grocery items based on the user’s budget.

---

# Dataset

Dataset Used:
- Open Food Facts Dataset

Dataset Sources:
- Kaggle: https://www.kaggle.com/datasets/openfoodfacts/world-food-facts
- Official Website: https://world.openfoodfacts.org/data

The dataset contains:
- product names
- brands
- nutritional values
- ingredients
- calories
- protein
- sugar
- fiber
- salt
- other food-related attributes

For this project, only relevant nutritional columns were selected and cleaned.

---

# Algorithm Used

## 0/1 Knapsack Dynamic Programming

The grocery optimization problem is solved using the **0/1 Knapsack algorithm**.

Each grocery item:
- can either be selected once or not selected
- has:
  - price → weight
  - nutrition score → value

The algorithm determines the optimal combination of grocery items that maximizes nutritional value while remaining within the specified budget.

Dynamic Programming was used to efficiently evaluate all possible combinations.

---

# Features

- Dataset preprocessing and cleaning
- Nutrition score calculation
- Grocery budget optimization
- 0/1 Knapsack Dynamic Programming implementation
- CSV export of selected grocery items
- Nutrition score visualization graph
- Interactive Streamlit web application

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit

---

# Project Structure

```text
grocery-knapsack-project/
│
├── src/
│   └── main.py
│
├── outputs/
│   ├── selected_items.csv
│   ├── nutrition_plot.png
│   └── sample_data.csv
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── demo_video.mp4
├── presentation.pdf
└── proposal.pdf
```

# Run Main Python Program

```bash
py src/main.py
```

The program:

- loads the dataset
- preprocesses the data
- calculates nutrition scores
- applies the knapsack algorithm
- generates optimized grocery selections

---

# Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

# Streamlit Hosted App

Hosted Application:

https://grocery-knapsack-project-x2g9sc7htbngsam8fhqqhd.streamlit.app/

---

# Example Workflow

1. Upload grocery dataset CSV file
2. Enter grocery budget
3. Click **“Optimize Grocery Basket”**
4. View:
   - selected grocery items
   - nutrition score graph
   - total cost
   - remaining budget
5. Download optimized grocery CSV results

---

# Results

The algorithm successfully generates optimized grocery baskets based on user-defined budgets.

### Example

- Budget: $30
- Total Cost: $30
- Nutrition Score: 1219

The project demonstrates how Dynamic Programming can solve practical real-world optimization problems.

---


# Team Members

- Simran Kharbanda (UID: 122283671)
- Shashank Ashoka (UID: 122241329)


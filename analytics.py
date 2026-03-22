import sys
import pandas as pd


def save_insight(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <input_csv>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Load dataset
    df = pd.read_csv(input_file)

    insights = []

    # Insight 1: dataset shape
    rows, cols = df.shape
    insights.append(
        f"The preprocessed dataset contains {rows} rows and {cols} columns."
    )

    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    # Insight 2: numeric columns summary
    if numeric_cols:
        means = df[numeric_cols].mean(numeric_only=True)
        top_mean_col = means.idxmax()
        top_mean_val = means.max()
        insights.append(
            f"Among the numeric columns, '{top_mean_col}' has the highest average value ({top_mean_val:.2f})."
        )
    else:
        insights.append("There are no numeric columns available for numerical analysis.")

    # Insight 3: most frequent value in first categorical column
    if categorical_cols:
        col = categorical_cols[0]
        most_common_value = df[col].mode(dropna=True)[0]
        freq = df[col].value_counts(dropna=True).iloc[0]
        insights.append(
            f"In the categorical column '{col}', the most frequent value is '{most_common_value}', appearing {freq} times."
        )
    else:
        insights.append("There are no categorical columns available for category-based analysis.")

    # Save insights in separate files
    save_insight("insight1.txt", insights[0])
    save_insight("insight2.txt", insights[1])
    save_insight("insight3.txt", insights[2])

    print("Generated insight1.txt, insight2.txt, and insight3.txt successfully.")


if __name__ == "__main__":
    main()
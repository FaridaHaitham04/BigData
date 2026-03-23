import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize.py <input_csv>")
        sys.exit(1)

    data_path = sys.argv[1]
    df = pd.read_csv(data_path)

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        print("No numeric columns found for visualization.")
        sys.exit(1)

    plt.figure(figsize=(18, 5))

    # 1) Histogram
    plt.subplot(1, 3, 1)
    if "Age" in numeric_df.columns:
        plt.hist(numeric_df["Age"], bins=20, edgecolor="black")
        plt.title("Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
    else:
        first_col = numeric_df.columns[0]
        plt.hist(numeric_df[first_col], bins=20, edgecolor="black")
        plt.title(f"{first_col} Distribution")
        plt.xlabel(first_col)
        plt.ylabel("Frequency")

    # 2) Boxplot
    plt.subplot(1, 3, 2)
    if "MonthlyIncome" in numeric_df.columns:
        sns.boxplot(y=numeric_df["MonthlyIncome"])
        plt.title("Monthly Income Boxplot")
        plt.ylabel("MonthlyIncome")
    else:
        second_col = numeric_df.columns[1] if len(numeric_df.columns) > 1 else numeric_df.columns[0]
        sns.boxplot(y=numeric_df[second_col])
        plt.title(f"{second_col} Boxplot")
        plt.ylabel(second_col)

    # 3) Correlation Heatmap
    plt.subplot(1, 3, 3)
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.savefig("summary_plot.png")
    plt.close()

    print("Plots saved as summary_plot.png")

    subprocess.run(["python", "cluster.py", data_path], check=True)

if __name__ == "__main__":
    main()
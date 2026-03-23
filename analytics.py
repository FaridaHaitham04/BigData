import sys
import subprocess
import pandas as pd


def save_insight(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <input_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    df = pd.read_csv(input_file)

    # Insight 1: Income variation
    if "MonthlyIncome" in df.columns:
        max_income = df["MonthlyIncome"].max()
        min_income = df["MonthlyIncome"].min()

        insight1 = (
            f"In the preprocessed dataset, the highest scaled MonthlyIncome value is {max_income:.2f} "
            f"and the lowest is {min_income:.2f}, showing variation in employee income levels."
        )
    else:
        insight1 = "MonthlyIncome column was not found, so income analysis could not be performed."

    save_insight("insight1.txt", insight1)

    # Insight 2: Attrition vs income
    if "Attrition" in df.columns and "MonthlyIncome" in df.columns:
        avg_income = df.groupby("Attrition")["MonthlyIncome"].mean()

        if len(avg_income) >= 2:
            lowest_group = avg_income.idxmin()
            highest_group = avg_income.idxmax()

            insight2 = (
                f"The average scaled MonthlyIncome differs across encoded attrition groups. "
                f"Group {lowest_group} has the lower average income ({avg_income[lowest_group]:.2f}), "
                f"while group {highest_group} has the higher average income ({avg_income[highest_group]:.2f})."
            )
        else:
            insight2 = "There are not enough attrition groups to compare average income."
    else:
        insight2 = "Attrition or MonthlyIncome column was not found, so attrition-income analysis could not be performed."

    save_insight("insight2.txt", insight2)

    # Insight 3: Department with highest attrition
    if "Department" in df.columns and "Attrition" in df.columns:
        attrition_counts = df.groupby("Department")["Attrition"].sum()

        if not attrition_counts.empty:
            top_department = attrition_counts.idxmax()
            top_value = attrition_counts.max()

            insight3 = (
                f"Encoded department {top_department} has the highest total attrition score ({top_value}), "
                f"suggesting it is the department most associated with employee leaving in the processed dataset."
            )
        else:
            insight3 = "Department attrition analysis could not be completed because no grouped data was found."
    else:
        insight3 = "Department or Attrition column was not found, so department attrition analysis could not be performed."

    save_insight("insight3.txt", insight3)

    print("Insights generated successfully: insight1.txt, insight2.txt, insight3.txt")

    # Call next script
    subprocess.run(["python", "visualize.py", input_file], check=True)


if __name__ == "__main__":
    main()
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

 
    # Insight 1: Salary range

    if 'MonthlyIncome' in df.columns:
        max_salary = df['MonthlyIncome'].max()
        min_salary = df['MonthlyIncome'].min()

        insight1 = (
            f"The highest monthly income in the dataset is {max_salary}, "
            f"while the lowest is {min_salary}, indicating variation in employee salaries."
        )
    else:
        insight1 = "MonthlyIncome column not found, so salary analysis could not be performed."

    save_insight("insight1.txt", insight1)


    # Insight 2: Attrition vs Salary
  
    if 'Attrition' in df.columns and 'MonthlyIncome' in df.columns:
        avg_income = df.groupby('Attrition')['MonthlyIncome'].mean()

        if 'Yes' in avg_income.index and 'No' in avg_income.index:
            insight2 = (
                f"Employees who left the company have an average income of {avg_income['Yes']:.2f}, "
                f"while those who stayed have an average income of {avg_income['No']:.2f}. "
                f"This suggests a relationship between salary and employee attrition."
            )
        else:
            insight2 = "Not enough data to compare attrition groups."
    else:
        insight2 = "Required columns for attrition analysis are missing."

    save_insight("insight2.txt", insight2)

    
    # Insight 3: Department attrition
   
    if 'Department' in df.columns and 'Attrition' in df.columns:
        attrition_df = df[df['Attrition'] == 'Yes']

        if not attrition_df.empty:
            top_dept = attrition_df['Department'].value_counts().idxmax()
            count = attrition_df['Department'].value_counts().max()

            insight3 = (
                f"The department with the highest employee attrition is {top_dept}, "
                f"with {count} employees leaving."
            )
        else:
            insight3 = "No attrition cases found in the dataset."
    else:
        insight3 = "Department or Attrition column not found."

    save_insight("insight3.txt", insight3)

    print("Insights generated successfully.")


if __name__ == "__main__":
    main()
import sys
import subprocess
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA

def main():
    if len(sys.argv) < 2:
        print("Usage: python preprocess.py <input_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = pd.read_csv(input_path)


                                                    # 1) DATA CLEANING 

    # Task 1: Remove duplicates
    df = df.drop_duplicates()

    # Task 2: Handle missing values (numeric → median)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Task 3: Handle missing values in categorical columns using mode
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
    for col in categorical_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])


    # Fix inconsistent text (e.g., 'hr' vs 'HR')
    if "Department" in df.columns:
        df["Department"] = df["Department"].astype(str).str.upper().str.strip()

  
                                                 # 2) FEATURE TRANSFORMATION


    # Task 1: Encode categorical columns
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    # Task 2: Scale numeric features
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Task 3 (extra): Create new feature
    if "MonthlyIncome" in df.columns:
        df["Income_per_Year"] = df["MonthlyIncome"] * 12


                                                # 3) DIMENSIONALITY REDUCTION 

    # Task 1: Select subset of important features
    selected_features = df[["Age", "MonthlyIncome", "YearsAtCompany", "JobSatisfaction"]]

    # Task 2: Apply PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(selected_features)

    df["PCA1"] = pca_result[:, 0]
    df["PCA2"] = pca_result[:, 1]

    #  (extra): Drop less useful column
    if "EmployeeID" in df.columns:
        df = df.drop(columns=["EmployeeID"])
 
                                                # 4) DISCRETIZATION 


    # Task 1: Bin Age
    df["Age_Binned"] = pd.cut(df["Age"], bins=3, labels=["Young", "Mid", "Senior"])

    # Task 2: Bin Monthly Income
    df["Income_Binned"] = pd.cut(df["MonthlyIncome"], bins=3, labels=["Low", "Medium", "High"])

    # Task 3: Encode binned columns
    df["Age_Binned"] = LabelEncoder().fit_transform(df["Age_Binned"].astype(str))
    df["Income_Binned"] = LabelEncoder().fit_transform(df["Income_Binned"].astype(str))



    output_path = "data_preprocessed.csv"
    df.to_csv(output_path, index=False)

    print(f"Preprocessed data saved to {output_path}")

    
    subprocess.run(["python", "analytics.py", output_path], check=True)


if __name__ == "__main__":
    main()
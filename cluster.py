import pandas as pd
from sklearn.cluster import KMeans
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python cluster.py <input_csv>")
        sys.exit(1)

    data_path = sys.argv[1]
    df = pd.read_csv(data_path)

    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if numeric_df.empty:
        print("No numeric columns found for clustering.")
        sys.exit(1)

    # Use a subset of features if available
    preferred_features = ["Age", "MonthlyIncome", "YearsAtCompany", "JobSatisfaction"]
    selected_features = [col for col in preferred_features if col in numeric_df.columns]

    if len(selected_features) >= 2:
        cluster_data = numeric_df[selected_features]
    else:
        cluster_data = numeric_df

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(cluster_data)

    df["Cluster"] = clusters
    cluster_counts = df["Cluster"].value_counts().sort_index()

    with open("clusters.txt", "w", encoding="utf-8") as f:
        for cluster, count in cluster_counts.items():
            f.write(f"Cluster {cluster}: {count} samples\n")

    print("Clustering done. Results saved in clusters.txt")

if __name__ == "__main__":
    main()
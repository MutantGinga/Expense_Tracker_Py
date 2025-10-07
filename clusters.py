import pandas as pd
import numpy as np
from vectorizer import vectorize_text
from find_clusters import cluster_transactions

def process_transactions(df, n_clusters=5):
    # Vectorize the transaction descriptions
    X, vectorizer = vectorize_text(df['Description'].fillna(''))
    
    # Cluster the transactions
    kmeans, labels = cluster_transactions(X, n_clusters=n_clusters)
    
    # Add the cluster labels to the original DataFrame
    df['Cluster'] = labels
    return df, kmeans, vectorizer

def print_top_words_per_cluster(kmeans, vectorizer, n_words=10):

    terms = vectorizer.get_feature_names_out()
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]

    for cluster_num in range(kmeans.n_clusters):
        top_terms = [terms[ind] for ind in order_centroids[cluster_num, :n_words]]
        print(f"Cluster {cluster_num}: {', '.join(top_terms)}")

df = pd.read_excel('Statement_cleaned.xlsx')
processed_df, kmeans, vectorizer = process_transactions(df)
#print(processed_df.to_string())
print_top_words_per_cluster(kmeans, vectorizer)
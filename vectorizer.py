from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(texts):
    custom_stop = ["apple", "pay", "via", "gb", "2025", "on"]
    vectorizer = TfidfVectorizer(
        ngram_range=(1,2),
        max_df=0.8,
        min_df=1,
        stop_words=custom_stop
    )
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

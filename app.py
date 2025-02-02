import streamlit as st
import pandas as pd
import numpy as np
import re
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Load dataset
url = "https://raw.githubusercontent.com/fenago/datasets/refs/heads/main/sample-data.csv"
df = pd.read_csv(url)

# ✅ Remove HTML tags from descriptions
def clean_html(text):
    return re.sub(r"<.*?>", "", text)  # Strip HTML tags

df["description"] = df["description"].apply(clean_html)

# ✅ Tokenize descriptions
df["tokenized_desc"] = df["description"].apply(lambda x: x.split())

# ✅ Extract product name (first words before "-")
df["product_name"] = df["description"].apply(lambda x: x.split("-")[0].strip())

# ✅ Create categories (Use first word of the product name as category)
df["category"] = df["product_name"].apply(lambda x: x.split()[0].strip())

# ✅ Load trained Word2Vec model
try:
    model = Word2Vec.load("word2vec_model.model")
    # st.success("✅ Word2Vec model loaded successfully!")  # Commented out
except Exception as e:
    st.error(f"⚠️ Failed to load model: {e}")

# ✅ Convert text into vectors
def get_vector(text):
    vectors = [model.wv[word] for word in text if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

df["vector"] = df["tokenized_desc"].apply(get_vector)

# ✅ Compute cosine similarity
vectors = np.vstack(df["vector"].values)
similarity_matrix = cosine_similarity(vectors)

# ✅ Recommendation function (Filtered by Category)
def recommend_products(product_name, category, num_recommendations=5):
    try:
        # ✅ Filter the dataset to only include the selected category
        category_df = df[df["category"] == category].reset_index(drop=True)

        # ✅ Find the index of the selected product in the filtered category DataFrame
        product_index = category_df[category_df["product_name"] == product_name].index
        if product_index.empty:
            return pd.DataFrame()  # Return empty DataFrame if product is not found

        product_index = product_index[0]  # Extract index

        # ✅ Retrieve similarity scores for the selected product
        similarity_scores = cosine_similarity(
            [category_df["vector"].iloc[product_index]], 
            np.vstack(category_df["vector"].values)
        )[0]

        # ✅ Get the top N most similar product indices (excluding itself)
        similar_indices = np.argsort(similarity_scores)[-num_recommendations-1:-1][::-1]

        # ✅ Retrieve recommended product details
        recommendations = category_df.iloc[similar_indices][["product_name", "description"]]

        return recommendations

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        return pd.DataFrame()


# ✅ Streamlit UI
st.title("🔍 Product Recommendation System")

# ✅ Style improvements
st.markdown("""
<style>
    div[data-testid="stExpander"] div[role="button"] p {
        font-weight: bold;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ✅ Select a category first
category = st.selectbox("Select a Category:", df["category"].unique())

# ✅ Select a product from the chosen category
filtered_products = df[df["category"] == category]
product_name = st.selectbox("Select a Product:", filtered_products["product_name"].unique())

# ✅ Show selected product details
selected_product = filtered_products[filtered_products["product_name"] == product_name].iloc[0]
st.subheader(f"📌 Selected Product: **{selected_product['product_name']}**")
st.write(f"📝 **Description:** {selected_product['description']}")

# ✅ Show recommended products (from same category)
st.subheader("🔗 Recommended Products:")
recommended_products = recommend_products(product_name, category)

if recommended_products.empty:
    st.warning("⚠️ No recommendations found.")
else:
    for _, row in recommended_products.iterrows():
        with st.expander(f"🔹 **{row['product_name']}**"):
            st.write(f"📖 **Description:** {row['description']}")


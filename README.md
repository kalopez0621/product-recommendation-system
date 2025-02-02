# 🔍 Product Recommendation System

This is a **Streamlit-based Product Recommendation System** that uses **Word2Vec embeddings** and **cosine similarity** to recommend similar products based on their descriptions. The system allows users to **filter by category** and select a product to receive top recommendations.

## 🚀 Features
- **Product Search by Category**: Users can first select a category and then pick a product from that category.
- **Word2Vec Embeddings**: Converts product descriptions into vector representations.
- **Cosine Similarity**: Finds similar products based on their descriptions.
- **Interactive UI with Streamlit**: Users can easily select products and view recommendations.

---

## 📂 Dataset
- The dataset is retrieved from:  
  [🔗 Sample Product Data](https://raw.githubusercontent.com/fenago/datasets/refs/heads/main/sample-data.csv)
- It contains product **IDs, descriptions, and categories**.

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone kalopez0621/product-recommendation-system
```
### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh 
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
### **4️⃣ Run the Streamlit App**
```sh
streamlit run app.py
```
📌 How It Works
Select a Category from the dropdown.
Choose a Product within that category.
The system retrieves top 5 recommended products based on similarity.
Each recommendation includes a product name and description.
🖼️ Screenshot
(Update this with a screenshot URL)

📚 Dependencies
pandas
numpy
gensim
sklearn
streamlit
To install them manually:
```sh
pip install pandas numpy gensim scikit-learn streamlit
```
📌 Future Improvements
✅ Enhance Word2Vec training by fine-tuning hyperparameters.
✅ Improve UI with better visuals & filters.
✅ Deploy online using Streamlit Cloud or Heroku.

🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests.

📝 License
This project is for educational purposes. You may modify and use it freely.

📬 Contact
👤 Karla Lopez
📧 kalopez0621@gmail.com
🔗 GitHub: Kalopez0621

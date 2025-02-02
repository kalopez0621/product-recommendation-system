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
git clone https://github.com/kalopez/product-recommendation-system.git
cd Product-Recommendation
2️⃣ Create a Virtual Environment (Optional but Recommended)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Streamlit App
sh
Copy
Edit
streamlit run app.py
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

sh
Copy
Edit
pip install pandas numpy gensim scikit-learn streamlit
📌 Future Improvements
✅ Enhance Word2Vec training by fine-tuning hyperparameters.
✅ Improve UI with better visuals & filters.
✅ Deploy online using Streamlit Cloud or Heroku.

🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests.

📝 License
This project is for educational purposes. You may modify and use it freely.

📬 Contact
👤 Your Name
📧 your.email@example.com
🔗 GitHub: YourUsername

⭐ If you find this project useful, please give it a star on GitHub! ⭐

yaml
Copy
Edit

---

### **📌 How to Add This README to Your GitHub Repository**
1. **Save the file** as `README.md` in your project folder.
2. **Add & commit the file**:
   ```sh
   git add README.md
   git commit -m "Added README file"
   git push origin main

# 📚 Book Recommendation System — By Category or Title

This project presents a **Python-based Book Recommendation System** that helps users discover new books based on **title similarity** or **category/genre selection**. The system includes a clean, responsive **web interface**, making it accessible and user-friendly, and is powered by efficient **machine learning and data processing libraries**.

---

## 👨‍🎓 Team Members

- Ahmed Mohamed Ahmed Fouad El-Manylawi  
- Ahmed Saeed Mohamed Imam Zayed  
- Ahmed Reda Kamel Abdelghany  
- Ahmed Mohamed Ali Mohamed  
- Mohamed Hazem El-Sayed  

**Supervisor**: Prof. Dr. Medhat Hussein Ahmed  
**Faculty**: Faculty of Engineering – Helwan National University  
**Year**: 2025

---

## 📘 Introduction

In the modern digital era, the vast volume of available books can make it difficult for readers to find relevant titles. This system addresses the problem by providing **personalized recommendations** based on user interest — either through a **searched title** or a selected **book category**.

The system:
- Uses **text similarity algorithms** (TF-IDF, cosine similarity)
- Extracts book relationships from metadata (titles, genres)
- Offers recommendations via a **Python-powered web interface**
- Is adaptable for use in digital libraries or online bookstores

---

## ⚙️ How It Works

### 🧹 Data Preprocessing
- Cleans and normalizes book metadata (title, genre, etc.)
- Removes duplicates, nulls, and irrelevant entries
- Tokenizes and vectorizes textual content using `TfidfVectorizer`

### 📊 Data Visualization
- Charts and graphs used for:
  - Book category distributions
  - Popular titles
  - Recommendation trends
- Visualized using libraries like `matplotlib` and `seaborn`

### 🤖 Recommendation Engine
- **Input Method 1: By Title**
  - Uses cosine similarity to find books with similar textual patterns
- **Input Method 2: By Category**
  - Filters all books within the same genre and suggests random or top-rated picks

---

## 🖥️ Technologies Used

| Tool/Library      | Purpose                               |
|-------------------|----------------------------------------|
| Python            | Backend logic                          |
| Pandas, NumPy     | Data handling and preprocessing         |
| Scikit-learn      | Vectorization and similarity computation|
| Flask             | Web framework for backend API          |
| HTML/CSS/Bootstrap| Front-end design                       |
| Matplotlib, Seaborn | Data visualization                   |

---

## 🌐 Web Interface Features

- 🔍 **Search by title** — Get book suggestions based on similar titles  
- 📚 **Select by category** — Receive recommendations within a selected genre  
- 📈 **Stats/visuals** — Basic insights into the book dataset  
- 💡 **Real-time responses** — Powered by Flask and rendered instantly

---

## 📬 Contact

**Ahmed El-Manylawi**  
📧 Email: ahmed.elmanylawi@gmail.com  
🔗 LinkedIn: [linkedin.com/in/ahmed-el-manylawi-67b6162aa](https://www.linkedin.com/in/ahmed-el-manylawi-67b6162aa)

---

## 📜 License

This project is licensed under the **MIT License**.

> MIT License  
>  
> Copyright (c) 2025 Ahmed El-Manylawi  
>  
> Permission is hereby granted, free of charge, to any person obtaining a copy  
> of this software and associated documentation files (the "Software"), to deal  
> in the Software without restriction, including without limitation the rights  
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
> copies of the Software, and to permit persons to whom the Software is  
> furnished to do so, subject to the following conditions:  
>  
> The above copyright notice and this permission notice shall be  
> included in all copies or substantial portions of the Software.  
>  
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES  
> OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  
> IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  
> DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,  
> ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  
> IN THE SOFTWARE.

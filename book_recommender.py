import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Book Recommender")

def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://wallpapercave.com/wp/wp12420085.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Load data
@st.cache_data
def load_data():
    books = pd.read_csv('Books.csv')
    # Data Preprocessing
    books.columns = books.columns.str.strip()
    for col in books.select_dtypes(include=["object"]).columns:
        books[col] = books[col].replace(r'\s+', ' ', regex=True)
    books.rename(columns={'published': 'published_year', 'average_r': 'average_rating', 'num_page': 'num_pages'}, inplace=True)
    books = books.drop(columns=['subtitle', 'description'])
    books['authors'] = books['authors'].fillna('Unknown')
    books['thumbnail'] = books['thumbnail'].fillna('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOAp5VXoGKS16VrxT0PuDgPsktnBnT614axA&s')
    books['categories'] = books['categories'].fillna('Unknown')
    books['average_rating'] = books['average_rating'].fillna(books['average_rating'].median())
    books['ratings_count'] = books['ratings_count'].fillna(0)
    books.dropna(subset=['num_pages', 'published_year'], inplace=True)
    books.reset_index(drop=True, inplace=True)
    books = books[['title', 'authors', 'categories', 'average_rating', 'ratings_count', 'num_pages', 'published_year', 'thumbnail']]
    books['tags'] = books['title'] + ' ' + books['authors'] + ' ' + books['categories']
    books['tags'] = books['tags'].str.lower()
    return books

# Feature engineering and recommendation setup
@st.cache_data
def setup_recommender(books):
    ps = PorterStemmer()
    def stem_text(text):
        return " ".join([ps.stem(word) for word in text.split()])
    books['tags'] = books['tags'].apply(stem_text)
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vector = cv.fit_transform(books['tags']).toarray()
    similarity = cosine_similarity(vector)
    return books, similarity

# Recommendation by book title
def recommend(book_title, books, similarity):
    try:
        index = books[books['title'].str.lower() == book_title.lower()].index[0]
    except IndexError:
        return pd.DataFrame(), f"Book titled '{book_title}' not found."
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_indices = [i[0] for i in distances[1:6]]
    recommended_books = books.iloc[recommended_indices]
    return recommended_books, None

# Recommendation by category
def recommend_by_category(category_name, books, top_n=5):
    category_books = books[books['categories'].str.contains(category_name, case=False, na=False)].copy()
    if category_books.empty:
        return pd.DataFrame(), f"No books found in category '{category_name}'."
    category_books['score'] = category_books['average_rating'] * category_books['ratings_count']
    top_books = category_books.sort_values(by='score', ascending=False).head(top_n)
    return top_books, None

# Load and process data
books = load_data()
books, similarity = setup_recommender(books)

# Streamlit UI
st.title("Book Recommender")
st.markdown("Get book recommendations by entering a book title or category.")

# Recommendation type selection
recommendation_type = st.selectbox("Select recommendation type:", ["By Book Title", "By Category"])

if recommendation_type == "By Book Title":
    # Create search box with auto-complete that works from first character
    book_title = st.selectbox(
        "Search for a book:",
        options=[""] + sorted(books['title'].unique().tolist()),
        format_func=lambda x: "Type to search..." if x == "" else x
    )
    
    # Show recommendations immediately when a book is selected
    if book_title:
        recommended_books, error = recommend(book_title, books, similarity)
        if error:
            st.error(error)
        elif not recommended_books.empty:
            st.subheader(f"Books similar to '{book_title}':")
            cols = st.columns(5)
            for idx, (_, row) in enumerate(recommended_books.iterrows()):
                with cols[idx]:
                    st.image(row['thumbnail'], width=120)
                    st.write(f"{row['title']}")

else:  # By Category
    # Get unique categories
    all_categories = sorted(list(set([cat.strip() for sublist in books['categories'].str.split(',').dropna() for cat in sublist])))
    
    # Create category search with auto-complete that works from first character
    category = st.selectbox(
        "Search for a category:",
        options=[""] + all_categories,
        format_func=lambda x: "Type to search..." if x == "" else x
    )
        
    # Show recommendations immediately when a category is selected
    if category:
        top_books, error = recommend_by_category(category, books, 5)
        if error:
            st.error(error)
        elif not top_books.empty:
            st.subheader(f"Top {5} books in '{category}' category:")
            cols = st.columns(5)
            for idx, (_, row) in enumerate(top_books.iterrows()):
                with cols[idx]:
                    st.image(row['thumbnail'], width=120)
                    st.write(f"{row['title']}")

# streamlit run book_recommender.py
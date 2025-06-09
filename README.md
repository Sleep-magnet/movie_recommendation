<<<<<<< HEAD
# Movie-Recommendation-system
The project focuses on movie lovers who want to watch movies similarly to the other movie so that they can enjoy
=======
# Project: Movie Recommender System Using Machine Learning!

<img src="demo/6.jpeg" alt="workflow" width="70%">

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

---

# Types of Recommendation Systems:

### 1) Content-Based:
- Content-based systems use characteristic information and take item attributes into consideration.
- Examples: Twitter, YouTube.
- Based on what music you are listening to, which singers you follow, etc.
- User-specific actions or similar item recommendations.
- Vectors are created for features.
- These systems make recommendations using a user's item and profile features.
- Limitation: excessive specialization — can’t explore outside known categories.

### 2) Collaborative Filtering:
- Based on user-item interactions.
- Creates clusters of users with similar ratings or behavior.
- Example use case: Book recommendations.
- Focuses on ratings or reviews as input.
- Core idea: If user A likes item X and user B likes items X and Y, then A may also like Y.
- Limitations:
  - Requires large user-item matrices (can be computationally expensive).
  - Tends to recommend only popular items.
  - New items may never be recommended (cold start problem).

### 3) Hybrid Systems:
- Combines both content-based and collaborative filtering approaches.
- Avoids the shortcomings of using only one approach.
- Often uses techniques like Word2Vec and embeddings.
- Commonly used in modern recommendation engines.

---

# About This Project:

This is a **Streamlit** web application that recommends movies similar to a user's interest.



---

# Demo:

<img src="demo/1.png" alt="workflow" width="70%">
<img src="demo/2.png" alt="workflow" width="70%">
<img src="demo/3.png" alt="workflow" width="70%">

---

# Dataset Used:
- [TMDb 5000 Movie Dataset (Kaggle)](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

---

# Core Concept: Cosine Similarity

1. Cosine Similarity is used to measure document similarity based on vector space.
2. We use NumPy arrays as vectors.
3. `cosine_similarity()` from sklearn computes the similarity score.
4. Values range from 0 (completely different) to 1 (identical).
5. Learn more: [Cosine Similarity - LearnDataSci](https://www.learndatasci.com/glossary/cosine-similarity/)

---

# How to Run

STEP 1 – Clone the Repository
```bash
git clone https://github.com/Sleep-magnet/Movie-Recommendation-system
cd movie-recommender-system

STEP 2 – Create and Activate Conda Environment
conda create -n movie python=3.7.10 -y
conda activate movie

STEP 3 – Install Dependencies
pip install -r requirements.txt

STEP 4 – Generate Model
Run the Jupyter notebook:
Movie Recommender System Data Analysis.ipynb

STEP 5 – Launch Streamlit App
streamlit run app.py
>>>>>>> other/main

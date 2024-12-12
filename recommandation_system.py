import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time
from display import display_intro, progress_bar

#       . _______________________________________________________  .
#       |                                                          |
#       |                 WELCOME TO MY RECOMMAN-                  |  
#       |                      DATION ENGINE                       |     
#       |                  WITH ALMOST 600 USERS                   |
#       |                          BEGIN                           |
#       |                                                          |
#       . ________________________________________________________ .


print("Starting...")
# Loading the data from my dataset from MovieLens
ratings = pd.read_csv('ml-latest-small/ratings.csv', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv('ml-latest-small/movies.csv', usecols=['movieId', 'title'])

# Data processing
data = pd.merge(ratings, movies, on='movieId')
user_item_matrix = data.pivot_table(index='userId', columns='title', values='rating')
user_item_matrix.fillna(0, inplace=True)

# Similarity calculation functions
def calculate_cosine_similarity(matrix):
    return cosine_similarity(matrix)

def calculate_pearson_correlation(matrix):
    return np.corrcoef(matrix)

# Switchable similarity computation
def compute_similarity(matrix, method=1):
    if method == 1:
        return calculate_cosine_similarity(matrix)
    elif method ==2:
        return calculate_pearson_correlation(matrix)
    else:
        raise ValueError("Invalid similarity method. Use \n 1 .'cosine'\n 2 .'pearson'.\n")

display_intro()
method = int(input("Choose similarity method ('cosine' or 'pearson'): \n 1. cosine \n 2. pearson \n").strip().lower())

user_similarity = compute_similarity(user_item_matrix.values, method)

user = int(input("ENTER USER ID (1-500): "))
progress_bar()

def find_similar_users(user_id, user_similarity, top_n=5):
    user_index = user_id - 1  
    similar_users = user_similarity[user_index]
    similar_users_indices = np.argsort(similar_users)[::-1][1:top_n + 1]
    return [index + 1 for index in similar_users_indices]  

def generate_recommendations(user_id, user_similarity, user_item_matrix, top_n=5):
    similar_users = find_similar_users(user_id, user_similarity)
    similar_users_ratings = user_item_matrix.loc[similar_users]
    average_ratings = similar_users_ratings.mean()
    recommended_movies = average_ratings.sort_values(ascending=False).head(top_n)
    return recommended_movies

def evaluate_model(user_id, user_similarity, user_item_matrix, actual_ratings, top_n=5):
    recommendations = generate_recommendations(user_id, user_similarity, user_item_matrix, top_n)
    common_movies = recommendations.index.intersection(actual_ratings.index)
    precision = len(common_movies) / top_n
    recall = len(common_movies) / len(actual_ratings[actual_ratings > 0])
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return precision, recall, f1_score

recommendations = generate_recommendations(user, user_similarity, user_item_matrix)
print(f"Recommended movies for the user {user}:\n{recommendations}")

actual_ratings = user_item_matrix.loc[user]
precision, recall, f1_score = evaluate_model(user, user_similarity, user_item_matrix, actual_ratings)
print(f"Precision for the user {user}: {precision * 100:.2f} /100")
print(f"Recall for the user {user}: {recall * 100:.2f} /100")
print(f"F1 Score for the user {user}: {f1_score * 100:.2f} /100")

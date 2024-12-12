# Movie Recommendation System

## Overview
This project implements a movie recommendation system using collaborative filtering techniques. It calculates user similarities based on ratings and generates personalized movie suggestions. The system supports two similarity measures: cosine similarity and Pearson correlation, making it flexible for different scenarios.

## Features
- **Similarity Calculation**: Computes user similarity using either cosine similarity or Pearson correlation.
- **Personalized Recommendations**: Suggests movies based on the ratings of users with similar preferences.
- **Performance Evaluation**: Measures the system's effectiveness using precision, recall, and F1 score.
- **Interactive User Input**: Allows users to input their ID and view recommendations.

## How to Use

### Prerequisites
Ensure you have Python installed on your system. Additionally, install the required packages:

```bash
pip install pandas numpy scikit-learn
```

### Dataset
The project uses the [MovieLens](https://grouplens.org/datasets/movielens/) dataset. Download the dataset and ensure the following CSV files are available:
- `ratings.csv`
- `movies.csv`

Place these files in the `ml-latest-small` folder within the project directory.

### Running the Code
1. Clone this repository or copy the code into a Python script.
2. Ensure the `display` module (containing `display_intro` and `progress_bar` functions) is available or replace with your implementation.
3. Run the script:

```bash
python recommendation_system.py
```
4. Input a user ID (between 1 and 500) when prompted to receive movie recommendations.

### Switching Similarity Measures
By default, the system uses cosine similarity. To switch to Pearson correlation:

1. Locate the following line in the code:
   ```python
   similarity_measure = 'cosine'  # Default similarity measure
   ```
2. Change `'cosine'` to `'pearson'`:
   ```python
   similarity_measure = 'pearson'
   ```
3. Save the file and re-run the script.

## Code Structure
- **Similarity Calculation**: The `calculate_similarity` function computes user similarity using the selected method.
- **Find Similar Users**: The `find_similar_users` function identifies users with preferences similar to the input user.
- **Generate Recommendations**: The `generate_recommendations` function suggests movies based on similar users' ratings.
- **Evaluate Model**: The `evaluate_model` function calculates precision, recall, and F1 score to assess the system's performance.

## Example Output
```plaintext
Starting...

WELCOME TO MY RECOMMENDATION ENGINE
WITH ALMOST 600 USERS

ENTER USER ID (between 1 and 500): 42

Similar users to the user 42: [123, 87, 56, 98, 45]
Recommended movies for the user 42:
Movie A
Movie B
Movie C
Movie D
Movie E

Precision for the user 42: 80.00 /100
Recall for the user 42: 50.00 /100
F1 Score for the user 42: 61.54 /100
```

## Challenges and Future Enhancements
- **Challenges**:
  - Finding and preparing a suitable dataset.
  - Handling sparse data in the user-item matrix.
- **Future Work**:
  - Add hybrid filtering by combining collaborative and content-based techniques.
  - Optimize for larger datasets and improve scalability.
  - Incorporate contextual factors like time, location, and device type.

## References
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

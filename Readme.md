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

### Running the Code
1. Clone this repository.
2. Ensure the `display` module (containing `display_intro` and `progress_bar` functions) is available or replace with your implementation.
3. Run the script:

```bash
python recommendation_system.py
```
4. Input which 1 or 2 to choose between the two matrics . 
5. Input a user ID (between 1 and 500) when prompted to receive movie recommendations.

### Switching Similarity Measures
Before inputting the user ID it will ask you which matrics you want to use :
- input (1) for **cosine**
- input (2) for **pearson**

## Code Structure
- **Similarity Calculation**: The `calculate_similarity` function computes user similarity using the selected method.
- **Find Similar Users**: The `find_similar_users` function identifies users with preferences similar to the input user.
- **Generate Recommendations**: The `generate_recommendations` function suggests movies based on similar users' ratings.
- **Evaluate Model**: The `evaluate_model` function calculates precision, recall, and F1 score to assess the system's performance.

## Example Output
```plaintext
Starting...
. _______________________________________________________  .
|                                                          |
|                 WELCOME TO MY RECOMMAN-                  |
|                      DATION ENGINE                       |
|                                                          |
|                          BEGIN                           |
|                                                          |
. ________________________________________________________ .
Choose similarity method ('cosine' or 'pearson'):
 1. cosine
 2. pearson
1
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

## References
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Building Recommendation Engines Book](https://unidel.edu.ng/focelibrary/books/Gorakala,%20Suresh%20K%20-%20Building%20recommendation%20engines_%20understand%20your%20data%20and%20user%20preferences%20to%20make%20intelligent,%20accurate,%20and%20profitable%20decisions-Packt%20Publishing%20(2016).pdf)

## What is this ?
This project was developed as part of my university coursework to explore and understand recommendation systems. It represents the culmination of my learning in this area, including implementing collaborative filtering techniques and evaluating their effectiveness. While I recognize that the project has room for improvement, such as expanding features and optimizing performance, it serves as a foundation for deeper exploration. Additionally, through this project, I enhanced my Python skills and learned a new language, R, which I plan to leverage in future endeavors to refine and expand this system.
I hope it serves as a useful tool or learning resource. You're welcome to reach out with feedback or suggestions!

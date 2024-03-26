from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

app = Flask(__name__)

# Example dataset
mock_data = {
    'UserID': [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'RecipeID': [101, 102, 101, 103, 104, 103, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
    'Rating': [5, 3, 4, 5, 3, 3, 1, 3, 4, 1, 5, 4, 2, 5, 4, 3, 5, 4, 3, 4, 2, 5, 4, 3, 2, 4, 5, 3, 4, 2, 5, 3]
}



def get_data_from_db(mock=False):
    if mock:
        return pd.DataFrame(mock_data)
    else:
        # Fetch data from database and return it as dataframe
        return None

def preprocess_data(df):
    """# Preprocess data and return user similarity matrix and user-recipe matrix."""

    # Creating a user-recipe matrix
    user_recipe_matrix = df.pivot_table(index='UserID', columns='RecipeID', values='Rating').fillna(0)

    # Converting the user-recipe matrix to a sparse matrix
    sparse_matrix = csr_matrix(user_recipe_matrix.values)

    # Calculating cosine similarity between users
    user_similarity = cosine_similarity(sparse_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_recipe_matrix.index, columns=user_recipe_matrix.index)
    return user_similarity_df, user_recipe_matrix

def recommend_recipes(user_id, user_similarity_df, user_recipe_matrix, top_n=3):
    similar_users = user_similarity_df.loc[user_id].sort_values(ascending=False)[1:top_n+1].index
    recommended_recipes = pd.Series(dtype='float64')
    for similar_user in similar_users:
        similar_user_ratings = user_recipe_matrix.loc[similar_user]
        recommended_recipes = recommended_recipes.append(similar_user_ratings)

    rated_recipes = user_recipe_matrix.loc[user_id][user_recipe_matrix.loc[user_id] > 0].index
    recommended_recipes = recommended_recipes[~recommended_recipes.index.isin(rated_recipes)]

    return recommended_recipes.groupby(recommended_recipes.index).sum().sort_values(ascending=False).head(top_n)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """Take user_id and top_n as query parameters and return recommended recipes for the user."""
    user_id = request.args.get('user_id', type=int)
    top_n = request.args.get('top_n', default=3, type=int)

    if user_id is None:
        return jsonify({'error': 'User ID is required'}), 400
    
    df = get_data_from_db(mock=True) # Set mock=False when db is ready
    user_similarity_df, user_recipe_matrix = preprocess_data(df)

    if user_id not in user_similarity_df.index:
        return jsonify({'error': 'User ID not found'}), 404

    recommendations = recommend_recipes(user_id, user_similarity_df, user_recipe_matrix, top_n=top_n)
    
    return jsonify(recommendations.to_dict())

if __name__ == '__main__':
    app.run(debug=True)

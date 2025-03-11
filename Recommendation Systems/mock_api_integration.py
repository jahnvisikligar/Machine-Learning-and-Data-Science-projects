import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dot, Dense, Flatten
import numpy as np
import random
from mock_user_api import fetch_user_data
from mock_product_api import fetch_product_data

# Sample data
user_ids = [1, 2, 3, 4, 4, 3, 2, 2, 1, 3]
product_ids = [101, 102, 103, 104, 102, 101, 101, 103, 104, 101]
interactions = [1,0,1,1,1,0,1,1,1,0]  # 1 for interaction (e.g., purchase), 0 for no interaction

# Model definition
user_input = Input(shape=(1,))
product_input = Input(shape=(1,))
user_embedding = Embedding(input_dim=5, output_dim=2)(user_input)
product_embedding = Embedding(input_dim=105, output_dim=2)(product_input)
dot_product = Dot(axes=1)([user_embedding, product_embedding])
flattened = Flatten()(dot_product)
output = Dense(1, activation='sigmoid')(flattened)

model = Model(inputs=[user_input, product_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit([np.array(user_ids), np.array(product_ids)], np.array(interactions), epochs=10)

def get_user_data(user_id):
    return fetch_user_data(user_id)

def get_product_data(product_id):
    return fetch_product_data(product_id)

def get_recommendations(user_id, num_recommendations=5, strategy='A'):
    if strategy == 'A':
        product_ids_range = np.arange(101, 105)  # Strategy A
    elif strategy == 'B':
        product_ids_range = np.arange(101, 105)  # Strategy B can modify this range or add different logic
    else:
        raise ValueError("Unknown strategy. Use 'A' or 'B'.")

    user_id_array = np.array([user_id] * len(product_ids_range))

    # Predict interaction probabilities
    predictions = model.predict([user_id_array, product_ids_range]).flatten()

    # Get top N product indices
    top_indices = predictions.argsort()[-num_recommendations:][::-1]

    # Map product indices back to product_ids
    recommended_product_ids = product_ids_range[top_indices]

    return recommended_product_ids

def track_recommendation(user_id, recommendations, user_feedback):
    # Here you would implement your tracking logic
    # For example, log the recommendations and user feedback to a database or a file
    print(f"Tracking recommendation: User: {user_id}, Recommendations: {recommendations}, Feedback: {user_feedback}")

# Example usage for recommendations
user_id = 2
strategy = random.choice(['A', 'B'])  # Randomly choose a strategy for A/B testing
recommendations = get_recommendations(user_id, strategy=strategy)
print(f"Recommendations for User {user_id}: {recommendations}")

# Simulate user feedback
user_feedback = random.choice(['like', 'dislike'])
track_recommendation(user_id, recommendations, user_feedback)

# Fetch user data and product data using mock APIs
user_data = get_user_data(user_id)
if user_data:
    print(f"User Data for User {user_id}: {user_data}")
else:
    print(f"No data found for User {user_id}")

product_id = recommendations[0]  # Assuming taking the first recommendation for example
product_data = get_product_data(product_id)
if product_data:
    print(f"Product Data for Product {product_id}: {product_data}")
else:
    print(f"No data found for Product {product_id}")

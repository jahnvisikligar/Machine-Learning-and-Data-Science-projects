{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "#Recommendations"
      ],
      "metadata": {
        "id": "6twwq0yS8C16"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Model definition for recommendations\n",
        "\n",
        "*   Model Training\n",
        "*   Getting recommendations\n",
        "\n"
      ],
      "metadata": {
        "id": "lkHwoo048o0v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#model definition\n",
        "\n",
        "import tensorflow as tf\n",
        "from tensorflow.keras.models import Model\n",
        "from tensorflow.keras.layers import Input, Embedding, Dot, Dense, Flatten\n",
        "import numpy as np\n",
        "\n",
        "# Sample data\n",
        "user_ids = [1, 2, 3, 4, 4, 3, 2, 2, 1, 3]\n",
        "product_ids = [101, 102, 103, 104, 102, 101, 101, 103, 104, 101]\n",
        "interactions = [1,0,1,1,1,0,1,1,1,0]  # 1 for interaction (e.g., purchase), 0 for no interaction\n",
        "\n",
        "# Model definition\n",
        "user_input = Input(shape=(1,))\n",
        "product_input = Input(shape=(1,))\n",
        "user_embedding = Embedding(input_dim=5, output_dim=2)(user_input)\n",
        "product_embedding = Embedding(input_dim=105, output_dim=2)(product_input)\n",
        "dot_product = Dot(axes=1)([user_embedding, product_embedding])\n",
        "flattened = Flatten()(dot_product)\n",
        "output = Dense(1, activation='sigmoid')(flattened)\n",
        "\n",
        "model = Model(inputs=[user_input, product_input], outputs=output)\n",
        "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n",
        "\n",
        "# Train the model\n",
        "model.fit([np.array(user_ids), np.array(product_ids)], np.array(interactions), epochs=10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IHUXG25G8GQq",
        "outputId": "37485d7c-c525-4e2e-8eb4-bb5f0b647c99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/10\n",
            "1/1 [==============================] - 1s 815ms/step - loss: 0.6932 - accuracy: 0.6000\n",
            "Epoch 2/10\n",
            "1/1 [==============================] - 0s 11ms/step - loss: 0.6929 - accuracy: 0.6000\n",
            "Epoch 3/10\n",
            "1/1 [==============================] - 0s 12ms/step - loss: 0.6927 - accuracy: 0.7000\n",
            "Epoch 4/10\n",
            "1/1 [==============================] - 0s 11ms/step - loss: 0.6925 - accuracy: 0.7000\n",
            "Epoch 5/10\n",
            "1/1 [==============================] - 0s 12ms/step - loss: 0.6923 - accuracy: 0.7000\n",
            "Epoch 6/10\n",
            "1/1 [==============================] - 0s 11ms/step - loss: 0.6921 - accuracy: 0.7000\n",
            "Epoch 7/10\n",
            "1/1 [==============================] - 0s 11ms/step - loss: 0.6918 - accuracy: 0.7000\n",
            "Epoch 8/10\n",
            "1/1 [==============================] - 0s 12ms/step - loss: 0.6916 - accuracy: 0.7000\n",
            "Epoch 9/10\n",
            "1/1 [==============================] - 0s 10ms/step - loss: 0.6914 - accuracy: 0.7000\n",
            "Epoch 10/10\n",
            "1/1 [==============================] - 0s 11ms/step - loss: 0.6912 - accuracy: 0.7000\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.src.callbacks.History at 0x7888904bfc70>"
            ]
          },
          "metadata": {},
          "execution_count": 69
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def get_recommendations(user_id, num_recommendations=5):\n",
        "    product_ids_range = np.arange(101, 105)  # Adjust the range to be from 101 to 104\n",
        "    user_id_array = np.array([user_id] * len(product_ids_range))\n",
        "\n",
        "    # Predict interaction probabilities\n",
        "    predictions = model.predict([user_id_array, product_ids_range]).flatten()\n",
        "\n",
        "    # Get top N product indices\n",
        "    top_indices = predictions.argsort()[-num_recommendations:][::-1]\n",
        "\n",
        "    # Map product indices back to product_ids\n",
        "    recommended_product_ids = product_ids_range[top_indices]\n",
        "\n",
        "    return recommended_product_ids\n",
        "\n",
        "# Example usage for recommendations\n",
        "user_id = 2\n",
        "recommendations = get_recommendations(user_id)\n",
        "print(f\"Recommendations for User {user_id}: {recommendations}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ptT4n3K08iNa",
        "outputId": "0f1a24d3-a100-4278-e593-96f6eb4361ba"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 0s 69ms/step\n",
            "Recommendations for User 2: [103 102 101 104]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## A/B tests and unit tests"
      ],
      "metadata": {
        "id": "OPN9ZWYt87Am"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_recommendations(user_id, num_recommendations=5, strategy='A'):\n",
        "    if strategy == 'A':\n",
        "        product_ids_range = np.arange(101, 105)  # Strategy A\n",
        "    elif strategy == 'B':\n",
        "        product_ids_range = np.arange(101, 105)  # Strategy B can modify this range or add different logic\n",
        "    else:\n",
        "        raise ValueError(\"Unknown strategy. Use 'A' or 'B'.\")\n",
        "\n",
        "    user_id_array = np.array([user_id] * len(product_ids_range))\n",
        "\n",
        "    # Predict interaction probabilities\n",
        "    predictions = model.predict([user_id_array, product_ids_range]).flatten()\n",
        "\n",
        "    # Get top N product indices\n",
        "    top_indices = predictions.argsort()[-num_recommendations:][::-1]\n",
        "\n",
        "    # Map product indices back to product_ids\n",
        "    recommended_product_ids = product_ids_range[top_indices]\n",
        "\n",
        "    return recommended_product_ids\n",
        "\n",
        "def track_recommendation(user_id, recommendations, user_feedback):\n",
        "    # Here you would implement your tracking logic\n",
        "    # For example, log the recommendations and user feedback to a database or a file\n",
        "    print(f\"Tracking recommendation: User: {user_id}, Recommendations: {recommendations}, Feedback: {user_feedback}\")\n",
        "\n",
        "# Example usage for recommendations\n",
        "user_id = 2\n",
        "strategy = random.choice(['A', 'B'])  # Randomly choose a strategy for A/B testing\n",
        "recommendations = get_recommendations(user_id, strategy=strategy)\n",
        "print(f\"Recommendations for User {user_id}: {recommendations}\")\n",
        "\n",
        "# Simulate user feedback\n",
        "user_feedback = random.choice(['like', 'dislike'])\n",
        "track_recommendation(user_id, recommendations, user_feedback)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "97oq4M9m_1-R",
        "outputId": "40c2087d-09fd-4356-daf1-d166fdd10bc2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 0s 22ms/step\n",
            "Recommendations for User 2: [103 102 101 104]\n",
            "Tracking recommendation: User: 2, Recommendations: [103 102 101 104], Feedback: like\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def run_unit_tests():\n",
        "    \"\"\"\n",
        "    Run unit tests for content generation and recommendation scripts in Google Colab.\n",
        "    \"\"\"\n",
        "    # Example of testing recommendation\n",
        "    user_id = 2\n",
        "    strategy = 'A'  # Adjust strategy as needed for testing\n",
        "\n",
        "    recommendations = get_recommendations(user_id, strategy=strategy)\n",
        "    num_expected_recommendations = 4\n",
        "\n",
        "    assert len(recommendations) == num_expected_recommendations, f\"Expected {num_expected_recommendations} recommendations but got: {len(recommendations)}\"\n",
        "    print(f\"Recommendations for User {user_id}: {recommendations}\")\n",
        "\n",
        "    print(\"Recommendation test passed.\")\n",
        "\n",
        "# Run unit tests\n",
        "run_unit_tests()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6tyztXtM_6Ry",
        "outputId": "d2163f75-1fb6-4e08-97da-b68adab75f08"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 0s 21ms/step\n",
            "Recommendations for User 2: [103 102 101 104]\n",
            "Recommendation test passed.\n"
          ]
        }
      ]
    }
  ]
}

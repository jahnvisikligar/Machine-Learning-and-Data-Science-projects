# MyIndia_Assessment

## Setup and Installation

1. Ensure you have Python 3.7+ installed on your system.
2. Clone the repository or download the following files:
    ```bash
    git repo clone jahnvisikligar/MyIndia_Assessment
    ```
    
   - `content_generation_MI.ipynb`
   - `recommendation_MI.ipynb`
   - `mock_api_integration.py`
   - `mock_product_api.py`
   - `mock_user_api.py`

4. Install the required dependencies:
   ```
   pip install tensorflow numpy openai python-dotenv
   ```
5. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Running the Scripts

### Content Generation

1. Open `content_generation_MI.ipynb` in Jupyter Notebook or Google Colab.
2. Run all cells in the notebook.
3. The script will generate product descriptions based on given attributes.

### Recommendation System

1. Open `recommendation_MI.ipynb` in Jupyter Notebook or Google Colab.
2. Run all cells in the notebook.
3. The script will train a recommendation model and provide product recommendations for users.

        Note: The A/B testing and unit tests have been provided in respective notebooks

### API Integration

1. Run the `mock_api_integration.py` script:

   ```
   python mock_api_integration.py
   ```
2. This script integrates the recommendation model with mock user and product APIs.

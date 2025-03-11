# mock_user_api.py

import random

def fetch_user_data(user_id):
    # Simulate fetching user data from a database or external service
    users_data = {
        1: {'name': 'John Doe', 'age': 30, 'gender': 'male'},
        2: {'name': 'Jane Smith', 'age': 25, 'gender': 'female'},
        3: {'name': 'Mike Johnson', 'age': 35, 'gender': 'male'},
        4: {'name': 'Emily Brown', 'age': 28, 'gender': 'female'}
    }
    
    if user_id in users_data:
        return users_data[user_id]
    else:
        return None

# Example usage
user_id = 2
user_data = fetch_user_data(user_id)
if user_data:
    print(f"User Data for User {user_id}: {user_data}")
else:
    print(f"No data found for User {user_id}")

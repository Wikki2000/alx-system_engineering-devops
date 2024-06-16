#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
Usage: python3 <script_name.py> <employee_id>
"""
import requests
import sys

def fetch_user_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    try:
        # Fetch user information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user = user_response.json()

        # Fetch TODO list for the user
        todos_response = requests.get(f"{base_url}/todos/", params={"userId": employee_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        return user, todos

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def display_todo_progress(user, todos):
    total_tasks = 0
    count_completed_tasks = 0
    list_of_completed_tasks = []


    for task in todos:
        total_tasks += 1
        if task["completed"] == True:
            count_completed_tasks += 1
            list_of_completed_tasks.append(task["title"])

    print(f"User {user['name']} has {total_tasks} tasks in total.")
    print(f"Completed {count_completed_tasks} tasks.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name.py> <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user, todos = fetch_user_data(employee_id)
    display_todo_progress(user, todos)


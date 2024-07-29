#!/usr/bin/python3
"""Fetches and exports to-do list information for a given employee ID to a CSV file.
Usage: python3 <1-export_to_CSV.py> <employer_id>
"""
import csv
import requests
import sys


def fetch_employee_data(employer_id):
    url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch user information
        response = requests.get(f"{url}/users/{employer_id}")
        user = response.json()

        # Fetch employee todo list
        response = requests.get(f"{url}/todos/", params={"userId": employer_id})
        todos = response.json()
        return user, todos

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


def export_to_csv(user, todos):
    user = user["name"]
    user_id = user["id"]
    file_name = f"{user['id']}.csv"

    with open(file_name, w) as csv_file:
         csv_writer = csv.writer(csv_file)

         for todo in todos:
             csv_writer.writerow([employee_id, username, todo['completed'], todo['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name.py> <Employer_id>")
        sys.exit(1)

    employer_id = sys.argv[1]

    user, todos = fetch_employee_data(employer_id)
    print(user)
    print("**************************")
    print(todos)

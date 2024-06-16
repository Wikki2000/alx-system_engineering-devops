
import requests

base_url = "https://jsonplaceholder.typicode.com"
employee_id = 1

response = requests.get(f"{base_url}/todos", params={"userId": employee_id})

print(response.url)  # Output: "https://jsonplaceholder.typicode.com/todos?userId=1"


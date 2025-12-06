Now we automate the process using Python. We will use `requests`, the industry-standard library for synchronous HTTP calls.

## 1. First Request (GET)

- We will fetch data from a public API.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    print("Success!")
    
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
else:
    print(f"Failed with status: {response.status_code}")
```

- Also we can proceed with params like you specify what you are looking for

```python
params = {
    "userId": 1
}

response = requests.get(url, params=params)

data = response.json()
print(f"Found {len(data)} posts for User 1")
```
---

## 2. Sending Data (POST)

To create resources, we send a Dictionary as the json parameter. The library automatically adds the correct headers (`Content-Type: application/json`) and formats the data.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Try to make fun with APIs",
    "body": "Ooooh API without P is AI but not what we are thinking about.",
    "userId": 99
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print("Resource created successfully!")
    print("Server Response:", response.json())
else:
    print("Something went wrong.")
```

---

## 3. Handling Errors

APIs are unpredictable. Always wrap network calls in try/except blocks.

```python
import requests

try:
    response = requests.get("https://httpbin.org/status/404")
    
    response.raise_for_status() 
    
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")
except requests.exceptions.ConnectionError:
    print("Error Connecting to server")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException as err:
    print(f"Something went wrong: {err}")
```

---
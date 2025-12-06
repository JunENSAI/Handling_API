import requests

def api_requests(get: bool, post: bool):

    """ Function to demonstrate GET and POST requests to a sample API."""

    if get:
        url_get = "https://jsonplaceholder.typicode.com/posts/1"

        response_1 = requests.get(url_get)

        if response_1.status_code == 200:
            print("Success!")

            data_1 = response_1.json()
            print(f"Title: {data_1['title']}")
            print(f"Body: {data_1['body']}")
        else:
            print(f"Failed with status: {response_1.status_code}")

    else:
        url_post = "https://jsonplaceholder.typicode.com/posts"

        payload = {
            "title": "Try to make fun with APIs",
            "body": "Ooooh API without P is AI but not what we are thinking about.",
            "userId": 99
        }

        response_2 = requests.post(url_post, json=payload)

        if response_2.status_code == 201:
            print("Resource created successfully!")
            print("Server Response:", response_2.json())
        else:
            print("Something went wrong.")

print(api_requests(get=True, post=False))

print(api_requests(get=False, post=True))
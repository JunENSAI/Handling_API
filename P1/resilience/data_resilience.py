import requests
import json

#--- Example of handling timeouts and connection errors with requests ---

url = "https://httpbin.org/delay/2" 
timeout_seconds = 1.5

try:

    response = requests.get(url, timeout=timeout_seconds)
    response.raise_for_status()
    
    print("Success:", response.json())

except requests.exceptions.Timeout:
    print("Error: The server was too slow. We stopped waiting.")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the internet.")
except requests.exceptions.HTTPError as err:
    print(f"Error: Bad Status Code. {err}")
except requests.exceptions.RequestException as e:
    print(f"Catastrophic error: {e}")


#--- Example of saving JSON data to a file ---

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
        
    print("Data successfully saved to users.json")

except Exception as e:
    print(f"Failed: {e}")
Making the request is easy. The hard part is making your code robust enough to handle the internet's instability and useful enough to save the results.

## 1. Advanced Error Handling
The internet is unreliable. Servers go down, DNS fails, and connections time out. If your script crashes every time the Wi-Fi blinks, it's not production-ready.

We use the `try...except` block specifically looking for `requests` exceptions.

**The Hierarchy of Errors:**

* `requests.exceptions.RequestException`: The base class for all exceptions (catch-all).

* `requests.exceptions.HTTPError`: Specific to status codes (4xx, 5xx).

* `requests.exceptions.ConnectionError`: Network problems (DNS failure, refused connection).

* `requests.exceptions.Timeout`: The server took too long to reply.

---

## 2. Verifying Downloaded Data

Passing malformed data downstream creates cascading failures. Always validate what you download.

```python
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # SAVE TO FILE
    # 'w' = write mode
    # indent=4 makes the file readable for humans (pretty print)
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
        
    print("Data successfully saved to users.json")

except Exception as e:
    print(f"Failed: {e}")
```

### What Should Be Verified?

- The response is valid JSON.

- The structure matches your expectations.

- Critical fields are present.

- Types correspond to your model.

---
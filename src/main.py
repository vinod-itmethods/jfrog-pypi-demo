import requests

def get_status():
    response = requests.get("https://www.google.com")
    return response.status_code

if __name__ == "__main__":
    print(f"Google Status: {get_status()}")

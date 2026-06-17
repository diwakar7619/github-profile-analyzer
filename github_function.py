import requests


def get_github_profile(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(e)
        return None


def get_github_repositories(username):
    try:
        url = f"https://api.github.com/users/{username}/repos"

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(e)

        return None

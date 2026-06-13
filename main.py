from github_function import get_github_profile

username = input("Enter GitHub username: ")

profile = get_github_profile(username)

if profile:
    print("=" * 25)
    print(" GitHub Profile Analyzer ")
    print("=" * 25)

    print(f"Username: {profile['login']}")
    print(f"Name: {profile['name']}")
    print(f"Followers: {profile['followers']}")
    print(f"Following: {profile['following']}")
    print(f"Public Repositories: {profile['public_repos']}")
else:
    print("GitHub user not found.")

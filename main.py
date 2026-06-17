from github_function import get_github_profile, get_github_repositories


username = input("Enter GitHub username: ")

profile = get_github_profile(username)

important_fields = ["login", "name", "followers", "following", "public_repos"]


if profile:
    print("=" * 25)
    print(" GitHub Profile Analyzer ")
    print("=" * 25)

    for key in important_fields:
        print(key, " : ", profile.get(key))

    repos = get_github_repositories(username)
    if repos:
        print(f"Total Repositories: {len(repos)}")
        print("\nRepositories:")
        print("-" * 25)
        for repo in repos:
            print(repo.get("name"))

else:
    print("GitHub user not found.")

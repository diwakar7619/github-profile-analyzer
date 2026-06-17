# GitHub Profile Analyzer

A Python application that fetches and displays GitHub user profile information and public repositories using the GitHub REST API.

## Features

* Search for any GitHub user
* Display profile details:

  * Username
  * Name
  * Followers
  * Following
  * Public Repository Count
* Display all public repositories
* Handle invalid usernames gracefully
* Basic exception handling for network-related errors

## Technologies Used

* Python
* Requests
* GitHub REST API

## Project Structure

```text
github_profile_analyzer/
│
├── main.py
├── github_function.py
├── README.md
└── .venv/
```

## How It Works

1. User enters a GitHub username.
2. The application sends HTTP GET requests to GitHub REST API endpoints.
3. GitHub returns JSON data.
4. JSON data is converted into Python dictionaries and lists.
5. The application displays profile and repository information.

## Example Output

```text
Enter GitHub username: torvalds

=========================
 GitHub Profile Analyzer
=========================
login : torvalds
name : Linus Torvalds
followers : 307740
following : 0
public_repos : 12

Total Repositories: 12

Repositories:
-------------------------
1590A
AudioNoise
GuitarPedal
HunspellColorize
libdc-for-dirk
libgit2
linux
pesconvert
ScrollWheel
subsurface-for-dirk
test-tlb
uemacs
```

## Concepts Practiced

* Functions
* Parameters and Arguments
* Return Values
* REST API Integration
* HTTP GET Requests
* JSON Parsing
* Dictionaries
* Lists
* Loops
* Exception Handling
* Modular Programming

## Installation

Install dependencies:

```bash
pip install requests
```

Run the project:

```bash
python main.py
```

## Learning Outcomes

This project was built to practice working with APIs and strengthen Python fundamentals by using:

* Real-world API data
* JSON responses
* Dictionaries and lists
* Loops and functions
* Exception handling
* Multi-file project structure

## Future Improvements

* Display repository descriptions
* Display star counts
* Sort repositories by popularity
* Export results to CSV
* Add a graphical user interface (GUI)

## Author

Pratham Diwakar

import time
import requests
from cli_app.validators import validate_username, validate_repo_name
from typing import Dict

def fetch_repo_details(username: str, repo_name: str) -> Dict[str, int]:
    """
    Fetches details like branches, stars, and forks from a GitHub repository.
    Implements retry logic in case of non-200 status codes and validates inputs.
    """
    # Validate inputs
    validate_username(username)
    validate_repo_name(repo_name)

    retries = 3
    for attempt in range(retries):
        try:
            # API URL for GitHub
            url = f'https://api.github.com/repos/{username}/{repo_name}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # Get branches
                branches_url = f"https://api.github.com/repos/{username}/{repo_name}/branches"
                branches_response = requests.get(branches_url)
                branches = len(branches_response.json()) if branches_response.status_code == 200 else 0

                stars = data.get('stargazers_count', 0)
                forks = data.get('forks_count', 0)

                return {
                    'username': username,
                    'repo_name': repo_name,
                    'branches': branches,
                    'stars': stars,
                    'forks': forks
                }
            elif response.status_code == 404:
                raise Exception(f"Repository not found: {username}/{repo_name} (404)")
            elif response.status_code == 403:
                raise Exception("API rate limit exceeded or authentication required (403)")
            elif response.status_code == 500:
                raise Exception("GitHub API server error (500)")
            elif response.status_code == 503:
                raise Exception("GitHub API service unavailable (503)")
            else:
                raise Exception(f"GitHub API error: {response.status_code}")

        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)  # Retry delay (can adjust the duration)
            else:
                raise e



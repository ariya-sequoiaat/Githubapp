import pytest
from unittest.mock import patch, MagicMock
from cli_app.git_hub_app import fetch_repo_details

@pytest.fixture
def mock_repo_data():
    return {
        'username': 'test-user',
        'repo_name': 'test_repo',
        'branches': 5,
        'stars': 10,
        'forks': 3
    }

@pytest.fixture
def mock_github_api_response():
    return {
        'stargazers_count': 10,
        'forks_count': 3
    }

# Helper function to handle different status code responses
def mock_github_response(status_code, json_data=None):
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = json_data if json_data else {}
    return response

@patch('cli_app.git_hub_app.requests.get')
def test_fetch_repo_details_success(mock_get, mock_repo_data, mock_github_api_response):
    # Setup mock response for a successful API call (status code 200)
    repo_response = mock_github_response(200, mock_github_api_response)
    branches_response = mock_github_response(200, [{'name': 'branch'} for _ in range(5)])

    def side_effect(*args, **kwargs):
        if 'branches' in args[0]:
            return branches_response
        return repo_response

    mock_get.side_effect = side_effect

    # Call the function
    result = fetch_repo_details(mock_repo_data['username'], mock_repo_data['repo_name'])

    # Verify API calls and results
    assert mock_get.call_count == 2
    assert result['branches'] == 5
    assert result['stars'] == mock_github_api_response['stargazers_count']
    assert result['forks'] == mock_github_api_response['forks_count']

@patch('cli_app.git_hub_app.requests.get')
def test_fetch_repo_details_404(mock_get, mock_repo_data):
    # Setup mock response for a 404 (Not Found) error
    repo_response = mock_github_response(404)
    mock_get.return_value = repo_response

    # Test that the exception is raised for a 404 error
    with pytest.raises(Exception) as exc_info:
        fetch_repo_details(mock_repo_data['username'], mock_repo_data['repo_name'])
    
    assert "Repository not found" in str(exc_info.value)

@patch('cli_app.git_hub_app.requests.get')
def test_fetch_repo_details_403(mock_get, mock_repo_data):
    # Setup mock response for a 403 (Forbidden) error
    repo_response = mock_github_response(403)
    mock_get.return_value = repo_response

    # Test that the exception is raised for a 403 error
    with pytest.raises(Exception) as exc_info:
        fetch_repo_details(mock_repo_data['username'], mock_repo_data['repo_name'])

    assert "API rate limit exceeded" in str(exc_info.value)

@patch('cli_app.git_hub_app.requests.get')
def test_fetch_repo_details_500(mock_get, mock_repo_data):
    # Setup mock response for a 500 (Internal Server Error)
    repo_response = mock_github_response(500)
    mock_get.return_value = repo_response

    # Test that the exception is raised for a 500 error
    with pytest.raises(Exception) as exc_info:
        fetch_repo_details(mock_repo_data['username'], mock_repo_data['repo_name'])

    assert "GitHub API server error" in str(exc_info.value)

@patch('cli_app.git_hub_app.requests.get')
def test_fetch_repo_details_503(mock_get, mock_repo_data):
    # Setup mock response for a 503 (Service Unavailable) error
    repo_response = mock_github_response(503)
    mock_get.return_value = repo_response

    # Test that the exception is raised for a 503 error
    with pytest.raises(Exception) as exc_info:
        fetch_repo_details(mock_repo_data['username'], mock_repo_data['repo_name'])

    assert "GitHub API service unavailable" in str(exc_info.value)


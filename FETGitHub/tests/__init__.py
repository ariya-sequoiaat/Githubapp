import sys
import os
from pathlib import Path

# Assuming cli-app is at the same level as the test folder
cli_app_dir = Path(__file__).parent.parent / 'cli-app'

# Check if cli-app directory exists
if cli_app_dir.exists():
    if str(cli_app_dir) not in sys.path:
        sys.path.append(str(cli_app_dir))
    print(f"cli-app directory added to sys.path: {cli_app_dir}")
else:
    print(f"Error: cli-app directory not found at {cli_app_dir}")
    sys.exit(1)  # Exit if the directory is not found

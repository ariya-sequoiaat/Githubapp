import pytest
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cli_app')))
from cli_app.logger import setup_logger

# Test the logger setup
def test_logger():
    logger = setup_logger()
    
    # Ensure the logger has a handler and the correct level
    assert len(logger.handlers) > 0
    assert logger.level == logging.INFO

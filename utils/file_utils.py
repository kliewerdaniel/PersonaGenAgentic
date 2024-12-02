# utils/file_utils.py

import os
import json
from datetime import datetime

def load_sample_text(filename: str) -> str:
    """
    Load sample text from a file with proper error handling.
    """
    try:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return ""
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            print("Warning: File is empty.")
            return ""
        
        return content
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return ""

def create_backup(filename: str):
    """
    Create a backup of the specified file.
    """
    try:
        if os.path.exists(filename):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f"{filename}.{timestamp}.backup"
            os.rename(filename, backup_filename)
            print(f"Created backup: {backup_filename}")
    except Exception as e:
        print(f"Error creating backup: {str(e)}")

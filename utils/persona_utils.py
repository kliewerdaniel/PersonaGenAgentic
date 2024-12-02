# utils/persona_utils.py

import json
import os
from datetime import datetime
from utils.file_utils import create_backup


def save_persona(persona: dict, persona_file='persona.json') -> bool:
    try:
        if not persona:
            print("Error: Cannot save empty persona.")
            return False
        create_backup(persona_file)
        os.makedirs(os.path.dirname(persona_file) if os.path.dirname(persona_file) else '.', exist_ok=True)
        with open(persona_file, 'w', encoding='utf-8') as f:
            json.dump(persona, f, indent=4, ensure_ascii=False)
        os.chmod(persona_file, 0o600)  # Read and write permissions for the owner only
        print(f"Successfully saved persona to {persona_file}")
        return True
    except Exception as e:
        print(f"Error saving persona: {str(e)}")
        return False


def load_persona(persona_file='persona.json') -> dict:
    try:
        if not os.path.exists(persona_file):
            print(f"No persona file found at {persona_file}")
            return {}
        with open(persona_file, 'r', encoding='utf-8') as f:
            persona = json.load(f)
        if not persona:
            print("Warning: Loaded persona is empty.")
        else:
            print(f"Successfully loaded persona from {persona_file}")
            return persona
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file: {e}")
        return {}
    except Exception as e:
        print(f"Error loading persona: {str(e)}")
        return {}

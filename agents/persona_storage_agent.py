# agents/persona_storage_agent.py

import json
import os
from datetime import datetime
from utils.file_utils import create_backup


class PersonaStorageAgent:
    def __init__(self, persona_file='persona.json'):
        self.persona_file = persona_file

    def save_persona(self, persona: dict) -> bool:
        try:
            if not persona:
                print("Error: Cannot save empty persona.")
                return False
            create_backup(self.persona_file)
            os.makedirs(os.path.dirname(self.persona_file) if os.path.dirname(self.persona_file) else '.', exist_ok=True)
            with open(self.persona_file, 'w', encoding='utf-8') as f:
                json.dump(persona, f, indent=4, ensure_ascii=False)
            os.chmod(self.persona_file, 0o600)  # Read and write permissions for the owner only
            print(f"Successfully saved persona to {self.persona_file}")
            return True
        except Exception as e:
            print(f"Error saving persona: {str(e)}")
            return False

    def load_persona(self) -> dict:
        try:
            if not os.path.exists(self.persona_file):
                print(f"No persona file found at {self.persona_file}")
                return {}
            with open(self.persona_file, 'r', encoding='utf-8') as f:
                persona = json.load(f)
            if not persona:
                print("Warning: Loaded persona is empty.")
            else:
                print(f"Successfully loaded persona from {self.persona_file}")
                return persona
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")
            return {}
        except Exception as e:
            print(f"Error loading persona: {str(e)}")
            return {}

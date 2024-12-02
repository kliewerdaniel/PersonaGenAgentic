# nodes/save_persona_node.py

from nodes.node import Node
from agents.persona_storage_agent import PersonaStorageAgent

class SavePersonaNode(Node):
    def __init__(self, persona_file="persona.json"):
        self.persona_file = persona_file
        self.storage_agent = PersonaStorageAgent(persona_file)

    def run(self, inputs):
        persona = inputs.get("persona")
        if not self.storage_agent.save_persona(persona):
            raise ValueError("Failed to save persona.")
        return {"message": f"Persona saved to {self.persona_file}"}

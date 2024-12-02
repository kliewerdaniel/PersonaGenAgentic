from agents.persona_agent import PersonaAgent
from nodes.node import Node  # Updated import


class GeneratePersonaNode(Node):
    def __init__(self, api_key):
        self.persona_agent = PersonaAgent(api_key)

    def run(self, inputs):
        sample_text = inputs.get("sample_text", "")
        if not sample_text.strip():
            raise ValueError("Sample text is empty.")
        persona = self.persona_agent.generate_persona(sample_text)
        if not persona:
            raise ValueError("Failed to generate persona.")
        return {"persona": persona}

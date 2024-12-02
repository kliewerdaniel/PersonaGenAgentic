# nodes/generate_response_node.py

from nodes.node import Node
from agents.response_agent import ResponseAgent
from agents.persona_storage_agent import PersonaStorageAgent

class GenerateResponseNode(Node):
    def __init__(self, api_key, persona_file="persona.json"):
        self.response_agent = ResponseAgent(api_key)
        self.storage_agent = PersonaStorageAgent(persona_file)

    def run(self, inputs):
        prompt = inputs.get("prompt", "")
        if not prompt.strip():
            raise ValueError("Prompt is empty.")
        persona = self.storage_agent.load_persona()
        if not persona:
            raise ValueError("No persona available. Please generate a persona first.")
        response = self.response_agent.generate_response(persona, prompt)
        return {"response": response}

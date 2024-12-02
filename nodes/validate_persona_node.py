from nodes.node import Node  # Updated import
from agents.validation_agent import ValidationAgent

class ValidatePersonaNode(Node):
    def __init__(self):
        self.validator = ValidationAgent()

    def run(self, inputs):
        persona = inputs.get("persona")
        if not self.validator.validate(persona):
            raise ValueError("Invalid persona JSON.")
        return {"persona": persona}

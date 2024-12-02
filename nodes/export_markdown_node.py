from nodes.node import Node  # Updated import
from agents.export_agent import ExportAgent

class ExportMarkdownNode(Node):
    def __init__(self):
        self.export_agent = ExportAgent()

    def run(self, inputs):
        response = inputs.get("response", "")
        filename = inputs.get("filename", None)
        if not response.strip():
            raise ValueError("Response is empty.")
        success = self.export_agent.export_to_markdown(response, filename)
        if not success:
            raise ValueError("Failed to export response.")
        return {"message": f"Response exported to {filename or 'default filename'}"}

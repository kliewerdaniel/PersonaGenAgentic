# workflows/response_workflow.py

from nodes.generate_response_node import GenerateResponseNode
from nodes.export_markdown_node import ExportMarkdownNode
from workflow import Workflow

def create_response_workflow(api_key, persona_file="persona.json"):
    workflow = Workflow()
    
    generate_response_node = GenerateResponseNode(api_key, persona_file)
    export_markdown_node = ExportMarkdownNode()
    
    workflow.add_node("generate_response", generate_response_node)
    workflow.add_node("export_markdown", export_markdown_node)
    
    workflow.add_edge("generate_response", "export_markdown")
    
    return workflow

# workflows/persona_workflow.py

from nodes.generate_persona_node import GeneratePersonaNode
from nodes.validate_persona_node import ValidatePersonaNode
from nodes.save_persona_node import SavePersonaNode
from workflow import Workflow

def create_persona_workflow(api_key, persona_file="persona.json"):
    workflow = Workflow()
    
    generate_persona_node = GeneratePersonaNode(api_key)
    validate_persona_node = ValidatePersonaNode()
    save_persona_node = SavePersonaNode(persona_file)
    
    workflow.add_node("generate_persona", generate_persona_node)
    workflow.add_node("validate_persona", validate_persona_node)
    workflow.add_node("save_persona", save_persona_node)
    
    workflow.add_edge("generate_persona", "validate_persona")
    workflow.add_edge("validate_persona", "save_persona")
    
    return workflow

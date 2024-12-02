# main.py

import os
from dotenv import load_dotenv
from workflows.persona_workflow import create_persona_workflow
from workflows.response_workflow import create_response_workflow
from utils.input_utils import get_multiline_input

def main():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return

    persona_workflow = create_persona_workflow(api_key)
    response_workflow = create_response_workflow(api_key)

    print("\n=== Enhanced Persona Generator and Responder ===")
    while True:
        print("\nOptions:")
        print("1. Generate Persona")
        print("2. Generate Response")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        if choice == "3":
            break
        
        if choice == "1":
            sample_text = get_multiline_input("\nEnter sample text:")
            inputs = {"sample_text": sample_text}
            try:
                outputs = persona_workflow.run(inputs)
                print(outputs.get("message", "Persona generation completed."))
            except Exception as e:
                print(f"Error: {str(e)}")
        
        elif choice == "2":
            prompt = get_multiline_input("\nEnter your prompt:")
            inputs = {"prompt": prompt}
            try:
                outputs = response_workflow.run(inputs)
                print(outputs.get("message", "Response generation completed."))
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    print("\nThank you for using the Enhanced Persona Generator and Responder!")

if __name__ == "__main__":
    main()

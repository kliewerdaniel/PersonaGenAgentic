# utils/input_utils.py

def get_multiline_input(prompt: str) -> str:
    """
    Get multiline input from user with proper handling.
    """
    print(prompt)
    print("(Press Enter twice to finish)")
    
    lines = []
    try:
        while True:
            line = input()
            if not line and lines and not lines[-1]:
                break
            lines.append(line)
        return '\n'.join(lines[:-1])  # Remove last empty line
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")
        return ""
    except Exception as e:
        print(f"Error getting input: {str(e)}")
        return ""

# agents/export_agent.py

from datetime import datetime
import os

class ExportAgent:
    def export_to_markdown(self, content: str, filename: str = None) -> bool:
        """
        Export the content to a Markdown file with improved error handling.
        """
        try:
            if not content:
                print("Error: Cannot export empty content.")
                return False
            
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"response_{timestamp}.md"
            
            os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Successfully exported response to {filename}")
            return True
        except Exception as e:
            print(f"Error exporting to markdown: {str(e)}")
            return False

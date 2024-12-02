# agents/persona_agent.py

import json
import os
from openai import OpenAI
from utils.file_utils import create_backup

class PersonaAgent:
    def __init__(self, api_key, persona_file='persona.json'):
        self.client = OpenAI(api_key=api_key)
        self.persona_file = persona_file

    def generate_persona(self, sample_text: str) -> dict:
        prompt = (
            "Please analyze the writing style and personality of the given writing sample. "
            "You are a persona generation assistant. Analyze the following text and create a persona profile "
            "that captures the writing style and personality characteristics of the author. "
            "YOU MUST RESPOND WITH A VALID JSON OBJECT ONLY, no other text or analysis. "
            "The response must start with '{' and end with '}' and use the following exact structure:\n\n"
            "{\n"
            "  \"name\": \"[Author/Character Name]\",\n"
            "  \"vocabulary_complexity\": [1-10],\n"
            "  \"sentence_structure\": \"[simple/complex/varied]\",\n"
            "  \"paragraph_organization\": \"[structured/loose/stream-of-consciousness]\",\n"
            "  \"idiom_usage\": [1-10],\n"
            "  \"metaphor_frequency\": [1-10],\n"
            "  \"simile_frequency\": [1-10],\n"
            "  \"tone\": \"[formal/informal/academic/conversational/etc.]\",\n"
            "  \"punctuation_style\": \"[minimal/heavy/unconventional]\",\n"
            "  \"contraction_usage\": [1-10],\n"
            "  \"pronoun_preference\": \"[first-person/third-person/etc.]\",\n"
            "  \"passive_voice_frequency\": [1-10],\n"
            "  \"rhetorical_question_usage\": [1-10],\n"
            "  \"list_usage_tendency\": [1-10],\n"
            "  \"personal_anecdote_inclusion\": [1-10],\n"
            "  \"pop_culture_reference_frequency\": [1-10],\n"
            "  \"technical_jargon_usage\": [1-10],\n"
            "  \"parenthetical_aside_frequency\": [1-10],\n"
            "  \"humor_sarcasm_usage\": [1-10],\n"
            "  \"emotional_expressiveness\": [1-10],\n"
            "  \"emphatic_device_usage\": [1-10],\n"
            "  \"quotation_frequency\": [1-10],\n"
            "  \"analogy_usage\": [1-10],\n"
            "  \"sensory_detail_inclusion\": [1-10],\n"
            "  \"onomatopoeia_usage\": [1-10],\n"
            "  \"alliteration_frequency\": [1-10],\n"
            "  \"word_length_preference\": \"[short/long/varied]\",\n"
            "  \"foreign_phrase_usage\": [1-10],\n"
            "  \"rhetorical_device_usage\": [1-10],\n"
            "  \"statistical_data_usage\": [1-10],\n"
            "  \"personal_opinion_inclusion\": [1-10],\n"
            "  \"transition_usage\": [1-10],\n"
            "  \"reader_question_frequency\": [1-10],\n"
            "  \"imperative_sentence_usage\": [1-10],\n"
            "  \"dialogue_inclusion\": [1-10],\n"
            "  \"regional_dialect_usage\": [1-10],\n"
            "  \"hedging_language_frequency\": [1-10],\n"
            "  \"language_abstraction\": \"[concrete/abstract/mixed]\",\n"
            "  \"personal_belief_inclusion\": [1-10],\n"
            "  \"repetition_usage\": [1-10],\n"
            "  \"subordinate_clause_frequency\": [1-10],\n"
            "  \"verb_type_preference\": \"[active/stative/mixed]\",\n"
            "  \"sensory_imagery_usage\": [1-10],\n"
            "  \"symbolism_usage\": [1-10],\n"
            "  \"digression_frequency\": [1-10],\n"
            "  \"formality_level\": [1-10],\n"
            "  \"reflection_inclusion\": [1-10],\n"
            "  \"irony_usage\": [1-10],\n"
            "  \"neologism_frequency\": [1-10],\n"
            "  \"ellipsis_usage\": [1-10],\n"
            "  \"cultural_reference_inclusion\": [1-10],\n"
            "  \"stream_of_consciousness_usage\": [1-10],\n"
            "\n"
            "  \"psychological_traits\": {\n"
            "    \"openness_to_experience\": [1-10],\n"
            "    \"conscientiousness\": [1-10],\n"
            "    \"extraversion\": [1-10],\n"
            "    \"agreeableness\": [1-10],\n"
            "    \"emotional_stability\": [1-10],\n"
            "    \"dominant_motivations\": \"[achievement/affiliation/power/etc.]\",\n"
            "    \"core_values\": \"[integrity/freedom/knowledge/etc.]\",\n"
            "    \"decision_making_style\": \"[analytical/intuitive/spontaneous/etc.]\",\n"
            "    \"empathy_level\": [1-10],\n"
            "    \"self_confidence\": [1-10],\n"
            "    \"risk_taking_tendency\": [1-10],\n"
            "    \"idealism_vs_realism\": \"[idealistic/realistic/mixed]\",\n"
            "    \"conflict_resolution_style\": \"[assertive/collaborative/avoidant/etc.]\",\n"
            "    \"relationship_orientation\": \"[independent/communal/mixed]\",\n"
            "    \"emotional_response_tendency\": \"[calm/reactive/intense]\",\n"
            "    \"creativity_level\": [1-10]\n"
            "  },\n"
            "\n"
            "  \"age\": \"[age or age range]\",\n"
            "  \"gender\": \"[gender]\",\n"
            "  \"education_level\": \"[highest level of education]\",\n"
            "  \"professional_background\": \"[brief description]\",\n"
            "  \"cultural_background\": \"[brief description]\",\n"
            "  \"primary_language\": \"[language]\",\n"
            "  \"language_fluency\": \"[native/fluent/intermediate/beginner]\",\n"
            "  \"background\": \"[A brief paragraph describing the author's context, major influences, and any other relevant information not captured above]\"\n"
            "}\n\n"
            f"Sample Text:\n{sample_text}"
        )
        payload = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 1
        }
        try:
            response = self.client.chat.completions.create(**payload)
            content = response.choices[0].message.content.strip()

            # Extract and parse JSON
            start_idx = content.find('{')
            end_idx = content.rfind('}') + 1
            if start_idx == -1 or end_idx == 0:
                print("Error: No JSON structure found in response.")
                return {}

            json_str = content[start_idx:end_idx]
            try:
                persona = json.loads(json_str)
                return persona
            except json.JSONDecodeError as e:
                print(f"JSON parsing error: {e}")
                return {}
        except Exception as e:
            print(f"Error during persona generation: {str(e)}")
            return {}

    def save_persona(self, persona: dict) -> bool:
        try:
            if not persona:
                print("Error: Cannot save empty persona.")
                return False
            create_backup(self.persona_file)
            os.makedirs(os.path.dirname(self.persona_file) if os.path.dirname(self.persona_file) else '.', exist_ok=True)
            with open(self.persona_file, 'w', encoding='utf-8') as f:
                json.dump(persona, f, indent=4, ensure_ascii=False)
            os.chmod(self.persona_file, 0o600)  # Read and write permissions for the owner only
            print(f"Successfully saved persona to {self.persona_file}")
            return True
        except Exception as e:
            print(f"Error saving persona: {str(e)}")
            return False

    def load_persona(self) -> dict:
        try:
            if not os.path.exists(self.persona_file):
                print(f"No persona file found at {self.persona_file}")
                return {}
            with open(self.persona_file, 'r', encoding='utf-8') as f:
                persona = json.load(f)
            if not persona:
                print("Warning: Loaded persona is empty.")
            else:
                print(f"Successfully loaded persona from {self.persona_file}")
                return persona
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")
            return {}
        except Exception as e:
            print(f"Error loading persona: {str(e)}")
            return {}

    def format_persona_summary(self, persona: dict) -> str:
        summary = [
            "=== Persona Summary ===",
            f"Name: {persona.get('name', 'Unknown')}",
            f"Writing Style:",
            f"- Tone: {persona.get('tone', 'Not specified')}",
            f"- Vocabulary Complexity: {persona.get('vocabulary_complexity', 'N/A')}/10",
            f"- Sentence Structure: {persona.get('sentence_structure', 'Not specified')}",
            "\nPsychological Profile:",
        ]
        
        psych_traits = persona.get('psychological_traits', {})
        for trait, value in psych_traits.items():
            summary.append(f"- {trait.replace('_', ' ').title()}: {value}")
        
        summary.extend([
            "\nBackground:",
            f"Age: {persona.get('age', 'Not specified')}",
            f"Education: {persona.get('education_level', 'Not specified')}",
            f"Professional Background: {persona.get('professional_background', 'Not specified')}",
            "\nAdditional Context:",
            persona.get('background', 'No additional context provided')
        ])
        
        return '\n'.join(summary)

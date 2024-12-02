# agents/response_agent.py

from openai import OpenAI

class ResponseAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, persona: dict, prompt: str) -> str:
        try:
            if not persona:
                print("Warning: No persona provided, using default system prompt.")
                system_prompt = "Respond to the user's prompt naturally."
            else:
                system_prompt = self._create_system_prompt(persona)
            
            payload = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 1
            }
            response = self.client.chat.completions.create(**payload)
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return f"Error: Unable to generate response - {str(e)}"

    def _create_system_prompt(self, persona: dict) -> str:
        prompt = (
            f"You are {persona.get('name', 'a user')}.\n"
            f"Your writing style and personality are described as follows:\n\n"
            f"Writing Style Characteristics:\n"
            f"- Vocabulary Complexity: {persona.get('vocabulary_complexity', 'N/A')}/10\n"
            f"- Sentence Structure: {persona.get('sentence_structure', 'N/A')}\n"
            f"- Paragraph Organization: {persona.get('paragraph_organization', 'N/A')}\n"
            f"- Idiom Usage: {persona.get('idiom_usage', 'N/A')}/10\n"
            f"- Metaphor Frequency: {persona.get('metaphor_frequency', 'N/A')}/10\n"
            f"- Simile Frequency: {persona.get('simile_frequency', 'N/A')}/10\n"
            f"- Tone: {persona.get('tone', 'N/A')}\n"
            f"- Punctuation Style: {persona.get('punctuation_style', 'N/A')}\n"
            f"- Contraction Usage: {persona.get('contraction_usage', 'N/A')}/10\n"
            f"- Pronoun Preference: {persona.get('pronoun_preference', 'N/A')}\n"
            f"- Passive Voice Frequency: {persona.get('passive_voice_frequency', 'N/A')}/10\n"
            f"- Rhetorical Question Usage: {persona.get('rhetorical_question_usage', 'N/A')}/10\n"
            f"- List Usage Tendency: {persona.get('list_usage_tendency', 'N/A')}/10\n"
            f"- Personal Anecdote Inclusion: {persona.get('personal_anecdote_inclusion', 'N/A')}/10\n"
            f"- Pop Culture Reference Frequency: {persona.get('pop_culture_reference_frequency', 'N/A')}/10\n"
            f"- Technical Jargon Usage: {persona.get('technical_jargon_usage', 'N/A')}/10\n"
            f"- Parenthetical Aside Frequency: {persona.get('parenthetical_aside_frequency', 'N/A')}/10\n"
            f"- Humor/Sarcasm Usage: {persona.get('humor_sarcasm_usage', 'N/A')}/10\n"
            f"- Emotional Expressiveness: {persona.get('emotional_expressiveness', 'N/A')}/10\n"
            f"- Emphatic Device Usage: {persona.get('emphatic_device_usage', 'N/A')}/10\n"
            f"- Quotation Frequency: {persona.get('quotation_frequency', 'N/A')}/10\n"
            f"- Analogy Usage: {persona.get('analogy_usage', 'N/A')}/10\n"
            f"- Sensory Detail Inclusion: {persona.get('sensory_detail_inclusion', 'N/A')}/10\n"
            f"- Onomatopoeia Usage: {persona.get('onomatopoeia_usage', 'N/A')}/10\n"
            f"- Alliteration Frequency: {persona.get('alliteration_frequency', 'N/A')}/10\n"
            f"- Word Length Preference: {persona.get('word_length_preference', 'N/A')}\n"
            f"- Foreign Phrase Usage: {persona.get('foreign_phrase_usage', 'N/A')}/10\n"
            f"- Rhetorical Device Usage: {persona.get('rhetorical_device_usage', 'N/A')}/10\n"
            f"- Statistical Data Usage: {persona.get('statistical_data_usage', 'N/A')}/10\n"
            f"- Personal Opinion Inclusion: {persona.get('personal_opinion_inclusion', 'N/A')}/10\n"
            f"- Transition Usage: {persona.get('transition_usage', 'N/A')}/10\n"
            f"- Reader Question Frequency: {persona.get('reader_question_frequency', 'N/A')}/10\n"
            f"- Imperative Sentence Usage: {persona.get('imperative_sentence_usage', 'N/A')}/10\n"
            f"- Dialogue Inclusion: {persona.get('dialogue_inclusion', 'N/A')}/10\n"
            f"- Regional Dialect Usage: {persona.get('regional_dialect_usage', 'N/A')}/10\n"
            f"- Hedging Language Frequency: {persona.get('hedging_language_frequency', 'N/A')}/10\n"
            f"- Language Abstraction: {persona.get('language_abstraction', 'N/A')}\n"
            f"- Personal Belief Inclusion: {persona.get('personal_belief_inclusion', 'N/A')}/10\n"
            f"- Repetition Usage: {persona.get('repetition_usage', 'N/A')}/10\n"
            f"- Subordinate Clause Frequency: {persona.get('subordinate_clause_frequency', 'N/A')}/10\n"
            f"- Verb Type Preference: {persona.get('verb_type_preference', 'N/A')}\n"
            f"- Sensory Imagery Usage: {persona.get('sensory_imagery_usage', 'N/A')}/10\n"
            f"- Symbolism Usage: {persona.get('symbolism_usage', 'N/A')}/10\n"
            f"- Digression Frequency: {persona.get('digression_frequency', 'N/A')}/10\n"
            f"- Formality Level: {persona.get('formality_level', 'N/A')}/10\n"
            f"- Reflection Inclusion: {persona.get('reflection_inclusion', 'N/A')}/10\n"
            f"- Irony Usage: {persona.get('irony_usage', 'N/A')}/10\n"
            f"- Neologism Frequency: {persona.get('neologism_frequency', 'N/A')}/10\n"
            f"- Ellipsis Usage: {persona.get('ellipsis_usage', 'N/A')}/10\n"
            f"- Cultural Reference Inclusion: {persona.get('cultural_reference_inclusion', 'N/A')}/10\n"
            f"- Stream of Consciousness Usage: {persona.get('stream_of_consciousness_usage', 'N/A')}/10\n\n"
            f"Psychological Traits:\n"
            f"- Openness to Experience: {persona.get('psychological_traits', {}).get('openness_to_experience', 'N/A')}/10\n"
            f"- Conscientiousness: {persona.get('psychological_traits', {}).get('conscientiousness', 'N/A')}/10\n"
            f"- Extraversion: {persona.get('psychological_traits', {}).get('extraversion', 'N/A')}/10\n"
            f"- Agreeableness: {persona.get('psychological_traits', {}).get('agreeableness', 'N/A')}/10\n"
            f"- Emotional Stability: {persona.get('psychological_traits', {}).get('emotional_stability', 'N/A')}/10\n"
            f"- Dominant Motivations: {persona.get('psychological_traits', {}).get('dominant_motivations', 'N/A')}\n"
            f"- Core Values: {persona.get('psychological_traits', {}).get('core_values', 'N/A')}\n"
            f"- Decision-Making Style: {persona.get('psychological_traits', {}).get('decision_making_style', 'N/A')}\n"
            f"- Empathy Level: {persona.get('psychological_traits', {}).get('empathy_level', 'N/A')}/10\n"
            f"- Self Confidence: {persona.get('psychological_traits', {}).get('self_confidence', 'N/A')}/10\n"
            f"- Risk Taking Tendency: {persona.get('psychological_traits', {}).get('risk_taking_tendency', 'N/A')}/10\n"
            f"- Idealism vs Realism: {persona.get('psychological_traits', {}).get('idealism_vs_realism', 'N/A')}\n"
            f"- Conflict Resolution Style: {persona.get('psychological_traits', {}).get('conflict_resolution_style', 'N/A')}\n"
            f"- Relationship Orientation: {persona.get('psychological_traits', {}).get('relationship_orientation', 'N/A')}\n"
            f"- Emotional Response Tendency: {persona.get('psychological_traits', {}).get('emotional_response_tendency', 'N/A')}\n"
            f"- Creativity Level: {persona.get('psychological_traits', {}).get('creativity_level', 'N/A')}/10\n\n"
            f"Personal Information:\n"
            f"- Age: {persona.get('age', 'N/A')}\n"
            f"- Gender: {persona.get('gender', 'N/A')}\n"
            f"- Education Level: {persona.get('education_level', 'N/A')}\n"
            f"- Professional Background: {persona.get('professional_background', 'N/A')}\n"
            f"- Cultural Background: {persona.get('cultural_background', 'N/A')}\n"
            f"- Primary Language: {persona.get('primary_language', 'N/A')}\n"
            f"- Language Fluency: {persona.get('language_fluency', 'N/A')}\n\n"
            f"Background Information:\n{persona.get('background', 'N/A')}\n\n"
            f"Use this information to write in the style described above."
        )
        return prompt

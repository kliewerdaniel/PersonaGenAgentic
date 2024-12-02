# agents/validation_agent.py

class ValidationAgent:
    def validate(self, persona: dict) -> bool:
        """
        Validate the structure and content of a persona dictionary.
        Returns True if valid, False otherwise.
        """
        required_fields = [
            'name',
            'vocabulary_complexity',
            'sentence_structure',
            'tone',
            'psychological_traits'
        ]
        
        try:
            # Check for required fields
            for field in required_fields:
                if field not in persona:
                    print(f"Missing required field: {field}")
                    return False
            
            # Validate numeric values are within range
            numeric_fields = [
                'vocabulary_complexity',
                'idiom_usage',
                'metaphor_frequency',
                'simile_frequency',
                'contraction_usage',
                'passive_voice_frequency',
                'rhetorical_question_usage',
                'list_usage_tendency',
                'personal_anecdote_inclusion',
                'pop_culture_reference_frequency',
                'technical_jargon_usage',
                'parenthetical_aside_frequency',
                'humor_sarcasm_usage',
                'emotional_expressiveness',
                'emphatic_device_usage',
                'quotation_frequency',
                'analogy_usage',
                'sensory_detail_inclusion',
                'onomatopoeia_usage',
                'alliteration_frequency',
                'foreign_phrase_usage',
                'rhetorical_device_usage',
                'statistical_data_usage',
                'personal_opinion_inclusion',
                'transition_usage',
                'reader_question_frequency',
                'imperative_sentence_usage',
                'dialogue_inclusion',
                'regional_dialect_usage',
                'hedging_language_frequency',
                'personal_belief_inclusion',
                'repetition_usage',
                'subordinate_clause_frequency',
                'sensory_imagery_usage',
                'symbolism_usage',
                'digression_frequency',
                'formality_level',
                'reflection_inclusion',
                'irony_usage',
                'neologism_frequency',
                'ellipsis_usage',
                'cultural_reference_inclusion',
                'stream_of_consciousness_usage'
            ]
            
            for field in numeric_fields:
                if field in persona:
                    value = persona[field]
                    if not isinstance(value, (int, float)) or not (1 <= value <= 10):
                        print(f"Invalid value for {field}: must be number between 1-10.")
                        return False
            
            # Validate psychological traits
            psych_traits = persona.get('psychological_traits', {})
            if not isinstance(psych_traits, dict):
                print("psychological_traits must be a dictionary.")
                return False
            
            required_psych_traits = [
                'openness_to_experience',
                'conscientiousness',
                'extraversion',
                'agreeableness',
                'emotional_stability'
            ]
            
            for trait in required_psych_traits:
                if trait not in psych_traits:
                    print(f"Missing psychological trait: {trait}")
                    return False
                value = psych_traits[trait]
                if not isinstance(value, (int, float)) or not (1 <= value <= 10):
                    print(f"Invalid value for psychological trait {trait}: must be number between 1-10.")
                    return False
            
            return True
        
        except Exception as e:
            print(f"Error validating persona: {str(e)}")
            return False

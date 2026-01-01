import os
from reflex_prompt.templates.meta_prompts import INIT_PROMPT_GEN, MUTATION_PROMPT

class Generator:
    def __init__(self, model_client=None):
        """
        model_client: A function that takes a string prompt and returns a string response.
                      If None, looks for a default client setup.
        """
        self.model_client = model_client or self._default_client
        
    def _default_client(self, prompt):
        # Placeholder for actual LLM call
        # In a real library, this might use OpenAI/Anthropic/Gemini SDKs
        # For now, we'll raise an error if not provided
        raise ValueError("No model_client provided and default client not configured.")

    def generate_initial_prompt(self, task_description, samples):
        # Format samples for the prompt
        samples_str = "\n".join([f"- {s}" for s in samples[:5]]) # Take first 5 for brevity in meta-prompt
        
        prompt_input = INIT_PROMPT_GEN.format(
            task_description=task_description,
            samples=samples_str
        )
        
        return self.model_client(prompt_input)

    def mutate_prompt(self, current_prompt, feedback):
        prompt_input = MUTATION_PROMPT.format(
            current_prompt=current_prompt,
            feedback=feedback
        )
        return self.model_client(prompt_input)

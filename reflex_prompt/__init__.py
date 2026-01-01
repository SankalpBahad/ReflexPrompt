from reflex_prompt.core.ge_loop import GEPALoop
from reflex_prompt.interface.cli import CLIInterface

class ReflexPrompt:
    def __init__(self, task_description, samples, model=None):
        """
        task_description: str
        samples: list of strings
        model: optional callable (prompt -> response)
        """
        self.task_description = task_description
        self.samples = samples
        self.model = model
        
        # Initialize components
        self.interface = CLIInterface()
        self.loop = GEPALoop(
            task_name=task_description, 
            samples=samples, 
            model_client=model, 
            interface=self.interface
        )

    def run(self, iterations=5):
        best_prompt = self.loop.run(iterations=iterations)
        self.interface.show_winner(best_prompt)
        return best_prompt

import random
from reflex_prompt.core.generator import Generator
from reflex_prompt.core.scorer import Scorer

class GEPALoop:
    def __init__(self, task_name, samples, model_client, interface):
        self.task_name = task_name
        self.samples = samples
        self.interface = interface
        self.generator = Generator(model_client)
        self.scorer = Scorer(model_client)
        self.best_prompt = None

    def run(self, iterations=5):
        # 1. Bootstrapping
        if not self.best_prompt:
            print("Bootstrapping initial prompt...")
            self.best_prompt = self.generator.generate_initial_prompt(self.task_name, self.samples)

        # 2. Loop
        for i in range(iterations):
            # Select a random sample for this round
            # In a real app, we might cycle through them
            sample = random.choice(self.samples)
            
            # Run Current Best
            output_best = self.scorer.run_batch(self.best_prompt, [sample])[0]
            
            # Ask Human
            action, feedback = self.interface.get_feedback(sample, self.best_prompt, output_best)
            
            if action == "good":
                continue # Keep going
            
            elif action == "critique":
                # User found a flaw. Mutate!
                print("Mutating based on feedback...")
                candidate_prompt = self.generator.mutate_prompt(self.best_prompt, feedback)
                
                # Verify Candidate on SAME sample
                output_candidate = self.scorer.run_batch(candidate_prompt, [sample])[0]
                
                # Duel!
                duel_action, duel_feedback = self.interface.get_feedback(
                    sample, 
                    self.best_prompt, output_best,
                    candidate_prompt, output_candidate
                )
                
                if duel_action == "switch_to_b":
                    self.best_prompt = candidate_prompt
                    print("New Best Prompt Discovered!")
                elif duel_action == "keep_a":
                    print("Mutation rejected. Keeping original.")
                # If both bad, we keep original for now and maybe try again later
                
        return self.best_prompt

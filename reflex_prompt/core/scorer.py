class Scorer:
    def __init__(self, model_client):
        self.model_client = model_client

    def run_batch(self, prompt, samples):
        """
        Runs the prompt on a list of samples.
        Returns a list of outputs.
        """
        outputs = []
        for sample in samples:
            # Construct the actual input to the model
            # We assume the prompt is a system prompt or instruction
            # and the sample is the user input.
            full_input = f"{prompt}\n\nInput: {sample}"
            output = self.model_client(full_input)
            outputs.append(output)
        return outputs

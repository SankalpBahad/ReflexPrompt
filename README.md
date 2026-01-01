# Human GEPA Library

This library implements a Human-in-the-loop Genetic-Pareto optimization for prompt engineering.

## Installation

Ensure you have the required dependencies:
```bash
pip install rich
```

## Usage

```python
from reflex_prompt import ReflexPrompt

# 1. Define your LLM client wrapper
def my_llm_client(prompt_text):
    # Call OpenAI, Anthropic, or Gemini here
    # return client.chat.completions.create(...)
    return "Mock Response"

# 2. Setup the optimizer
optimizer = ReflexPrompt(
    task_description="Extract medicines from clinical notes",
    samples=[
        "Patient took 50mg Sertraline daily.",
        "Prescribed Ibuprofen as needed."
    ],
    model=my_llm_client
)

# 3. Run the interactive optimization loop
# This will launch a CLI where you can review outputs and provide feedback.
best_prompt = optimizer.run(iterations=5)

print("Final Optimized Prompt:")
print(best_prompt)
```

## How it works

1.  **Bootstrapping**: Generates an initial prompt `V0` based on your samples.
2.  **Evaluation**: Runs the prompt on a sample.
3.  **Feedback**: Shows you the Input and Output. You say "Good" or "Bad".
4.  **Mutation**: If "Bad", it asks for critique and generates a `Candidate` prompt.
5.  **Selection**: It shows you `V0` output vs `Candidate` output. You pick the winner.
6.  **Iteration**: The winner becomes the new baseline.

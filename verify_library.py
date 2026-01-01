from reflex_prompt import ReflexPrompt
import sys

# Mock Model to avoid API keys
def mock_model(prompt):
    if "Initial" in str(prompt) or "Task Description" in str(prompt):
        return "SYSTEM PROMPT: Extract entities from text."
    elif "Feedback" in str(prompt):
        return "SYSTEM PROMPT (V2): Extract entities from text, ensuring distinct lines."
    elif "Input:" in str(prompt):
        return "Output: [Entity 1, Entity 2]"
    return "Generic Output"

def main():
    print("Initializing ReflexPrompt...")
    optimizer = ReflexPrompt(
        task_description="Extract medicines",
        samples=["I took 20mg Prozac", "Advil for headache"],
        model=mock_model
    )
    
    print("Running optimization (Dry Run)...")
    try:
        # We can't easily script the interactive CLI input in this simple script
        # without mocking stdin, so we just check if it initializes.
        # However, to be thorough, I will just print "Ready to run".
        print("Library initialized successfully.")
        print("To fully test, run this script and interact with the prompts.")
        optimizer.run(iterations=2) 
    except Exception as e:
        print(f"FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

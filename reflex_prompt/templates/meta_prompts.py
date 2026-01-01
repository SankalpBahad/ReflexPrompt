
INIT_PROMPT_GEN = """
You are an expert prompt engineer. Your goal is to write a high-quality system prompt for an LLM to perform a specific task.

Task Description: {task_description}

Here are some examples of the inputs and the nature of the task:
{samples}

Based on this, write a concise but comprehensive system prompt that would instruct an LLM to handle these inputs correctly. 
Do not include any "Here is the prompt" text, just output the prompt itself.
The prompt should be general enough to handle unseen examples of similar nature.
"""

MUTATION_PROMPT = """
You are an expert prompt engineer.
You are given a Current Prompt and some Feedback on how it performed on specific examples.
Your goal is to rewrite the Current Prompt to address the feedback while maintaining its performance on other aspects.

Current Prompt:
{current_prompt}

Feedback/Critique from User:
{feedback}

Please write the NEW, IMPROVED prompt. Do not output any explanations, just the prompt.
"""

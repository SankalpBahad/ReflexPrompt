from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.layout import Layout
from rich import print as rprint

class CLIInterface:
    def __init__(self):
        self.console = Console()

    def get_feedback(self, sample, prompt_a, output_a, prompt_b=None, output_b=None):
        """
        Presents one or two options to the user and gets feedback.
        """
        self.console.clear()
        self.console.rule("[bold blue]Human GEPA Feedback Loop[/bold blue]")
        
        # Display Input
        self.console.print(Panel(sample, title="[bold]Input Sample[/bold]", expand=False))

        # Display Option A
        self.console.print(Panel(output_a, title="[bold green]Option A (Current Best)[/bold green]", expand=False))

        if output_b:
            self.console.print(Panel(output_b, title="[bold yellow]Option B (Candidate)[/bold yellow]", expand=False))
            
            choices = ["a", "b", "both_bad", "skip"]
            choice = Prompt.ask("Which is better?", choices=choices, default="a")
            
            if choice == "a":
                feedback = Prompt.ask("Why is A better? (Optional)", default="")
                return "keep_a", feedback
            elif choice == "b":
                feedback = Prompt.ask("Why is B better? (Optional)", default="")
                return "switch_to_b", feedback
            elif choice == "both_bad":
                critique = Prompt.ask("What is wrong with both?", default="Incorrect output")
                return "critique", critique
            else:
                return "skip", None
        else:
            # Single option review
            valid = Prompt.ask("Is this correct?", choices=["y", "n"], default="y")
            if valid == "n":
                critique = Prompt.ask("What is the issue?")
                return "critique", critique
            return "good", None

    def show_winner(self, prompt, score=None):
        self.console.clear()
        self.console.rule("[bold green]Optimization Complete![/bold green]")
        self.console.print(Panel(prompt, title="[bold]Optimized Prompt[/bold]"))

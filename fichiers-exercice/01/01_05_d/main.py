import os
import pprint
import dotenv
from colorama import Fore, Style
from pprint import pprint
from rich.console import Console # type: ignore

from openai import OpenAI

dotenv.load_dotenv()

 
console = Console()
console.rule("[bold blue]Demos - GitHub Models[/bold blue]")


# Get GitHub token from environment variable
github_token = os.getenv("GITHUB_TOKEN")
if not github_token:
    raise ValueError(
        "GITHUB_TOKEN environment variable is not set. "
        "Please set it with: export GITHUB_TOKEN='your_token_here'"
    )

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=github_token,
    default_query={
        "api-version": "2024-08-01-preview",
    },
)

messages = []

def main():
    print(Style.BRIGHT + "//==============*****[GitHub Models]*****===============//" + Style.RESET_ALL)
    print(Fore.CYAN +  "\n-Taper votre question\n–Taper 'quit' pour sortir.\n" + Style.RESET_ALL)
     
    while True:
        user_input = input("Vous: ")

        if user_input.lower() in ("quit", "exit", "q"):
            print(Style.BRIGHT + Fore.CYAN + "Assistant: À bientôt 👋" + Style.RESET_ALL)
            break

        messages.append({"role": "user", "content": user_input})

        try:
            pass
            
        except Exception as e:
            print(e)
            continue
    
if __name__ == "__main__":
    main()
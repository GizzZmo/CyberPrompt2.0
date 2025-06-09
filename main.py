# cyberprompt/main.py

from .core import CyberPromptCore
from .utils import print_welcome_message, print_goodbye_message

def main():
    """
    The main entry point for the CyberPrompt 2.0 command-line interface.
    """
    print_welcome_message()
    core = CyberPromptCore()

    while True:
        try:
            prompt = input(">>> Your prompt: ")
            if prompt.lower() in ["exit", "quit"]:
                break

            response = core.generate_response(prompt)
            print("\n✅ AI Response:\n")
            print(response)
            print("-" * 50)

        except KeyboardInterrupt:
            break

    print_goodbye_message()

if __name__ == "__main__":
    main()

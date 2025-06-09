# cyberprompt/utils.py

import time

def print_welcome_message():
    """
    Prints a welcome message to the user when the application starts.
    """
    print("=" * 50)
    print("🚀 Welcome to CyberPrompt 2.0!")
    print("   Type your prompt below and press Enter to get a response.")
    print("   Type 'exit' or 'quit' to end the session.")
    print("=" * 50)

def print_goodbye_message():
    """
    Prints a goodbye message to the user when the application exits.
    """
    print("\n👋 Thank you for using CyberPrompt 2.0!")
    print("   See you next time!")

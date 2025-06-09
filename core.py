# cyberprompt/core.py

import time

class CyberPromptCore:
    """
    The core of the CyberPrompt 2.0 application. This class handles the
    interaction with the AI model, including prompt processing and response
    generation.
    """

    def __init__(self, recursion_depth=3, creativity=0.7):
        """
        Initializes the CyberPromptCore.

        Args:
            recursion_depth (int): The number of times the AI will refine its
                own response.
            creativity (float): A value between 0 and 1 that controls the
                randomness of the AI's output.
        """
        self.recursion_depth = recursion_depth
        self.creativity = creativity
        self.history = []

    def generate_response(self, prompt):
        """
        Generates a response from the AI model based on the given prompt.

        Args:
            prompt (str): The user's input prompt.

        Returns:
            str: The AI-generated response.
        """
        print("🤖 AI is thinking...")
        for i in range(self.recursion_depth):
            print(f"   -> Refining response (level {i + 1}/{self.recursion_depth})...")
            time.sleep(0.5)  # Simulate AI thinking time

        # In a real application, this would be a call to an actual AI model.
        # For this example, we'll just return a mock response.
        response = f"This is a mock AI response to your prompt: '{prompt}'\n" \
                   f"(Recursion Depth: {self.recursion_depth}, Creativity: {self.creativity})"

        # Add the interaction to the history
        self.history.append({"prompt": prompt, "response": response})

        return response

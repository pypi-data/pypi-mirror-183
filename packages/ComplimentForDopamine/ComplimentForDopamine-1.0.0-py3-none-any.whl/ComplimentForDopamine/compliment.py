import random


class ComplimentList:
    """
    A class that stores a list of compliments.
    """

    def __init__(self):
        self.compliments = [
            "you are an amazing person",
            "you have a great sense of humor",
            "you are intelligent and articulate",
            "you have a kind and compassionate heart",
            "you are a talented and creative individual",
            'you are excellent',
            'You are doing a great job',
            'You are kind.',
            'I admire your bravery to speak up about things that matter to you.',
            'Your confidence inspires me to be more confident in myself.',
            'I appreciate your honesty.',
            'You are a thoughtful planner, and are good at being proactive.',
            'Your routines are inspiring to me.',
            'I admire your ability to set boundaries and take care of yourself.',
            'Your jokes always brighten my day! I appreciate your sharp sense of humor.',
            'You are a wonderful listener.I always feel understood by you.',
            'I have such good memories of all the times we’ve been able to share together; I’m always looking forward to spending time with you.'
        ]


class ComplimentGenerator(ComplimentList):
    def __init__(self, name):
        """
        Initialize a ComplimentGenerator instance with a given name.

        Parameters:
        - name (str): The name for which to generate compliments.
        """
        super().__init__()  # initialize the ComplimentList superclass
        self.name = name

    def generate_compliment(self):
        """
        Generate a random compliment for the name passed to the constructor.

        Returns:
        - str: A string containing the name and a randomly chosen compliment.
        """
        compliment = random.choice(self.compliments)
        return f"{self.name}, {compliment}!"


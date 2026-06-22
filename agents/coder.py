class CoderAgent:
    def __init__(self):
        self.attempts = 0

    def write_code(self, plan, feedback=None):
        self.attempts += 1
        print(f"💻 CODER: Writing code (Attempt {self.attempts})...")
        
        if feedback:
            print(f"💻 CODER: Adjusting based on feedback: {feedback}")
            # Simulated fix
            return "def webhook_listener():\n    import json\n    return 'Success, payload secured!'"
            
        # Simulated initial buggy code (to trigger the loop)
        return "def webhook_listener():\n    print('Listening...')\n    # forgot to import json"

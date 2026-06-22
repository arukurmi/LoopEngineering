class PlannerAgent:
    def create_plan(self, goal):
        print(f"🗓️ PLANNER: Analyzing goal -> '{goal}'")
        print("🗓️ PLANNER: Reading payment API docs... done.")
        plan = [
            "Step 1: Import requests and json.",
            "Step 2: Create a webhook listener function.",
            "Step 3: Add error handling for invalid payloads."
        ]
        return plan

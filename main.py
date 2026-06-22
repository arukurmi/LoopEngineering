from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.reviewer import ReviewerAgent
from agents.git_operator import GitOperatorAgent
import time

def run_loop():
    print("🔄 STARTING LOOP ENGINEERING PIPELINE...\n")
    
    # Initialize Agents
    planner = PlannerAgent()
    coder = CoderAgent()
    reviewer = ReviewerAgent()
    git_operator = GitOperatorAgent()

    target_goal = "Build a secure payment webhook listener"
    
    # Node 1: Plan
    build_plan = planner.create_plan(target_goal)
    time.sleep(1)
    
    # Node 2 & 3: The Self-Healing Loop
    is_approved = False
    feedback = None
    final_code = ""
    
    while not is_approved:
        # Coder writes/rewrites
        final_code = coder.write_code(build_plan, feedback)
        time.sleep(1)
        
        # Reviewer checks
        is_approved, feedback = reviewer.review(final_code)
        time.sleep(1)
        print("-" * 40)

    # Node 4: Save and Deploy
    filename = "generated_webhook.py"
    with open(filename, "w") as f:
        f.write(final_code)
        
    print(f"💾 SYSTEM: Code saved to {filename}")
    git_operator.push_to_github(filename)
    
    print("\n✅ PIPELINE COMPLETE. No human intervention required.")

if __name__ == "__main__":
    run_loop()

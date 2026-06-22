class ReviewerAgent:
    def review(self, code):
        print("🕵️ REVIEWER: Inspecting code for errors and security flaws...")
        
        # Simulated code review logic
        if "import json" not in code:
            error_msg = "FAILED: Missing 'json' module import. You cannot parse payment payloads without it."
            print(f"🕵️ REVIEWER: ❌ {error_msg}")
            return False, error_msg
            
        print("🕵️ REVIEWER: ✅ PASSED. Code is clean and secure.")
        return True, "Looks good."

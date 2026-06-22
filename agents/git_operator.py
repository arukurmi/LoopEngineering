import subprocess

class GitOperatorAgent:
    def push_to_github(self, file_name):
        print(f"🚀 GIT OPERATOR: Committing and pushing {file_name} to GitHub...")
        try:
            # These are the actual terminal commands the agent runs
            subprocess.run(["git", "add", file_name], check=True)
            subprocess.run(["git", "commit", "-m", "Automated commit by Loop Engineer"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("🚀 GIT OPERATOR: Successfully pushed to production!")
        except Exception as e:
            print(f"🚀 GIT OPERATOR: ⚠️ Push skipped (Not in a git repo or no changes).")

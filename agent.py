
class WalletAgent:
    def __init__(self):
        self.name = "Wallet Master"
        self.tasks = []

    def think(self, task):
        print(f"Task received: {task}")
        self.tasks.append(task)
        return self.plan(task)

    def plan(self, task):
        return {
            "task": task,
            "steps": [
                "Analyze request",
                "Check project files",
                "Prepare implementation",
                "Test implementation",
                "Report results"
            ]
        }

    def run(self, task):
        result = self.think(task)
        print("\nExecution plan:")
        for i, step in enumerate(result["steps"], 1):
            print(f"{i}. {step}")


if __name__ == "__main__":
    agent = WalletAgent()
    agent.run("Build a multi-chain wallet dashboard")

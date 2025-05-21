class DummyAutomator:
    def can_handle(self, step):
        # Accepts any step for demo
        return True

    def handle(self, step):
        return f"Automated step: {step}"

class AutomationMesh:
    def __init__(self):
        self.automators = [DummyAutomator()]

    def register(self, automator):
        self.automators.append(automator)

    def execute(self, plan):
        results = []
        for step in plan:
            for automator in self.automators:
                if automator.can_handle(step):
                    results.append(automator.handle(step))
                    break
        return results
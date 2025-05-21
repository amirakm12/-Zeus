class SecurityCore:
    def __init__(self):
        self.policies = {}

    def audit(self, orchestrator):
        # Always returns empty for demo
        return []

    def enforce_policy(self, action):
        return "Policy enforced"
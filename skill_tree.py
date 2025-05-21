from skills.todo_skill import ToDoSkill

class DummySkill:
    def execute(self, **params):
        return f"Executed dummy skill with params: {params}"

class SkillTree:
    def __init__(self):
        self.skills = {
            "dummy_skill": DummySkill(),
            "todo_skill": ToDoSkill()
        }

    def register_skill(self, name, skill_module):
        self.skills[name] = skill_module

    def plan(self, intent, context):
        # Very basic intent parsing for "todo" actions
        intent_lower = intent.lower()
        plan = []
        if "add todo" in intent_lower or "new todo" in intent_lower or "create todo" in intent_lower:
            text = intent.split(":", 1)[-1].strip() if ":" in intent else intent
            plan.append({"skill": "todo_skill", "action": "add", "params": {"text": text}})
        elif "list todo" in intent_lower or "show todo" in intent_lower:
            plan.append({"skill": "todo_skill", "action": "list", "params": {}})
        elif "mark done" in intent_lower or "complete todo" in intent_lower:
            # Extract id (for demo, assumes the last word is the id)
            try:
                todo_id = int(intent_lower.split()[-1])
                plan.append({"skill": "todo_skill", "action": "done", "params": {"todo_id": todo_id}})
            except:
                pass
        elif "remove todo" in intent_lower or "delete todo" in intent_lower:
            try:
                todo_id = int(intent_lower.split()[-1])
                plan.append({"skill": "todo_skill", "action": "remove", "params": {"todo_id": todo_id}})
            except:
                pass
        else:
            plan.append({"skill": "dummy_skill", "params": {"intent": intent, "context": context}})
        return plan

    def execute(self, plan):
        results = []
        for step in plan:
            skill = self.skills.get(step["skill"])
            action = step.get("action")
            params = step.get("params", {})
            if skill:
                if step["skill"] == "todo_skill":
                    if action == "add":
                        results.append(skill.add_todo(**params))
                    elif action == "list":
                        results.append(skill.list_todos())
                    elif action == "done":
                        skill.mark_done(**params)
                        results.append(f"Marked todo {params.get('todo_id')} as done.")
                    elif action == "remove":
                        skill.remove_todo(**params)
                        results.append(f"Removed todo {params.get('todo_id')}.")
                else:
                    results.append(skill.execute(**params))
        return results
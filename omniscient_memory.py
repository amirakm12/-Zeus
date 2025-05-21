class OmniscientMemory:
    def __init__(self):
        self.knowledge_graph = {}

    def store(self, interaction):
        key = hash(str(interaction))
        self.knowledge_graph[key] = interaction

    def retrieve(self, query):
        # Return all stored memory for now
        return list(self.knowledge_graph.values())
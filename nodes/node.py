class Node:
    def run(self, inputs):
        """
        Base Node class with a run method.
        All custom nodes should inherit from this class and override the run method.
        """
        raise NotImplementedError("The 'run' method must be implemented by subclasses.")

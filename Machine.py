class Machine:

    def __init__(self, reward):
        self.reward = reward

    def __str__(self):
      return f"Reward={self.reward}"
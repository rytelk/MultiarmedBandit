class Machine:

    def __init__(self, reward, rewardProbability):
        self.reward = reward
        self.rewardProbability = rewardProbability

    def __str__(self):
      return f"Reward={self.reward}, Probability={self.rewardProbability:.2f}"
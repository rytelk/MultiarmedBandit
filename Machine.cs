using System;

namespace MultiArmedBanditProblem.Domain
{
    class Machine
    {
        public double Reward { get; set; } = 0.0;
        public double Probability { get; set; } = 0.0;
        public int MaxReward = 1000;

        public Machine()
        {
            Random r = new Random(0);

            Reward = r.Next(MaxReward);
            Probability = r.Next((int) 1e6) / 1e6;
        }

        public Machine(double reward, double probability)
        {
            Reward = reward;
            Probability = probability;
        }

        public override string ToString()
        {
            return $"Reward={Reward,3}, Probability={Probability,6:P2}";
        }
    }
}

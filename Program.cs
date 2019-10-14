using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MultiArmedBanditProblem.Domain;

namespace MultiArmedBanditProblem
{
    class Program
    {
        static Machine[] GenerateMachines(int numberOfMachines)
        {
            Random r = new Random();

            Console.WriteLine($"Number of machines: {numberOfMachines}");

            Machine[] machines = new Machine[numberOfMachines];

            for (int i = 0; i < numberOfMachines; i++)
            {
                int reward = r.Next(99) + 1;
                double probability = r.NextDouble();

                machines[i] = new Machine(reward, probability);
                Console.WriteLine($"Machine #{i}: {machines[i]}");
            }

            return machines;
        }

        static int getMachineIndexWithHighestPayout(double[] averagePayout)
        {
            int index = 0;
            double max = Double.MinValue;

            for (int i = 0; i < averagePayout.Length; i++)
            {
                if (max < averagePayout[i])
                {
                    index = i;
                    max = averagePayout[i];
                }
            }

            return index;
        }

        static void Main(string[] args)
        {
            int numberOfMachines = 10;
            int iterationsCount = 100;
            double eps = 0.1;

            Random r = new Random();

            Machine[] machines = GenerateMachines(numberOfMachines);

            double[] averagePayout = new double[numberOfMachines];
            int[] machineRunCounts = new int[numberOfMachines];
            double[] totalPayout = new double[numberOfMachines];
            double totalPayout2 = 0.0f;

            double explorationRatio = 0.2;
            int explorationIterations = (int) (explorationRatio * iterationsCount);

            for (int i = 0; i < iterationsCount; i++)
            {
                if (i < explorationIterations)
                {
                    // choose machine
                    int index = (int) Math.Floor(r.NextDouble() * numberOfMachines);

                    // 'play'
                    double p = r.NextDouble();

                    machineRunCounts[index]++;

                    if (p > 1 - machines[index].Probability)
                    {
                        totalPayout[index] += machines[index].Reward;
                        totalPayout2 += machines[index].Reward;
                    }

                    averagePayout[index] = totalPayout[index] / machineRunCounts[index];

                    Console.WriteLine("it={0} [{1}]", i, string.Join(", ", averagePayout));
                    Console.WriteLine($"Total payout: {totalPayout2}");
                }
                else
                {
                    // exploitation phase

                    double p = r.NextDouble();
                    int index = 0;

                    if (p > eps)
                    {
                        index = getMachineIndexWithHighestPayout(averagePayout);
                    }
                    else
                    {
                        index = (int)Math.Floor(r.NextDouble() * numberOfMachines);
                    }

                    // 'play'
                    double p2 = r.NextDouble();

                    machineRunCounts[index]++;

                    if (p2 > 1 - machines[index].Probability)
                    {
                        // win
                        totalPayout[index] += machines[index].Reward;
                        
                        totalPayout2 += machines[index].Reward;
                    }

                    averagePayout[index] = totalPayout[index] / machineRunCounts[index];

                    Console.WriteLine("it={0} [{1}]", i, string.Join(", ", averagePayout));
                    Console.WriteLine($"Total payout: {totalPayout2}");
                }

                // https://jamesmccaffrey.wordpress.com/2017/11/30/the-epsilon-greedy-algorithm/
            }
        }
    }
}

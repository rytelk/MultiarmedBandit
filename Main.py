import random
from Machine import Machine
import matplotlib.pyplot as plt

machines = []
machinesCount = 10
machinesTotalPayouts = []
totalPayout = 0
averagePayouts = []
machineRunCounts = []
maxIterations = 1000
epses = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
avgRewardY = []
stepsX = []

explorationRatio = 0.2

def createMachines():
    for i in range(machinesCount):
        reward = random.randint(1, 101)
        rewardProbability = random.uniform(0, 1)
        machines.append(Machine(reward, rewardProbability))
        machinesTotalPayouts.append(0)
        averagePayouts.append(0)
        machineRunCounts.append(0)


def printMachines():
    for idx, machine in enumerate(machines):
        print(f"Machine #{idx}: {machine}")


def getHighestPayoutMachineIndex():
    return averagePayouts.index(max(averagePayouts))


def getRandomMachineIndex():
    return random.randint(0, machinesCount - 1)


def play(index, iteration):
    global totalPayout

    p = random.uniform(0, 1)
    machineRunCounts[index] += 1

    if p > (1 - machines[index].rewardProbability):
        machinesTotalPayouts[index] += machines[index].reward
        totalPayout += machines[index].reward

    averagePayouts[index] = machinesTotalPayouts[index] / machineRunCounts[index]
    # print(f"Iteracja: {iteration} [{' '.join(str(x) for x in averagePayouts)}]")
    # print(f"Total payout: {totalPayout}")


if __name__ == '__main__':
    random.seed(333)

    createMachines()
    printMachines()

    explorationIterations = maxIterations * explorationRatio
    for eps in epses:
        for i in range(maxIterations + 1):
            if i < explorationIterations:
                index = getRandomMachineIndex()
                play(index, i)
            else:
                explorationProbability = random.uniform(0, 1)
                if(explorationProbability > eps):
                    index = getHighestPayoutMachineIndex()
                else:
                    index = getRandomMachineIndex()
                play(index, i)
            print(f"Average payout: {totalPayout / (i + 1)} Iteration {i}")
            avgRewardY.append(totalPayout / (i + 1))
            stepsX.append(i)
        # TODO - rysowanie wielu epsów
        plt.plot(stepsX, avgRewardY)
        plt.show()

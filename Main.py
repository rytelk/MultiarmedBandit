import random
from Machine import Machine
import matplotlib.pyplot as plt

machines = []
machinesCount = 10
machinesTotalPayouts = []
totalPayout = 0
averagePayouts = []
machineRunCounts = []
maxIterationsCount = 1000
eps = 0.01
avgRewardY = []
stepsX = []

explorationRatio = 0.2

def createMachines():
    for i in range(machinesCount):
        reward = random.randint(1, 101)
        rewardProbability = random.uniform(0, 1)
        machines.append(Machine(reward, rewardProbability))
    createMachineProperties()

def createMachineProperties():
    for i in range(machinesCount):
        machinesTotalPayouts.append(0)
        averagePayouts.append(0)
        machineRunCounts.append(0)

def resetMachineProperties():
    global machinesTotalPayouts
    global totalPayout
    global averagePayouts
    global machineRunCounts

    machinesTotalPayouts = []
    totalPayout = 0
    averagePayouts = []
    machineRunCounts = []
    createMachineProperties()

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
    random.seed(50)

    createMachines()
    printMachines()

    for currentMaxIterations in range(1, maxIterationsCount + 1):
        explorationIterations = currentMaxIterations * explorationRatio
        for i in range(currentMaxIterations + 1):
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
        print(f"Average payout: {totalPayout / currentMaxIterations} Max iterations {currentMaxIterations}")
        stepsX.append(currentMaxIterations)
        avgRewardY.append(totalPayout / currentMaxIterations)
        resetMachineProperties()

    plt.plot(stepsX, avgRewardY)
    plt.show()


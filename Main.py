import random
from Machine import Machine
import matplotlib.pyplot as plt
import numpy as nmp

machines = []
machinesCount = 10
machinesTotalPayouts = []
totalPayout = 0
averagePayouts = []
machineRunCounts = []
maxIterations = 1000
epses = [0.0, 0.01, 0.1, 0.2]
avgRewardY = []
stepsX = []
randomSeed = 3

explorationRatio = 0.01

def createMachines():
    for i in range(machinesCount):
        reward = nmp.random.normal(0, 1)
        machines.append(Machine(reward))
    createMachinesProperties()


def createMachinesProperties():
    for i in range(machinesCount):
        machinesTotalPayouts.append(0)
        averagePayouts.append(0)
        machineRunCounts.append(0)

def reset():
    global avgRewardY
    global stepsX
    global totalPayout
    global machinesTotalPayouts
    global averagePayouts
    global machineRunCounts

    stepsX = []
    avgRewardY = []
    machinesTotalPayouts = []
    averagePayouts = []
    machineRunCounts = []
    totalPayout = 0
    createMachinesProperties()
    random.seed(randomSeed)
    nmp.random.seed(randomSeed)

def printMachines():
    for idx, machine in enumerate(machines):
        print(f"Machine #{idx}: {machine}")


def play(index, iteration):
    global totalPayout

    machinesTotalPayouts[index] += machines[index].reward
    machineRunCounts[index] += 1
    totalPayout += machines[index].reward
    averagePayouts[index] = machinesTotalPayouts[index] / machineRunCounts[index]


if __name__ == '__main__':
    random.seed(randomSeed)
    nmp.random.seed(randomSeed)

    createMachines()
    printMachines()

    explorationIterations = maxIterations * explorationRatio
    for eps in epses:
        for i in range(maxIterations + 1):
            if i < explorationIterations:
                index = random.randint(0, machinesCount - 1)
                play(index, i)
            else:
                explorationProbability = random.uniform(0, 1)
                if(explorationProbability > eps):
                    index =  nmp.argmax(averagePayouts)
                else:
                    index = random.randint(0, machinesCount - 1)
                play(index, i)

            print(f"Average payout: {totalPayout / (i + 1)} Iteration {i}")
            avgRewardY.append(totalPayout / (i + 1))
            stepsX.append(i)
        line, = plt.plot(stepsX, avgRewardY, label = f"Epsilon: {eps}")
        reset()

    plt.title("Greedy-epsilon policy")
    plt.xlabel(f"Steps")
    plt.ylabel("Average payout from all machines")
    plt.legend()
    plt.show()

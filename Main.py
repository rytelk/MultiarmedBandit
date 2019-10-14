import random
from Machine import Machine

machines = []
machinesCount = 10
machinesTotalPayouts = []
totalPayout = 0
averagePayouts = []
machineRunCounts = []
iterationsCount = 100
eps = 0.1

explorationRatio = 0.2
explorationIterations = iterationsCount * explorationRatio

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
    print(f"Iteracja: {iteration} [{' '.join(str(x) for x in averagePayouts)}]")
    print(f"Total payout: {totalPayout}")


if __name__ == '__main__':
    random.seed(50)

    createMachines()
    printMachines()

    for i in range(iterationsCount + 1):
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
    print(f"Average payout: {totalPayout / iterationsCount}")
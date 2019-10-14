import random
from Machine import Machine


machinesCount = 10


def createMachines():
    machines = []
    for i in range(machinesCount):
        reward = random.randint(1, 101)
        rewardProbability = random.uniform(0, 1)
        machines.append(Machine(reward, rewardProbability))
    return machines


def printMachines(machines):
    for idx, machine in enumerate(machines):
        print(f"Machine #{idx}: {machine}")


def getMachineIndexWithHighestPayout(averagePayouts):
    return averagePayouts.index(max(averagePayouts))


if __name__ == '__main__':
    random.seed(100)

    machines = createMachines()
    printMachines(machines)

    print("test")

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
    print(f"Machine #{idx} {machine}")


if __name__ == '__main__':
    machines = createMachines()
    printMachines(machines)
    print("test")

def playMethod(machineRunCounts):
    global machinesCount;
    index = randint(0, machinesCount);
    p = random.uniform(0, 1);
    machineRunCounts[index] = machineRunCounts[index] + 1;
    # TODO
    return;

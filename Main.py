import random
from Machine import Machine

# ------------------------------------
# Zainicjalizować według Grześka
machines;
totalPayout;
averagePayout;
totalPayout2;
machineRunCounts;
# ------------------------------------

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

def playMethod(i):
    
    global machines;
    global totalPayout;
    global averagePayout;
    global totalPayout2;
    global machinesCount;
    global machineRunCounts;
    
    index = randint(0, machinesCount);
    p = random.uniform(0, 1);
    machineRunCounts[index] = machineRunCounts[index] + 1;
    
    if p > (1 - machines[index].Probability):
        totalPayout[index] += machines[index].reward;
        totalPayout2       += machines[index].reward;
        
    averagePayout[index] = totalPayout[index] / machineRunCounts[index];
    print("iteracja: " + i + " [" + ", ".join(averagePayout) + "]");
    print("Total payout: " + totalPayout2);
    
    return;

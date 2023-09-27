import random
print ("Enter Number of Transactions")
n=int(input())
transaction_amount=[0 for i in range(n)]
print("Enter amount type and amount")
for i in range(n):
    amount = input()
    if int(amount[2:]) != 0:
      if amount[0] == "l":
        transaction_amount[i] = -int(amount[2:])
      elif amount[0] == "d":
        transaction_amount[i] = int(amount[2:])



def generate_population(x=n):
    temp_pop = []
    for i in range(x):
        temp_pop.append(generate_tran())
    return temp_pop


def compute_fitness(v):
    fitness = 0
    if v.count(0) == n:
        return 999999999
    for i in range(len(v)):
        if v[i]:
            fitness += transaction_amount[i]
    return abs(fitness)





def crossover(v):
    x = random.randint(0, len(v) - 1)
    y = random.randint(0, len(v) - 1)
    while x == y:
        y = random.randint(0, len(v) - 1)
    cut_point = random.randint(1, n - 1)
    return v[x][:cut_point] + v[y][cut_point:]


def mutate(x, mut_per):
    pos = [0] * (int(n * mut_per))
    temp_pos = [0] * len(pos)
    for i in range(len(pos)):
        temp_pos[i] = random.randint(0, len(x) - 1)
        while temp_pos[i] in pos:
            temp_pos[i] = random.randint(0, len(x) - 1)
        pos[i] = temp_pos[i]
    for i in pos:
        if x[i] == 1:
            x[i] = 0
        else:
            x[i] = 1
    return x


def selection(x, max_pop, select_percentage):
    temp_data = []
    for i in x:
        if compute_fitness(i) == 0:
            return i
        else:
            temp_data.append([compute_fitness(i), i])
    population = temp_data
    population.sort()
    return population[:int(max_pop * select_percentage)]


def to_bin(s):
    string_list = [str(x) for x in s]
    return "".join(string_list)


def algo(max_pop, select_percentage=0.5, mutation_percentage=0.3, max_iteration=100):
    n = max_iteration
    population = generate_population(max_pop)
    population = selection(population, max_pop, select_percentage)
    while n > 0:
        tempo = []
        try:
            for i in population:
                tempo.append(i[1])
        except TypeError:
            return to_bin(population)
        population = tempo
        new_population = []
        for i in range(0, len(population)):
            child = crossover(population)
            child = mutate(child, mutation_percentage)
            if compute_fitness(child) == 0:
                return to_bin(child)
            new_population.append(child)
        population = selection(new_population, max_pop, select_percentage)
        n -= 1
    return -1

print(algo(100))

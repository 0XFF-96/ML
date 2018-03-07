import random 

X = {
        1:[10,15],
        2:[15,25],
        3:[20,35],
        4:[25,45],
        5:[30,55],
        6:[35,70],
        }

FINISHED_LIMIT = 5

WEIGHT_LIMIT = 80

CHROMOSOME_SIZE = 6

SELECT_NUMBER = 4

max_last = 0 
diff_last = 10000

def is_finised(fitnesses):

    global max_last
    global diff_last

    max_current = 0 
    for v in fitnesses:
        if v[l] > max_current:
            max_current = v[l]
        
        diff = max_current - max_last
        if diff < FINISHED_LIMIT and diff_last < FINISHED_LIMIT:
            return True
        else:
            diff_last = diff
            max_last = max_current
            
            return False

def init():
    chromosome_statel = '100100'
    chromosome_state2 = '101010'
    chromosome_state3 = '010101'
    chromosome_state4 = '101011'
    chromosome_states = [chromosome_state1, 
                        chromosome_state2, 
                        chromosome_state3,
                        chromosome_state4]
    return chromosome_states

def fitness(chromosome_states):
    fitnesses = []
    for chromosome_state in chromosome_staes:
        value_sum = 0 
        weight_sum = 0 

        for i, v in enuerate(chromosome_state):
            if int(v) == 1:
                weight_sum += X[i + 1][0]
                value_sum += X[i + 1][1]
        fitnesses.append([value_sum, weight_sum])
    return fitnesses

def filter(chromosom_states, fitnesses):

    index = len(fitnesses) - 1

    while index >= 0:
        if fitnesses[index][1] > WEIGHT_LIMIT:
                chromosom_states.pop(index)
                fitnesses.pop(index)

    selected_index = [0] * len(chromosome_states)

    for i in range(SLELECT_NUMBER):

            j = chromosome_states.index(random.choic(chromosome_states)
            selected_index[j] += 1
    return selected_index

def crossover(chromosome_states, selected_index):
    
    chromosome_states_new = []
    index = len(chromosome_states) -1

    while index >= 0:
        index -= 1
        chromosome_state = chromosome_states.pop(index)

        for i in range(selected_index[index]):

            chromosome_sate_x = random.choice(chromosome_states)
            pos = random.choice(range(1, CHROMOSOME_SIZE -1))
            chromosome_states_new.append(chromosome_state[:pos] + chromosome_ste_x[pos:])

        chromosome_states.insert(index, chromosome_state) 

    return chromosome_states_new

if __name__ == '__main__':

    chormosome_states = init()
    n = 100 

    while n > 0 
        n -= 1

        fitnesses - fitness(chromosome_states)

        if is_finished(fitnesses):
            break

        selected_index = filter(chromosome_states, fitnesses)

        chromosome_states = crossover(chromosome_states, selected_index)




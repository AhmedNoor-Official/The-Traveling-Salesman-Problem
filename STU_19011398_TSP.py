import random
import turtle
import math
import copy

def student_details():

    student_id = 19011398
    student_username = "aa19aiy" 

    return student_id, student_username

    
    # add variables to store student ID and username to be returned

    
def generate_map(x_range, y_range, locations):

    # add code to create a list then use a for loop to create a random population for this list
    generated_map = []
    for x in range(locations):
       x_random = random.randint(-x_range,x_range) 
       y_random = random.randint(-y_range,y_range) 
       locations = [x_random,y_random]
       generated_map.append(locations)

    return generated_map

def print_map(speed, color, thickness, selected_map):
    print("printing map")

    turtle.speed(speed)
    turtle.color(color)
    turtle.pensize(thickness)
    turtle.goto(selected_map[0])

    for x in range(len(selected_map)):
        turtle.goto(selected_map[x])

    # add code to use the turtle to draw the path between all destinations
    # the turtle should make use of the parameters provided: speed. color, etc...
    # you will need to use a loop in order to draw the path to all locations
    
def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance

def calculate_path(selected_map):
    distance = 0
    for i in range(len(selected_map)):
        if i is len(selected_map)-1:
            calcedDistance =calculate_distance(selected_map[i][0],selected_map[i][1], selected_map[0][0],selected_map[0][1])
            distance = distance + calcedDistance
            break
        calcedDistance = calculate_distance(selected_map[i][0],selected_map[i][1], selected_map[i+1][0],selected_map[i+1][1])
        distance = distance + calcedDistance
    return distance
   

    # you will need to setup a variable to store the total path distance
    # you will need to use a loop in order to calculate the distance of the locations individually
    # it would be wise to use make use of the calculate_distance function as you can reuse this
    # remember your need to calculate the path of all locations returning to the original location

    

#################################################################################################

def nearest_neighbour_algorithm(selected_map):  
    optermised_map = []
    temp_map = copy.deepcopy(selected_map)
    optermised_map.append(temp_map.pop(0))

    for x in range(len(temp_map)):
        checkLocation = {
            "coordinate": temp_map[0],
            "calculateddistance": calculate_distance(optermised_map[len(optermised_map)-1][0],optermised_map[len(optermised_map)-1][1], temp_map[0][0],temp_map[0][1])
        }

        for i in range(len(temp_map)):
            newDistance = calculate_distance(optermised_map[len(optermised_map)-1][0],optermised_map[len(optermised_map)-1][1], temp_map[i][0],temp_map[i][1])

            if newDistance < checkLocation["calculateddistance"]:
                checkLocation["calculateddistance"] = newDistance
                checkLocation["coordinate"] = temp_map[i]

        optermised_map.append(checkLocation["coordinate"])
        temp_map.remove(checkLocation["coordinate"])

    return optermised_map


#################################################################################################

def genetic_algorithm(selected_map, population, iterations, mutation_rate, elite_threshold):

    gene_pool = create_population(population, selected_map)
    best_solution = iterator(gene_pool, iterations, mutation_rate, elite_threshold)


    # this is the main genetic algorithm function and should make use of the inputs and call the sub functions in order to run

    # you will need to call the create_population function and store this in a list

    # you will then need to use the iterator function and store the returned solution to best_solution

    return best_solution

def create_population(population, selected_map):

    gene_pool = []

    for x in range(population):
        gene_pool.append(copy.deepcopy(selected_map))
        random.shuffle(gene_pool[x])
        
    return gene_pool

        

    # you need to create an empty list called gene_pool for the population

    # use a for loop and the provided inputs to create the population 

    # you will also need to randomise the individuals within the population
        
    
def fitness_function(gene_pool, best_solution):

    ranking = []
    best_score = calculate_path(best_solution)
    for x in gene_pool:
        score = calculate_path(x)
        if score < best_score:
            best_solution = x
        ranking.append(score)

    sorted_gene_pool = [x for _,x in sorted(zip(ranking, gene_pool))]

    return sorted_gene_pool, best_solution

    

    # you need to find a way to rank the fitness of your population. one way you may consider doing this is with a ranked list

    # you will need to have correctly implemented the calculate_path function in order to rank the fitness of the population

    # you may consider using a loop to achieve this

    # your function must return a sorted gene pool that is sorted by fittest (shortest path to longest path

    # your function should also return the fittest individual in best_solution
    
    

def iterator(gene_pool, iterations, mutation_rate, elite_threshold):

    best_solution = []
    temp_gene_pool = []

    for i in range(iterations):
        sorted_pool, new_best_solution = fitness_function(gene_pool, best_solution)
        new_gene_pool = mating_function(sorted_pool, new_best_solution, mutation_rate, elite_threshold)
        temp_gene_pool.extend(new_gene_pool)

    for x in range(len(temp_gene_pool)):
        temp_gene_pool[x] = {
            "single_gene": temp_gene_pool[x],
            "calculate_distance": calculate_path(temp_gene_pool[x])
        }

    temp_gene_pool = sorted(temp_gene_pool, key=lambda i : i['calculate_distance'])
    best_solution = temp_gene_pool[0]["single_gene"]

    

    return best_solution
    

    # you need to use the provided inputs to iterate (run) the algorithm for the specified iterations

    # you will need to use a for loop in order to achieve this

    # in order for this function to work all over parts of the algorithm must be complete

    # the function must return the best individual (best_solution) in the population

    return best_solution

def mating_function(gene_pool, best_solution, mutation_rate, elite_threshold):

    new_gene_pool = []

    for x in gene_pool:

        parent_1 = copy.deepcopy(gene_pool[random.randint(0,int(len(gene_pool) * elite_threshold))])
        parent_2 = copy.deepcopy(x)
        child = breed(parent_1, parent_2)
        child = mutate(child, mutation_rate)
        new_gene_pool.append(child)

    return new_gene_pool

    # you need to create a new list called new_gene_pool to store the newly created individuals from this function

    # you will need to use a loop in order to perform the genetic crossover and mutations for each individual

    # in order for this function to work correctly you need to select the parent genes based to create the child

    # one of the top individuals based on the elite_threshold should be selected as one of the parents

    # once both parents have been chosen the breed function should be called using both of these parents
    # this means the breed function must be working and returning a child

    # once the breed function has returned a new individual this individual needs to be mutated
    # this means you need to implement the mutate function and it must return the mutated child

    # the function must return a new generation of individuals in new_gene_pool
    
  

def breed(parent_1, parent_2):

    cut_point = []

    cut_point.extend([random.randint(0,len(parent_2)),random.randint(0, len(parent_2))])

    child = []
    dna_1 = []
    dna_2 = []


    for n in range(cut_point[0], cut_point[1]):

        dna_1.append(parent_1[n])
        
    dna_2 = [item for item in parent_2 if item not in dna_1]

    child = dna_1 + dna_2

    return child

    # you need to select random points in which to cut the genes of the parents and put them into the child

    # because the individual must contain all of the locations (this is a unique issue to the TSP) the gene selection is slightly more difficult
    
    # one suggested way is to selected portions of genetic data from one parent then fill in the remainder of locations from the other parent

    # the portion of genes selected should be random and you may want to use some for loops to achieve this

    # the function must return a child of the 2 parents containing all the locations in the original map

    

def mutate(child, mutation_rate):

    
    for switch in range(len(child)):

        if(random.random()<mutation_rate):

            switch_with = random.randint(0,len(child)-1)
            gene_1 = child[switch]
            gene_2 = child[switch_with]
            child[switch] = gene_2
            child[switch_with] = gene_1

        mutated_child = child

    return mutated_child

    # this function must mutate the genes of the child based on the mutation rate provided

    # to achieve this you may want to use a for loop to go through the child

    # then use a random number with an if statement according the mutation rate

    # selected genes will then need to be swapped

    # the function must return a child containing all the locations in the original map but not as it originally arrived

  

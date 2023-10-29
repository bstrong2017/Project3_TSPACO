#Brittany Strong
#October 28, 2023
#CAP 4630
#Dr. Marques
#Project 03 Traveling Salesman Problem using Ant Colony Optimization
#In this program we seek to create a TSP by simulating a ant colony traveling to every randomized city in our algorithm using matrixes. The ants will travel to every city leaving behind a path to the next ant to determine the shortest path, this essentially recreate the swarm intelligence found in ant colonies
import numpy as np
import random
import matplotlib.pyplot as plt

# Function to calculate the total distance of a tour
def tour_length(tour, distance_matrix):
    length = 0
    num_cities = len(tour)
    for i in range(num_cities):
        length += distance_matrix[tour[i]][tour[(i + 1) % num_cities]]
    return length

# Ant Colony Optimization function to find the shortest TSP tour
def ant_colony_optimization(distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate):
    num_cities = len(distance_matrix)   #give numcities length of matrix for phermone trail
    pheromone_matrix = np.ones((num_cities, num_cities))  # Initialize pheromone levels

    best_tour = None    #best tour hasn't been determined yet
    best_length = float('inf')

    for iteration in range(num_iterations):
        ant_tours = []  #array to hold travled cities by ants
        for ant in range(num_ants):
            visited = [False] * num_cities
            current_city = random.randint(0, num_cities - 1)
            tour = [current_city]

            for _ in range(num_cities - 1):
                # Calculate probabilities to move to the next city
                probabilities = []
                for city in range(num_cities):
                    if not visited[city]:
                        pheromone = pheromone_matrix[current_city][city]
                        distance = 1 / distance_matrix[current_city][city]
                        probability = (pheromone ** alpha) * (distance ** beta)
                        probabilities.append((city, probability))

                # Select the next city based on the probabilities
                selected_city = max(probabilities, key=lambda x: x[1])[0]
                tour.append(selected_city)
                visited[selected_city] = True
                current_city = selected_city

            ant_tours.append(tour)

        # Update pheromone levels
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    pheromone_matrix[i][j] *= (1 - evaporation_rate)
        for tour in ant_tours:
            tour_len = tour_length(tour, distance_matrix)
            for i in range(num_cities):
                j = (i + 1) % num_cities
                pheromone_matrix[tour[i]][tour[j]] += 1 / tour_len

        # Update the best tour
        for tour in ant_tours:
            tour_len = tour_length(tour, distance_matrix)
            if tour_len < best_length:
                best_tour = tour
                best_length = tour_len

    return best_tour, best_length
  
  # Function to plot the TSP solution
def plot_tsp_solution(tour, coordinates):
  x = [coordinates[i][0] for i in tour]
  y = [coordinates[i][1] for i in tour]
  x.append(x[0])  # Return to the starting city
  y.append(y[0])  # Return to the starting city

  plt.figure(figsize=(8, 6))
  plt.plot(x, y, 'ro-')
  plt.title('TSP Solution')
  plt.xlabel('X-coordinate')
  plt.ylabel('Y-coordinate')
  plt.grid()
  plt.show()

# Driving code
if __name__ == '__main__':
    num_cities = 25 #NUM of Cities
    distance_matrix = np.random.rand(num_cities, num_cities)  # Random distance matrix
    #randomized coordinates for our cities
    coordinates = [(random.random(), random.random()) for _ in range(num_cities)]


    num_ants = 10   #ants in colony, can be changed or varied
    num_iterations = 100    #number of iterations, our stopping criteria
    alpha = 1.0  # Pheromone influence
    beta = 2.0  # Distance influence
    evaporation_rate = 0.5  #Evaporation rate, used to update our phermone trail

    best_tour, best_length = ant_colony_optimization(distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate)
    print("Best tour:", best_tour)
    print("Shortest tour length:", best_length)
  
    # Plot the solution
    plot_tsp_solution(best_tour, coordinates)


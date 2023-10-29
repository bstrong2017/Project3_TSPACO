# Project3_TSPACO
Brittany Strong 

Dr.Marques 

CAP4630 Into. to Artificial Intelligence 

Project 3, Traveling Salesman Problem using Ant Colony Optimization 

# Project Breakdown/ Overall Design 

In creating the Traveling Salesman problem, the implementation of Evolutionary algorithms was used to find rather than the best solution but a different solution each time the program ran. This allowed for a large compilation of data to be found from a singular program rather than changing the data every time. However, evolutionary algorithms span to many other genetic algorithms, such as Swarm Intelligence. As the basis of evolutionary algorithms is utilizing the patterns found in nature to create algorithms based on those fundamentals, Swarm intelligent algorithms such as Ant Colony Optimization use the same concept. According to Grokking Artificial Intelligence Algorithms, the idea of swarm intelligence comes from seemingly unintelligent life forms acting in ways that we would deem as intelligent. And this is mostly due to these life forms that we view as “primitive and unintelligent as individuals”, exhibiting “intelligent emergent behavior when acting in groups” (Hurbans 153), which means that life forms such as ants adopt intuitiveness not usually associated with the species when they are in groups. These traits that are brought on by swarm intelligence can be recognizing and communicating with other ants, building and collecting food, as well as sharing travel information. This contribution to the group at large not only aids the colony but ensures survival among other ants. This instinct is adaptable to coding algorithms as it provides a programmer with a way to establish a structure that will develop the best solutions without user interaction. Programmers will use concepts adapted from ACO such as memory, best fitness, and action to extract the best solution within the selected data. 
Memory within Ant Colony Optimization is how the ants remember the tour distances and which path is most optimal. In an algorithm, the memory could be obtained by establishing a counter or array with conditions. In the ACO algorithm, this would be an array of all the places the ants have visited along with the numerical distances. The Best Fitness within the concept of ACO would be the best solution of the algorithm which will provide the shortest distance between the tours. In the program provided in Grokking, we see that the best fitness is determined by the shortest distances between the attractions in the Carnival. In this example, it is intuitive to see how the best fitness is determined, as each ant would travel to each attraction and pass along the shortest possible route. However, to develop the best route, an action of traveling to each destination and leaving behind pheromones would have to be developed. The implementation of Pheromone trails is the bulk of Ant colony optimization, this concept is what makes ACO a swarm intelligent algorithm and efficient in finding the best solutions. 
In Grokking text, there are six steps to create an ACO algorithm which include, initializing the pheromones, creating the ant population, updating the trails, updating the best tour, and developing a stopping criterion. Initialing the pheromones can be either setting a variable to 1 indicating that they are unvisited or establishing a matrix of pheromone trails. Grokking notes that having a valid strategy for the pheromone trails is important in creating the ACO program as this is the determining factor for the best solution. Creating the ant population can be as simple as initializing a variable with several ants or creating an array to append the ants to later in the program. Updating the pheromone trail and best tour or implementations done within the ACO function, which will change every time an ‘ant’ visits a distance, and a new tour is determined. This keeps track of every time a shorter distance is found so that the next ants in the population can determine the next best distance. 

# Project Questions 

How were the cities and distances represented (as a data structure)? 

The cities and distances are represented as matrixes or an array of arrays in the program. The data in the matrixes are made to be x and y coordinates which the program will run through to access within the functions. This was mostly due to my previous Traveling Salesman problem created using a genetic algorithm that utilized arrays filled with randomized cities with coordinates and the Grokking textbook example. In the Carnival attraction example, the cities and pheromone trails were represented as matrixes along with a graph to display how the weighted edges and vertices were connected. 

How did you encode the solution space? 

The Grokking Artificial Intelligence Algorithm provided an in-depth example of the Ant Colony Optimization for Carnival rides which is what I used to create my program. In the text, pseudocode was provided to display how the program would be implemented. The distances were a matrix filled with the allotted distances between the attractions. The matrix was stored in an array that would be passed to the ACO algorithm. 

How did you handle the creation of the initial ant population? 

The initial ant population was initialized to a variable num ants, that will be passed to the ACO function. Within the ACO function, we will append visited locations based on the number of ants in num ant, so that every ant in the colony visits a city and creates a path.

How did you handle the updating of the pheromone trails? 

The Pheromone trails are a matrix of the current cities and the cities in the program. To create a pheromone trial that will mimic the actions of an actual ant, we must remove the values in the matrix that do not represent the best trail, we do this by creating the evaporation rate and using a loop to change the matrix each time. We update the pheromone trail and decrease the values in the matrix by using a calculation that subtracts our values from the evaporation rate. The lower values in the matrix represent the less desirable paths, so the calculation in the program updates the path that our coded ants can follow. 

Which strategy(ies) did you use to compute the best solution? 

To find the best solution in the ACO algorithm, I compared all the distances the ants traveled by the best distance which was infinity. If the ant distance was less than the best distance, then the ant distance was added to the list of tours in the algorithm and the new best length of distances is the ant’s distance. This comparison changes what is considered the best-traveled distance in the TSP algorithm to the best by ACO standards. 

Which stopping condition did you use? Why? 

The number of iterations stops the program from a never-ending loop. The number of iterations gets the ant tour for the coordinates in the cities as there are not many other times when the data of the ant tours needs to mutate or vary. So, the stopping conditions only need to be placed on the number within the tours. This is no different than the explanation provided in the Grokking text, which clarifies the iterations of the code should be based on the number of tours that the ants have traveled. This keeps unnecessary iterations from occurring in the code and keeps the best solution from being lost. 


What other parameters, design choices, initialization, and configuration steps are relevant to your design and implementation? 

It was adding multiple function imports such as plotting and initializing NumPy as a variable that could be used within my functions. While this was an optional feature of the program, it was important for me to plot out my city’s distances and ant trails so that I could see the implementation of the program. Looking at the plotted graph, there are many ways to visit every city in the array of locations, but there is a best solution within that graph. Like the Carnival attraction in the Grokking text that showed the many ways to visit all the attractions at the Carnival but inevitably found that there was a best possible route to all attractions. 

Which (simple) experiments have you run to observe the impact of different design decisions and parameter values? 

One experiment I implemented when creating the Ant Colony optimization problem was tracing the carnival ACO pseudocode. Before writing my own solution, I wanted to understand how the ants would be involved in the TSP program. After reading through the text, it was my understanding that the ACO problem utilized many functions and techniques that the genetic algorithm implemented such as using a roulette to randomize data, heuristic value, initializing a best solution, creating stopping criteria, etc. As Swarm Intelligence is essentially a Evolutionary algorithm, there are a lot of shared details when creating the algorithm. 

# Solution + Graphs 

<a href="https://ibb.co/nMfF93F"><img src="https://i.ibb.co/3mWn2fn/Screenshot-2023-10-24-at-5-14-18-PM.png" alt="Screenshot-2023-10-24-at-5-14-18-PM" border="0"></a>

<a href="https://ibb.co/D7cV6SW"><img src="https://i.ibb.co/THjvnF2/Screenshot-2023-10-24-at-5-14-01-PM.png" alt="Screenshot-2023-10-24-at-5-14-01-PM" border="0"></a>

# Citations

Hurbans, Rishal, Grokking Artificial Intelligence Algorithms. Manning Shelter Island, 2020. 

Hurbans, Rishal, (2020). Grokking Artificial Intelligence Algorithms, Ch06- swarm_intelligence_ants. GitHub. https://github.com/rishal-hurbans/Grokking-Artificial-Intelligence- Algorithms.git 





import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import permutations
from brute_force import BruteForce

class RouteOptimizer():
    def optimize(
            self,
            origin: tuple, 
            destiny: tuple,
            adresses: list[tuple],
            solution_method: str
            ):
            """This is the main method of the optimiser.

            Args:
                origin (tuple): Starting dot of the route
                destiny (tuple): Ending dot of the route
                adresses (list[tuple]): Dots that must be visited in the route
            """
            solution_method_mapping = {
                "1": BruteForce
            }
            optimizer = solution_method_mapping[solution_method]()
            route = optimizer.get_results(origin, destiny, adresses)
            
            self.show_results(route)

    def show_results(self, route: list[tuple]):
            """This method shows results in a graph containing all dots: origin, adresses and destiny.
            It also draws arrows indicating the path selected for the optimal result.

            Args:
                route (list[tuple]): Colection of dots that the graph will plot
            """
            route_size = len(route)
            travelled_distance = 0

            for i in range(route_size):
                x, y = route[i]
                dot_color = 'black'
                if i == 0:
                    dot_color = 'blue'
                elif i == route_size - 1:
                    dot_color = 'red'
                
                plt.scatter(x, y, color=dot_color)

                if i < route_size - 1:
                    x1, y1 = route[i+1]
                    dx = x1 - x
                    dy = y1 - y
                    plt.arrow(x, y, dx, dy, color='black', head_width=0.1)
                    travelled_distance += euclidean(route[i], route[i+1])
            
            plt.title(f'Route has distance of {round(travelled_distance, 2)}')
            plt.savefig('otm_result.png')
            print('Plot saved as otm_result.png')
        
if __name__ == '__main__':
    origin = (0,0)
    destiny = (4,4)
    adresses = [(2,2),(2,1),(5,3),(8,3)]

    route_optimiser = RouteOptimizer()
    solution_method = input(
        "Qual método de resolução deseja aplicar?"
        + "\n(1) Força-bruta"
        + "\nR:"
    )
    route_optimiser.optimize(origin, destiny, adresses, solution_method)
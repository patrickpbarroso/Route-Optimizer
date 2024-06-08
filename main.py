import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import permutations

class RouteOptimizer:
    def optimize(self, origin, destiny, adresses):
        route = self.get_best_route(origin, destiny, adresses)
        self.show_results(route)

    def get_best_route(self, origin, destiny, adresses):
        best_distance = float('inf')
        best_route = None

        for permutation in permutations(adresses):
            route = [origin] + list(permutation) + [destiny]
            distance_route = self.calculate_route_distance(route)

            if distance_route < best_distance:
                best_distance = distance_route
                best_route = route
        
        return best_route

    def calculate_route_distance(self, route):
        distance = 0
        route_size = len(route)

        for i in range(route_size):
            if i < route_size - 1:
                distance += euclidean(route[i], route[i+1])
        
        return distance

    def show_results(self, route):
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
        plt.show()

origin = (0,0)
destiny = (4,4)
adresses = [(2,2),(2,1),(5,3),(8,3)]

route_optimiser = RouteOptimizer()
route_optimiser.optimize(origin, destiny, adresses)
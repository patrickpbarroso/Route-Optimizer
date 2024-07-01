from scipy.spatial.distance import euclidean
from itertools import permutations

class BruteForce:
    def get_results(
        self,
        origin: tuple,
        destiny: tuple,
        adresses: list[tuple]
        ) -> list[tuple]:
        """This method obtains the best possible route, a.k.a. the route with minimal total
        distance.

        Args:
            origin (tuple): Starting dot of the route
            destiny (tuple): Ending dot of the route
            adresses (list[tuple]): Dots that must be visited in the route

        Returns:
            list[tuple]: Complete route with minimal total distance from origin to destiny
        """

        best_distance = float('inf')
        best_route = None

        for permutation in permutations(adresses):
            route = [origin] + list(permutation) + [destiny]
            distance_route = self.calculate_route_distance(route)

            if distance_route < best_distance:
                best_distance = distance_route
                best_route = route
        
        return best_route

    def calculate_route_distance(self, route: list[tuple]) -> float:
        """This method calculates distance from origin to destiny given complete route

        Args:
            route (list[tuple]): Complete route, made by origin, adresses and destiny

        Returns:
            float: Distance of the given route
        """
        distance = 0
        route_size = len(route)

        for i in range(route_size):
            if i < route_size - 1:
                distance += euclidean(route[i], route[i+1])
        
        return distance
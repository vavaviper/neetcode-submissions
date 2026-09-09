'''
You are building a system that helps users find the house closest to a
given location.

Create a class called NeighbourhoodSearch that stores a list of house
locations and provides functions for searching for the closest house.

Class Requirements

Implement the following:

NeighbourhoodSearch(houses)
    Initializes the system with a list of integer house locations.

findClosestHouse(target)
    Returns the index of the house closest to target.

If two houses are equally close to the target, return the index of the
house that appears first in the list.

Example:

houses = [10, 4, 8, 15, 3]

search = NeighbourhoodSearch(houses)

search.findClosestHouse(9)
-> 2

The house at index 2 is located at 8, which is closest to 9.

Constraints
1 ≤ n ≤ 10⁵
-10⁹ ≤ houses[i] ≤ 10⁹
-10⁹ ≤ target ≤ 10⁹

Your task: implement the NeighbourhoodSearch class and its required
functions.
'''
class NeighbourhoodSearch:
    def __init__(self, houses):
        self.houses = houses

    def findClosestHouse(self, target):
        closest_index = 0
        closest_distance = abs(self.houses[0] - target)

        for i in range(1, len(self.houses)):
            distance = abs(self.houses[i] - target)

            if distance < closest_distance:
                closest_distance = distance
                closest_index = i

        return closest_index

houses = [10, 4, 8, 15, 3]
search = NeighbourhoodSearch(houses)

print(search.findClosestHouse(9))
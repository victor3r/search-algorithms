import matplotlib.pyplot as plt

from Map import Map

from Depth import Depth
from Breadth import Breadth
from Greedy import Greedy
from AStar import AStar

map_depth = Map()
map_breadth = Map()
map_greedy = Map()
map_astar = Map()

cities = [c for c in dir(Map()) if c[0] != '_']

for i in range(len(cities)):
    print('{} - {}'.format(i+1, getattr(Map(), cities[i]).name))

start = int(input('Escolha o ponto de partida: '))
end = int(input('Escolha o destino: '))
print('\n')

depth = Depth(
    getattr(map_depth, cities[start - 1]), getattr(map_depth, cities[end - 1]))
breadth = Breadth(
    getattr(map_breadth, cities[start - 1]), getattr(map_breadth, cities[end - 1]))
greedy = Greedy(getattr(map_greedy, cities[end - 1]))
astar = AStar(getattr(map_astar, cities[end - 1]))

number_visited_cities = []
travelled_distance = []
search_algorithms = ['DFS', 'BFS', 'Gulosa', 'A*']

greedy_values = greedy.search(getattr(map_greedy, cities[start - 1]))
astar_values = astar.search(getattr(map_astar, cities[start - 1]))

visited_cities_depth = depth.search()
visited_cities_breadth = breadth.search()
visited_cities_greedy = greedy_values[0]
visited_cities_astar = astar_values[0]

number_visited_cities.append(len(visited_cities_depth))
number_visited_cities.append(len(visited_cities_breadth))
number_visited_cities.append(len(visited_cities_greedy))
number_visited_cities.append(len(visited_cities_astar))

travelled_distance.append(greedy_values[1])
travelled_distance.append(astar_values[1])

print('DFS: {}\n'.format(' -> '.join(visited_cities_depth)))
print('BFS: {}\n'.format(' -> '.join(visited_cities_breadth)))
print('Gulosa: {}\n'.format(' -> '.join(visited_cities_greedy)))
print('A*: {}\n'.format(' -> '.join(visited_cities_astar)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('Comparação entre os algoritmos')
ax1.bar(search_algorithms, number_visited_cities)
ax1.set_ylabel('Cidades visitadas')
ax1.set_xlabel('Algoritmos de busca')

search_algorithms = ['Gulosa', 'A*']

ax2.bar(search_algorithms, travelled_distance)
ax2.set_ylabel('Distância percorrida (km)')
ax2.set_xlabel('Algoritmos de busca com informação')

plt.show()

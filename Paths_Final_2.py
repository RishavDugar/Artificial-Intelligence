import sys
import numpy as np
import math

noCity = 8
noCar = 8
maxDepth = 2

class Cars():
 
    def __init__(self, quantity):
        self.V = quantity
        self.stats = [[0 for column in range(7)]
                      for row in range(quantity)]
        self.route_all = [[0 for column in range(1)]
                      for row in range(quantity)]
        self.route_dist_all = [[0 for column in range(1)]
                      for row in range(quantity)]
        self.route = [[0 for column in range(1)]
                      for row in range(quantity)]
        self.route_dist = [[0 for column in range(1)]
                      for row in range(quantity)]

ev = Cars(noCar)
q = np.genfromtxt(r"D:\Rishav\Study\AI-Foundations and Applications\Assignment\EV.csv", delimiter=',')
q = q.tolist()
ev.stats = q

r = np.genfromtxt(r"D:\Rishav\Study\AI-Foundations and Applications\Assignment\Nodes.csv", delimiter=',')
r = r.tolist()
r[0][0] = 0


# Python program to print all paths from a source to destination.
   
from collections import defaultdict
   
# This class represents a directed graph 
# using adjacency list representation
class Graph2:
   
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices 

        # default dictionary to store graph
        self.graph = defaultdict(list) 
   
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
   
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path, id):
  
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
        
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            path2 = path.copy()
            dist =0
            for i in range(len(path2)-1) :
              dist = dist + r[path2[i]][path2[i+1]]
            
            #For all paths possible
            if ev.route_dist_all[id][0] == 0:
              ev.route_dist_all[id][0] = dist
              ev.route_all[id][0] = path2
            else :
              ev.route_dist_all[id].append(dist)
              ev.route_all[id].append(path2)
            
            '''#Fortwo best paths of each car
            if ev.route_dist[id][0] == 0 and ev.route_dist[id][1] == 0 :
              
              ev.route_dist[id][0] = dist
              ev.route[id][0] = path2
              ev.route_dist[id][1] = dist
              ev.route[id][1] = path2

            elif ev.route_dist[id][0] > dist and ev.route_dist[id][1] > dist:     
              ev.route_dist[id][0] = dist
              ev.route[id][0] = path2
            
            elif ev.route[id][0]==ev.route[id][1]:
              ev.route_dist[id][1] = dist
              ev.route[id][1] = path2
              
            elif ev.route_dist[id][1] > dist :    
              ev.route_dist[id][1] = dist
              ev.route[id][1] = path2'''

        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False and r[u][i] < 100 * ev.stats[id][4]:
                    self.printAllPathsUtil(i, d, visited, path, id)
                      
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d, id):
  
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
  
        # Create an array to store paths
        path = []
  
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path, id)

t = Graph2(noCity)
for i in range(noCity):
  for j in range(noCity) :
    if r[i][j] < 10000 :
      t.addEdge(i,j)

for id in range(noCar) :
  t.printAllPaths(int(ev.stats[id][0]-1),int(ev.stats[id][1]-1),id)
#print(ev.route_dist_all)

## for natural form of path
'''for i in range(noCar) :
  for j in range(2) :
    ev.route[i][j] = [x+1 for x in ev.route[i][j]]'''


#print(ev.route_all[0])

for id in range(noCar) :
  sort_arg = np.argsort(ev.route_dist_all[id])
  for j in range(min(maxDepth,len(ev.route_all[id]))) :
    n = sort_arg[j]
    if ev.route_dist[id][0] == 0:
      ev.route_dist[id][0] = ev.route_dist_all[id][n]
      ev.route[id][0] = ev.route_all[id][n]
    else :
      ev.route_dist[id].append(ev.route_dist_all[id][n])
      ev.route[id].append(ev.route_all[id][n])

#print(ev.route_dist)


## for natural form of path
'''for i in range(noCar) :
  for j in range(2) :
    ev.route[i][j] = [x+1 for x in ev.route[i][j]]'''

#print(ev.route)

batc = np.zeros((noCar,noCity), dtype=int)
battery_needed = [0.]*noCar
path = []
current_battery = [0]*noCar
visited = [[-1 for column in range(1)]
                     for row in range(noCity)]

#Assuming one path
for id in range(noCar):
  path.append(ev.route[id][0])
  #battery_needed[id] = max(0,math.ceil(ev.route_dist[id][0]/ev.stats[id][4] - ev.stats[id][2]))
  current_battery[id] = int(ev.stats[id][2])



path_optimal = []
batc_optimal = np.zeros((noCar,noCity), dtype=int)
time_optimal = [[0 for column in range(1)]
                for row in range(noCar)]
minimum_time_achieved = sys.maxsize
charge_start_time = [[-1 for column in range(noCity)]
                      for row in range(noCar)]
charge_end_time = [[-1 for column in range(noCity)]
                    for row in range(noCar)]


def final_time (bc,path) :

  time = [[0 for column in range(1)]
          for row in range(noCar)]
  charging_start_time = [[-1 for column in range(noCity)]
                         for row in range(noCar)]
  charging_end_time = [[-1 for column in range(noCity)]
                         for row in range(noCar)]

  for id in range(noCar) :
    for j in range(len(path[id])) :
      if j==0:
        time[id][0] = 0
      else :
        time[id].append(time[id][j-1]+r[path[id][j-1]][path[id][j]]/ev.stats[id][6])

  instances = [0]*noCity
  car_at_instance = [[-1 for column in range(1)]
                     for row in range(noCity)]
  for i in range(noCity) :
    for j in range(noCar) :
      if bc[j][i] > 0 :
        instances[i] += 1
        if car_at_instance[i][0] == -1:
          car_at_instance[i][0] = j
        else:
          car_at_instance[i].append(j)
  #print("instances",instances)
  #print("car_instances",car_at_instance)

  #Adding the charging time to all
  for i in range(noCity) :
    if instances[i] >= 1 :
      for j in range(len(car_at_instance[i])) :
        id = car_at_instance[i][j]
        if id > -1 :
          count = 0
          for k in range(len(path[id])) :
            if path[id][k] == i :
              count = 1
              charging_start_time[id][i] = time[id][k]
              charging_end_time[id][i] = time[id][k] + bc[id][i]*ev.stats[id][3]
            if count>0 :
              time[id][k] = time[id][k] + bc[id][i]*ev.stats[id][3]
  
  visited = car_at_instance.copy()
 
  #Adding the delay time if any:
  def delay() :
    counter = 0
    for i in range(noCity) :
      if instances[i] > 1 :
        max_time = 0
        max_time_car = -1
        id = -1
        #time_stamp = [0]*len(visited[i])
        j_val = -1

        for j in range(len(visited[i])) :
          id = visited[i][j] 
          if visited[i][-2] == -1 :
            max_time = time[id][-1]
            max_time_car = id
            j_val = j
          else :    
            if time[id][-1] > max_time and id > -1:
              max_time = time[id][-1]
              max_time_car = id
              j_val = j
              counter = 1

        if id==(noCity-1) and counter == 0 :
          return 0
        
        for j in range(len(car_at_instance[i])) :
          id = visited[i][j]
          if id > -1 and id != max_time_car:
            if charging_end_time[id][i] < charging_start_time[max_time_car][i] :
              visited[i][j_val] = -1
              return 1
            elif charging_end_time[max_time_car][i] < charging_start_time[id][i] :
              visited[i][j_val] = -1
              return 1
            else :
              if charging_start_time[id][i] < charging_start_time[max_time_car][i]:
                count = 0
                diff = 0
                for k in range(len(path[id])) :
                  if path[id][k] == i :
                    count = 1
                    diff = min(charging_end_time[max_time_car][i]-charging_start_time[max_time_car][i], abs(charging_end_time[id][i]-charging_start_time[max_time_car][i]))
                    charging_end_time[id][i] = charging_end_time[id][i] + diff
                  if count>0 :
                    time[id][k] = time[id][k] + diff
                visited[i][j_val] = -1
                return 1

              elif charging_start_time[id][i] < charging_end_time[max_time_car][i]:
                count = 0
                diff = 0
                for k in range(len(path[id])) :
                  if path[id][k] == i :
                    count = 1
                    diff = charging_end_time[max_time_car][i]-charging_start_time[id][i]
                    charging_end_time[id][i] = charging_end_time[id][i] + diff
                    charging_start_time[id][i] = charging_end_time[max_time_car][i]
                  if count>0 :
                    time[id][k] = time[id][k] + diff
                visited[i][j_val] = -1
                return 1

      elif i == noCar-1 and counter == 0:
        return 0

  while True :
    i = delay()
    if i == 0 :
      break
  
  max_Total_Time = 0

  for id in range(noCar) :
    if time[id][-1] > max_Total_Time :
      max_Total_Time = time[id][-1]

  global path_optimal
  global batc_optimal
  global time_optimal
  global charge_end_time
  global charge_start_time
  global minimum_time_achieved

  if max_Total_Time < minimum_time_achieved :
    #print("Entered")
    minimum_time_achieved = max_Total_Time
    path_optimal = path.copy()
    batc_optimal = batc.copy()
    time_optimal = time.copy()
    charge_start_time = charging_start_time.copy()
    charge_end_time = charging_end_time.copy()

def time_calculator(id, src, batr,current,path) :
  ## here reduced src form
  ##batr = battery remaining
  ## if src in path is 2 read 1

  if id==(noCar-1) and src==path[id][-2] :
    #print(batc)
    
    final_time(batc,path)

  else :
    if src==path[id][-2] :

        time_calculator(id+1,int(ev.stats[id+1][0]-1), battery_needed[id+1],current_battery[id+1],path)

    else :

      for i in range(len(path[id])-1):
        if path[id][i] == src :
          next = path[id][i+1]

      batRangeMax = int(min(batr,100-current))
      
      batRangeMin = int(max(0, math.ceil(r[src][next]/ev.stats[id][4] - current)))

      for j in range(batRangeMin,batRangeMax+1) :

        if next == path[id][-2]:
          if ( batr + current - r[src][next]/ev.stats[id][4] ) > 100 :
            return
          else :
            batc[id][src] = j
            batc[id][next] = batr - j
            time_calculator(id, next, batr - j,current + j - r[src][next]/ev.stats[id][4],path)
        else:
          batc[id][src] = j
          time_calculator(id, next, batr-j,current + j - r[src][next]/ev.stats[id][4],path) 

counter_for_initialisation = 0

def path_builder(id) :
  global battery_needed
  if id == (noCar - 1) :
    
    time_calculator(0,int(ev.stats[0][0])-1,battery_needed[0],current_battery[0],path)
    #print(path)
  else:
    for j in range(len(ev.route[id])) :
      path[id] = ev.route[id][j]
      battery_needed[id] = max(0,math.ceil(ev.route_dist[id][j]/ev.stats[id][4] - ev.stats[id][2]))
      #print(ev.route[id][j])
      path_builder(id + 1)
  
path_builder(0)

#time_calculator(0,int(ev.stats[0][0])-1,battery_needed[0],current_battery[0])

print("Path Taken",path_optimal)
print("Battery charge Matrix",batc_optimal)
print("Time charging starts of car i at node j",charge_start_time)
print("Time charging ends of car i at node j",charge_end_time)
print("Time when Car i leaves nodes in its path",time_optimal)
print("Maximum of the time",minimum_time_achieved)
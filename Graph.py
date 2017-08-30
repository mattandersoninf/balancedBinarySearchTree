class Vertex:
  def __init__(self, value, neighbors = None, visited = False):
    if neighbors == None:
      neighbors = []
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
  def getValue(): return self.value
  def getNeighbors(): return self.neighbors
  def visited(): return self.visited
  
class Graph:
  def __init__(self, vertexDict = {},edgeDict = {}):
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
  def addVertex(self, vertex):
    vertexDict[vertex.value] = vertex.neighbors

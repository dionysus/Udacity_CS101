# graph = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

def kvalue (graph, page, link):

	if page == link:
		return 0

	else:
		testlist = []

		for i in graph[link]:
			testlist.append(i)

		if page in testlist:
			return 1 

			return 1 + kvalue (graph, page, i)

g = {'a': ['a', 'b', 'c'], 'c': ['d'], 'b': ['e', 'g'], 'e': ['f'], 'd': ['f', 'g'], 'g': ['a'], 'f': ['a']}

print kvalue(g, 'e', 'f')

 #e > f > a > b > e
import sys


#DFS to find patterns
def dfs(graph,start,leng,path,wl):

	if leng>=wl:
		word=''
		for w in path:
			word += w

		#Check word if it is valid or not 
		print word
		''' You Code Here '''


		return
	else:
		for ver in graph[start]:
			if ver not in path:
				leng+=1
				path.append(ver)
				#print path
				#print path,leng
				dfs(graph,ver,leng,path,wl)
				path.pop(-1)
				leng-=1
		

#Graph Defined
#Here we can take input also - Future Work!
words = {'A' : ['B','E','F'] , 'B' : ['A','C','E','F','G'], 'C' : ['B','F','G','H','D'], 'D' : ['C','G','H'], 'E' : ['A','B','F','I','J'] , 'F' : ['A','B','C','E','G','I','J','K'], 'G' : ['B','C','D','F','H','J','K','L'], 'H' : ['D','G','C','K','L'],'M' : ['I','J','N'] , 'N' : ['M','I','J','K','O'], 'O' : ['N','J','K','L','P'], 'P' : ['O','K','L'], 'I' : ['E','F','J','N','M'] , 'J' : ['E','F','G','M','N','I','O','K'], 'K' : ['G','O','N','F','H','J','P','L'], 'L' : ['H','G','O','K','P'] }

for i in range(3,9):
	for j in words:
		path = [j]
		dfs(words,j,1,path,i)
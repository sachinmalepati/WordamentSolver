import sys
import string

#DFS to find patterns
def dfs(graph,start,leng,path,wl):

	if leng>=wl:
		word=''
		for w in path:
			word += inw[w]

		#Check word if it is valid or not 
		#print word
		if word in wordlist:
			print word


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
		

# Input The Wordament
inw = {}
x='a'
for i in range(4):
	for j in range(4):
		inw[x]=raw_input('Wordament-' + '('+str(i)+','+str(j)+') : ')
		x=chr(ord(x)+1)

words = {'a' : ['b','e','f'] , 'b' : ['a','c','e','f','g'], 'c' : ['b','f','g','h','d'], 'd' : ['c','g','h'], 'e' : ['a','b','f','i','j'] , 'f' : ['a','b','c','e','g','i','j','k'], 'g' : ['b','c','d','f','h','j','k','l'], 'h' : ['d','g','c','k','l'],'m' : ['i','j','n'] , 'n' : ['m','i','j','k','o'], 'o' : ['n','j','k','l','p'], 'p' : ['o','k','l'], 'i' : ['e','f','j','n','m'] , 'j' : ['e','f','g','m','n','i','o','k'], 'k' : ['g','o','n','f','h','j','p','l'], 'l' : ['h','g','o','k','p'] }

WORDLIST_FILENAME = "words.txt"

def loadWords():
	global wordlist
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# line: string
	line = inFile.readline()
    	# wordlist: list of strings
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

wordlist = loadWords()


for i in range(3,9):
	for j in words:
		path = [j]
		dfs(words,j,1,path,i)

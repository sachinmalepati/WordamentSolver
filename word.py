import sys
import string
import re



#Binary Search
def binarySearch(alist,item):
	f=0
	l=len(alist)-1
	exist=False
	while f<=l and not exist:
		mid=(f+l)//2
		if alist[mid] == item:
			exist=True
		else:
			if item<alist[mid]:
				l=mid-1
			else:
				f=mid+1
	return exist

def validate(word):
	#Binary Search
	#Working Fine - Fast :D
	if word not in foundWords:
		if binarySearch(wordlist,word):
			print word
			foundWords.append(word)	
	return


#DFS to find patterns
def dfs(graph,start,leng,path,wl):

	if leng>=wl:
		word=''
		
		for w in path:
			word += inw[w]
		if '$' in word:
			validate(string.replace(word,'$',multi[0]))
			validate(string.replace(word,'$',multi[1]))
		elif '#' in word:
			if word[-1] == '#':
				validate(string.replace(word,'#',endsWith))
		else:
			validate(word)

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
multi=[]
endsWith=''
for i in range(4):
	for j in range(4):
		inp=raw_input('Wordament-' + '('+str(i)+','+str(j)+') : ')
		if '/' in inp:
			inp=re.split('/',inp)
			inw[x]= '$'
			multi=inp
		elif '-' in inp:
			inw[x] = '#' 
			endsWith = inp[1:]
			print endsWith
		else:
			inw[x]=inp
		print inw[x]
		x=chr(ord(x)+1)

words = {'a' : ['b','e','f'] , 'b' : ['a','c','e','f','g'], 'c' : ['b','f','g','h','d'], 'd' : ['c','g','h'], 'e' : ['a','b','f','i','j'] , 'f' : ['a','b','c','e','g','i','j','k'], 'g' : ['b','c','d','f','h','j','k','l'], 'h' : ['d','g','c','k','l'],'m' : ['i','j','n'] , 'n' : ['m','i','j','k','o'], 'o' : ['n','j','k','l','p'], 'p' : ['o','k','l'], 'i' : ['e','f','j','n','m'] , 'j' : ['e','f','g','m','n','i','o','k'], 'k' : ['g','o','n','f','h','j','p','l'], 'l' : ['h','g','o','k','p'] }

WORDLIST_FILENAME = "words1.txt"

def loadWords():
	global wordlist
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.read()
    	# wordlist: list of strings
	wordlist = line.split()
	print "  ", len(wordlist), "words loaded."
	return wordlist

#convert text file to a list of words
wordlist = loadWords()
#wordlist = sorted(wordlist)
foundWords = []

for i in range(3,10):
	for j in words:
		path = [j]
		dfs(words,j,1,path,i)

print len(foundWords),": words found"

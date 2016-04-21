class CodeGraph:

	def __init__(self, gnm, numnode):
		self.graphname = gnm
		self.numnodes = numnode
		self.nodes = [None] * numnode

	# method in CodeGraph class starts with 'g'
	# set graph name
	def gsetname(self, gnm):
		self.graphname = gnm
	
	# get graph name
	def ggetname(self):
		return self.graphname

	# set graph number of nodes
	def gsetnumofnodes(self, nds):
		self.numnodes = nds

	# get graph number of nodes
	def ggetnumofnodes(self):
		return self.numnodes

	# set graph node
	def gsetnode(self, nd):
		n = Nodes(nd)
		self.nodes[nd-1] = n

	# get graph all nodes
	def ggetnodes(self):
		return self.nodes

	# get graph node
	def ggetnode(self, nd):
		return self.nodes[nd-1]
	
	# set node adjacent
	def gsetadjnodes(self, nd, adj):
		self.nodes[nd-1].setadjnodes(adj)
	
	# get node adjacent
	def ggetadjnodes(self, nd):
		return self.nodes[nd-1].getadjnodes()

	# add adjacency for remaining nodes which only 
	#appeared as adjacent to some node
	def addremadjacent(self, remadj):
		#import pdb; pdb.set_trace()
		if None in self.nodes:
			var = self.nodes.index(None) + 1
			Flag = True
		else:
			Flag = False

		if Flag:
			self.gsetnode(var)
			for adj in remadj:
				if ' '+str(var) in adj:
					for i in adj.split():
						if '-' in i:
							self.gsetadjnodes(var, -int(i))
							break
			self.addremadjacent(remadj)
	
	# fix if node a appears to be adjacent of b 
	# but b does not have a in its adjacency list.
	def correctadjacent(self):
		for i in self.nodes:
			mn = i.vernm
			for j in i.adjver:
				if mn not in self.nodes[j-1].adjver:
					self.gsetadjnodes(j, mn)

class Nodes:
	def __init__(self, nm):
		self.vernm = nm
		self.adjver = []

	# get node name
	def getnodenm(self):
		return self.vernm

	# set node adjacent
	def setadjnodes(self, adj):
		self.adjver.append(adj)

	# get node adjacent
	def getadjnodes(self):
		return self.adjver


class LinkNodes:

	def __init__(self, nm):
		self.vernm = nm
		self.inlist = False
		self.nextnode = None
		self.prenode = None

	# get node name
	def lgetnodenm(self):
		return self.vernm

	# set inlist val 
	def lsetinlist(self, path):
		self.inlist = path

	# get inlist val 
	def lgetinlist(self):
		return self.inlist

	# set next node
	def lsetnextnode(self, val):
		self.nextnode = val

	# set previous node
	def lsetprevnode(self, val):
		self.prenode = val

	# get next node
	def lgetnextnode(self):
		return self.nextnode

	# set previous node
	def lsetprevnode(self, val):
		self.prenode = val

	# get previous node
	def lgetprevnode(self):
		return self.prenode

	# reset values of inlist and nextnode
	def lresetinlist(self):
		self.inlist = False
		self.nextnode = None
		self.prenode = None


class LinkList:

	def __init__(self, st):
		nd = LinkNodes(st)
		nd.lsetinlist(True)
		self.start = nd
		self.end = nd
		self.length = 1
		self.allnodes = []
		self.allnodes.append(nd)
		self.stacknodes = []
		self.stacknodes.append(nd)

	# set start val
	def setstart(self, st):
		self.start = st
		
	# get start of list
	def getstart(self):
		return self.start

	# get end of list
	def getend(self):
		return self.end

	# get node object
	def node(self, val):
		for i in self.allnodes:
			if i.lgetnodenm() == val:
				return i

	# get all nodes
	def nodes(self, val):
		return self.allnodes

	# sets the onpath value of node
	def addnode(self, nm):
		nd = LinkNodes(nm)
		nd.lsetinlist(True)
		self.allnodes.append(nd)
		self.stacknodes.append(nd)
		self.end = nd
		self.length = self.length + 1
		return nd

	# sets next node for a node
	def nextnode(self, val, nextnode):
		val.lsetnextnode(nextnode)

	# sets previous node for a node
	def prevnode(self, val, prevnode):
		val.lsetprevnode(prevnode)

	# print link list or path
	def printlist(self):
		node = self.start
		tmp = ''
		val = None
		while node.nextnode != None and node.nextnode != val:
			if node.nextnode == self.start.lgetnextnode():
				val = self.start.lgetnextnode() 
			tmp = tmp + str(node.lgetnodenm()) + ' - '
			node = node.lgetnextnode()
		print tmp + " " + str(node.lgetnodenm())

	# to check if wrong crossover is getting created
	def getlength(self):
		node = self.start
		tmp = ''
		val = None
		ct = 1
		while node.nextnode != None and node.nextnode != val:
			if node.nextnode == self.start.lgetnextnode():
				val = self.start.lgetnextnode() 
			tmp = tmp + str(node.lgetnodenm()) + ' - '
			node = node.lgetnextnode()
			ct = ct + 1
		return ct

	# to get length of elements inserted	
	def reallength(self):
		return self.length
	
def main():

	# Read the input graph.
	fnm = raw_input("Please enter name of input file: ")
	print "\nYou entered:", fnm
	rd = open(fnm, 'r')
	data = ''
	rdgraph = []
	
	# This code is reading all data from first line as provided
	# in assignment programming question.
	
	while 1:
		line = rd.readline()
		if not line:
			break
		else: 
			data = line
	rd.close()
	gfnm = ''
	tmp = 0    
	ct = 1		# counter
	nodes = 0	# number of vertices
	remainingadj = []
	val = ''
	flag = 0
	
	for detail in data.split():
		if ct == 1:
			gfnm = detail
			ct = ct + 1
		elif ct == 2:
			graph = CodeGraph(gfnm, int(detail)) 
			ct = ct + 1
		elif ct == 3:
			if int(detail) == 0:
				remainingadj.append(val)
				break
			if int(detail) < 0:
				if flag == 1:
					remainingadj.append(val)
					val = ''
	
				graph.gsetnode(-int(detail))
				# tmp is used to store u and connect all v to it.
				tmp = -int(detail)
				flag = 1
			else:
				graph.gsetadjnodes(tmp, int(detail))
				val = val + " " + str(-tmp) + " " + detail
	
	# correction method
	graph.addremadjacent(remainingadj)

	# correction method
	graph.correctadjacent()
	
	# print node and its adjacency	
	print "\n******* Node and its adjacency *******\n"
	for i in graph.ggetnodes():
		print "       ", i.vernm, "     ",i.adjver
	print "\n***************************************\n"

	

	def LongPath(G, x):

		# returns a random node which is not on path
		def getrandw(path, x):
			node = graph.ggetnode(x)
			nodes = node.getadjnodes()
			nodesrm = []

			for i in nodes:
				if not path.node(i):
					nodesrm.append(i)

			#print nodesrm
			if len(nodesrm) == 0:
				return False
			else:
				# correct this. pick a random value from here 
				import random; return random.choice(nodesrm)
		
		Flag = True
		while Flag:
			checkpath = ''
			path = LinkList(x)
			checkpath = checkpath + str(x) + " "
			u = x
			v = x

			while 1:
				# Will return false when no w found.
				# val type
				w = getrandw(path, u)
				if not w:
					#print "\nBreak in u loop.\n"
					break

				# add new node to path
				path.addnode(w)
				checkpath = checkpath + str(w) + " "

				# add w as next of u in path
				path.nextnode(path.node(u), path.node(w))

				# add v as previous of w on path
				path.prevnode(path.node(w), path.node(u))

				u = w

			# in order to transition the path link list
			# from u loop to v loop
			transitiontovloop = True

			while 1:
				# Will return false when no w found.
				# val type
				w = getrandw(path, v)
				if not w:
					path.setstart(path.node(v))
					#print "\nBreak in v loop.\n"
					break

				# add new node to path
				path.addnode(w)
				checkpath = checkpath + str(w) + " "

				if transitiontovloop:
					# This is to be done only once
					# add start as next of w in path
					path.nextnode(path.node(w), path.getstart())

					# add w as previous of start on path
					path.prevnode(path.getstart(), path.node(w))

					transitiontovloop = False
				else:
					# add v as next of w in path
					path.nextnode(path.node(w), path.node(v))

					# add w as previous of v on path
					path.prevnode(path.node(v), path.node(w))

				v = w

			display = False	
			check1 = True if (v in graph.ggetnode(u).getadjnodes()) else False

			if check1:
			# w connected to v
				for w in graph.ggetnode(v).getadjnodes():
					#wplus connected to w
					nodes = graph.ggetnode(w).getadjnodes()
					wplus = []
					for each in nodes:
						if each != v:
							wplus.append(each)
					if len(wplus) == 0:
						wplus = False
					if not wplus:
						print "There are no remaining nodes in wplus!"
					else:
						for wp in wplus:
							if wp in graph.ggetnode(u).getadjnodes() and path.node(wp).lgetnextnode().lgetnodenm() == w and Flag:
								cycle = path 

								def makecycleright(c, u, v, wp, w, stck):
									print "in make cycle"
									return
									nd = nxt = pre = None
									while 1:
										nd = stck.pop()
										nxt = nd.lgetnextnode()
										pre = nd.lgetprevnode()
										nd.lsetprevnode(nxt)
										if nd.vernm == w:
											break
										nd.lsetnextnode(pre)
									nd.lsetnextnode(c.node(v))
									c.node(wp).lsetnextnode(c.node(u))
									c.node(u).lsetprevnode(c.node(wp))

								if v in graph.ggetnode(u).getadjnodes():
									# crossover found 
									cycle.node(u).lsetnextnode(cycle.node(v))
									cycle.node(v).lsetprevnode(cycle.node(u))


									wp = cycle.node(v).lgetnextnode().lgetnodenm()
									adjnds = graph.ggetnode(wp).getadjnodes()
									pathadj = []
									for w in adjnds:
										# checks if node is on path
										if not cycle.node(w):
											pathadj.append(w)

									if len(pathadj) > 0:
										nxt = cycle.node(wp).lgetnextnode()
										nxt.lsetprevnode(None)
										cycle.node(wp).lsetnextnode(None)
										ct = 0
										link = []
										for i in pathadj:
											cycle.addnode(i)
											zz = i
											ct = ct + 1
											# create a link from w which are not on path yet
											# and then attack that whole link to wplus
											while 1:
												w = getrandw(cycle, zz)
												if not w:
													break
												cycle.addnode(w)
												cycle.nextnode(cycle.node(zz), cycle.node(w))
												cycle.prevnode(cycle.node(w), cycle.node(zz))
												zz = w
												ct = ct + 1
											link.append(ct)
											ct = 0
										appnd = link.index(max(link))
										cycle.nextnode(cycle.node(wp), cycle.node(pathadj[appnd]))
										cycle.prevnode(cycle.node(pathadj[appnd]), cycle.node(wp))
										cycle.setstart(nxt)
									display = True
									Flag = False
									path = cycle

			return {"path": path, "pathlength": path.getlength()}




	x = raw_input("Please enter the value of X: ")
	print "\nYou entered:", x, '\n'
	longest = None
	ret = LongPath(graph, int(x))
	cap = ret['pathlength']
	longest = ret['path']

	for i in range(9):
		import random; x = random.choice(graph.ggetnodes())
		print "Selecting x as: ", x.getnodenm(), '\n' 
		ret = LongPath(graph, x.getnodenm())
		if cap < ret['pathlength']:
			cap = ret['pathlength']
			longest = ret['path']

	print "Longest path is as below:"
	longest.printlist()


if __name__ == '__main__':
	main()

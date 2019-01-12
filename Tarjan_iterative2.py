# encoding: utf-8
from jieba import cut
N = 16
next = 0 # Next index.
index = [None] * N
lowlink = [None] * N
onstack = [False] * N
stack = []
nextgroup = 0 # Next SCC ID.
groups = [] # SCCs: list of vertices.
groupid = {} # Map from vertex to SCC ID.
adj = [[] for i in range(N)]
father = [None] * N
'''
删除一个无向图中的点，能使得原图增加几个连通分量？
如果该点是一个孤立的点，那么增加-1个。
如果该点不是割点，那么增加0个。
如果该点是割点且非根节点，那么增加该点在dfs树中(无反向边连回早期祖先的)的儿子数。
如果该点是割点且是一个dfs树的根节点，那么增加该点在dfs树中(无反向边连回早期祖先的)的儿子数-1的数目，也就是增加了以该dfs树的儿子数目-1
'''
#储存的是删除该给点后增加的连通分量的数目
cut = [0] * N
#表示每个节点是否为割点
isCut = [False] * N
#存储孩子节点的个数
child = [0] * N


def init():
    fp = open("data\\gouzaoshuju\\number_number.txt",'r')   
    for line in fp.readlines():
        datas = line.split(",")
        num1 = int(datas[0])
        num2 = int(datas[1])
        #不能重复添加元素，这里考虑的只是网络，并没有考虑权重的问题，所以可以这样写
        if num2 not in adj[num1]:
            adj[num1].append(num2)
        #在这处理一步,按无向图处理,就不用处理源文件了(源文件中1,0 但是没有0,1这一项)
        if num1 not in adj[num2]:
            adj[num2].append(num1)
    


# Tarjan's algorithm, iterative version.
def sconnect(v):
    global next, nextgroup
    work = [(v, 0)] # NEW: Recursion stack.
    while work:
        v, i = work[-1] # i is next successor to process.
        print "迭代的节点,其中在(a,b)中a代表节点,b代表节点是第几次访问"+str(work)
        del work[-1]
        #如果v是第一次访问
        if i == 0: # When first visiting a vertex:
            index[v] = next
            lowlink[v] = next
            next += 1
            stack.append(v)
            print "栈中的节点"+str(stack)
            onstack[v] = True
        recurse = False
        for j in range(i, len(adj[v])):
            #搜索下一个邻接点
            w = adj[v][j]
            #邻接点没有访问过
            if index[w] == None:
                #没有访问过的节点才算是孩子节点
                child[v] = child[v]+1
                # 入栈,标记之后要访问的节点,记录父节点
                father[w]=v
                #孩子节点的个数加一
                work.append((v, j+1))
                work.append((w, 0))
                recurse = True
                break
            #邻接点已经访问过
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], index[w])
        #recurse为False表示节点的所有子节点已经访问过
        if recurse: continue
        #如果v是一个根节点,将根以及所有子节点退栈
        if index[v] == lowlink[v]:
            com = []
            while True:
                w = stack[-1]
                del stack[-1]
                onstack[w] = False
                com.append(w)
                groupid[w] = nextgroup
                if w == v: break
            groups.append(com)
            nextgroup += 1
        #在递归的过程时递归一个节点就更新一次,虽然在迭代的时候只更新一次但是因为放入了栈中,
        #栈不空就更新,所以最后会全部更新
        if work: 
            w = v
            v, _ = work[-1]
            lowlink[v] = min(lowlink[v], lowlink[w])

#先调用一下初始化的方法
init() 
for v in xrange(N):
#     print v
    if v==0:
        continue

    if index[v] == None:
        sconnect(v)
    
        
   
for i in range(len(father)):
    if father[i] == None:
        continue
      
    if lowlink[i]>=index[father[i]]:
        print "i="+str(i)+"--节点"+str(father[i])+"是割点"
        cut[father[i]] = cut[father[i]]+1
        isCut[father[i]]=True


print "groups:"+str(groups)
print "lowlink:"+str(lowlink)
print "father:"+str(father)        
print "index:"+str(index)
print "isCut:"+str(isCut)
#如果是根节点还要额外的判断一下
print "cut:"+str(cut)
        
        
        
#         
#     
# print "---------------"
# 
# 
# def getname_number():
#     name_number = {}
#     fp = open("data\\gouzaoshuju\\name_number.txt",'r')
#     for line in fp.readlines():
#         line = line.strip()
#         data = line.split(",")
#         name_number[str(data[0])]=data[1]
#     fp.close()
#     return name_number
# name_number = getname_number()
# 
# 
# def getWeight():
#     weight = {}
#     fp = open("data\\gouzaoshuju\\weight.txt",'r')
#     for line in fp.readlines():
#         line = line.strip()
#         data = line.split(",")
#         weight[str(data[0])]=data[1]
#     fp.close()
#     return weight
# weight = getWeight();
# for i in range(len(gedian)):
#     print "关键节点为:"+str(name_number[str(gedian[i])])+"  "+"节点指标权重:"+weight[name_number[str(gedian[i])]]
#     
# print "*****************"
# for item in groups:
#     print item



# encoding: utf-8
import copy
import pr1
import math
import time





N = 1893
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
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_number_number.txt",'r')   
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
def sconnect(v,adj):
    global next, nextgroup
    work = [(v, 0)] # NEW: Recursion stack.
    while work:
        v, i = work[-1] # i is next successor to process.
#         print "迭代的节点,其中在(a,b)中a代表节点,b代表节点是第几次访问"+str(work)
        del work[-1]
        #如果v是第一次访问
        if i == 0: # When first visiting a vertex:
            index[v] = next
            lowlink[v] = next
            next += 1
            stack.append(v)
#             print "栈中的节点"+str(stack)
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


def run(exclude,adj):
    for v in xrange(N):
    #     print v
        if v in exclude:
            continue
    
        if index[v] == None:
            sconnect(v,adj)    
        
def res(): 
    for i in range(len(father)):
        if father[i] == None:
            continue
          
        if lowlink[i]>=index[father[i]]:
#             print "i="+str(i)+"--节点"+str(father[i])+"是割点"
            cut[father[i]] = cut[father[i]]+1
            isCut[father[i]]=True

'''
从数据中删除割点,即把ajd中割点对应的位置置为[],而且把每个子list中含有的相应的元素删除
'''
def deleteNode(num):
    global adj,next,index,lowlink,lowlink,onstack,stack,nextgroup,groups,groupid,father,cut,isCut,child,N
    #把数据复制一份,避免污染原始数据
    newadj = copy.deepcopy(adj)
    newadj[num] = []
    for item in newadj:
        if num in item:
            item.remove(num)
    next = 0 
    index = [None] * N
    lowlink = [None] * N
    onstack = [False] * N
    stack = []
    nextgroup = 0 # Next SCC ID.
    groups = [] # SCCs: list of vertices.
    groupid = {} # Map from vertex to SCC ID.
    father = [None] * N
    cut = [0] * N
    isCut = [False] * N
    child = [0] * N
    #将删除割点之后的数据返回
    return newadj


'''
    遍历每个割点求相应的MGS的值
    MGS即为删除S点后网络中的最大连通分支包含的节点的数目
'''
def getMGS_WGS(nodes):
    MGS = {}
    WGS = {}
    t=0
    for item in nodes:
        t=t+1
        if t%500==0:
            print "tarjan算法运行了"+str(t)+"个节点了"
#         print "删除一个节点之后再一次运行程序*************"
        newadj = deleteNode(item)
        #删除割点之后在一次运行程序
        run([item],newadj)
        res()
#         print "groups:"+str(groups)
#         print "lowlink:"+str(lowlink)
#         print "father:"+str(father)        
#         print "index:"+str(index)
#         print "isCut:"+str(isCut)
        #如果是根节点还要额外的判断一下
#         print "cut:"+str(cut)
        k=0
        for i in range(len(groups)):
            if k<len(groups[i]):
                k = len(groups[i])
        MGS[item]=k
        WGS[item]=len(groups) 
    return MGS,WGS

def computeTGS(MGS,WGS):
    TGS = {}
    KEY = list(MGS)
    MGS_VALUE = list(MGS.values())
    WGS_VALUE = list(WGS.values())
    for i in range(len(MGS)):
        s = 0
        s = s+1+int(MGS_VALUE[i])
        s = (float)(s)/(float)(WGS_VALUE[i])
        TGS[KEY[i]] = s
    return TGS


def getAllGTS(index, lowlink, groups, adj, i, father, cut, isCut):
    global N
    start = time.time()
    #先调用一下初始化的方法
    init()
    run([],adj)
    res()
    end = time.time()
    print "tarjan运行一遍的时间为:"+str(end-start)+"秒"
#     print "groups:" + str(groups)
#     print "lowlink:" + str(lowlink)
#     print "father:" + str(father)
#     print "index:" + str(index)
#     print "isCut:" + str(isCut)
#     #如果是根节点还要额外的判断一下
#     print "cut:" + str(cut)
#     print adj
    geDians = []
    for i in range(len(isCut)):
        if isCut[i] == True:
            geDians.append(i)
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_gedian.txt",'w')
    for i in geDians:
        fp.write(str(i)+"\n")
    fp.close()
    #获取所有节点
    nodes = []
    nodes.extend(geDians)
    for i in range(N):
        if i not in geDians:
            nodes.append(i)
 
    MGS, WGS = getMGS_WGS(nodes)
#     print MGS
#     print WGS
    TGS = computeTGS(MGS, WGS)
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_TGS.txt",'w')
    for key in TGS.keys():
        fp.write(str(key)+","+str(TGS[key])+"\n")
    fp.close()
#     print "---------------"
#     print TGS
    #下面是的输出对应的ri的值
#     name_number = pr1.getname_number()
#     for key in TGS:
#         print name_number[str(key)]+"  " +str(TGS[key])
    return TGS

def computeRi(TGS):
    Ri = {}
    minri = 1000000
    maxri = -1
    for key in TGS.keys():
        ri = TGS[key]
        if minri>ri:
            minri = ri
        if maxri<ri:
            maxri = ri
    for key in TGS.keys():
        ri = TGS[key]
        temp = (float)(ri-minri)/(float)(maxri-minri)
        Ri[key] = temp
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_Ri.txt",'w')
    for key in Ri.keys():
        fp.write(str(key)+","+str(Ri[key])+"\n")
    fp.close()
#     name_number = pr1.getname_number()
#     for key in TGS:
#         print name_number[str(key)]+"  " +str(Ri[key])
    return Ri
    
    
def computeTi(ED,Ri):
    totalRi=0
    for key in Ri:
        totalRi = totalRi+Ri[key]
    totalED = 0
    for key in ED:
        totalED = totalED+ED[key]
    print "totalRi:"+str(totalRi)
    print "totalED:"+str(totalED)
    Ti = {}
    for key in Ri:
        EDi = ED[str(key)]
        ri = Ri[key]
#         print key
#         print EDi
#         print ri
        temp1 = (float)(EDi)/(float)(math.sqrt(totalED))
        temp2 = (float)(ri)/(float)(math.sqrt(totalRi))
        Ti[key] = temp1+temp2
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%"
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_Ti.txt",'w')
    for key in Ti.keys():
        fp.write(str(key)+","+str(Ti[key])+"\n")
    fp.close()
    return Ti
    
def getED():
    ED = {}
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_ED.txt",'r')
    for line in fp.readlines():
        line = line.strip()
        datas = line.split(",")
        num1 = str(datas[0])
        num2 = float(datas[1])
        ED[num1] = num2
    return ED

def getRi():
    Ri = {}
    fp = open("data\\data_2018-12-26\\soc-Epinions1_Ri.txt",'r')
    for line in fp.readlines():
        line = line.strip()
        datas = line.split(",")
        num1 = str(datas[0])
        num2 = float(datas[1])
        Ri[num1] = num2
    fp.close()
    return Ri

def Ti_paixu():
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_Ti.txt","r")
    table = {}
    for line in fp.readlines():
        line = line.strip()
        datas = line.split(",")
        table[int(datas[0])]=float(datas[1])
    fp.close()
    t = sorted(table.items(),key = lambda x:x[1],reverse = False)
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_Ti_paixu.txt","w")
    for i in range(N):
        fp.write(str(t[i][0])+","+str(t[i][1])+"\n")
    fp.close()

if __name__=="__main__":
    start = time.time()
    TGS = getAllGTS(index, lowlink, groups, adj, i, father, cut, isCut)
    print "函数getAllGTS运行完成"
    Ri = computeRi(TGS)
#     Ri = getRi()
    print "函数computeRi运行完成"
#     ED = pr1.getTarget()
    ED = getED()
    print "函数getED运行完成"
    Ti = computeTi(ED,Ri)
    print "函数computeTi运行完成"
    end = time.time()
    print "花费的时间为:"+str(end-start)+"秒"
    Ti_paixu()
    

        
        
        

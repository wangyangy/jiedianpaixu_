# encoding: utf-8

#队列
Q = []
#用来检测是否为连通图
number = 0

'''
初始化图
'''

def getMaxNumber():
    maxnumber = 0
    fp = open("data\\data_2018-12-26\\Email-Enron.txt", 'r')
    nodes = []
    k=0
    for line in fp.readlines():
        k=k+1
        if k%10000==0:
            print "计算了"+str(k)+"行数据了"
        line = line.strip()
        datas = line.split(",")
        num1 = int(datas[0])
        num2 = int(datas[1])
        if num1 not in nodes:
            nodes.append(num1)
        if num2 not in nodes:
            nodes.append(num2)
        if maxnumber < num1:
            maxnumber = num1
        if maxnumber < num2:
            maxnumber = num2
    print len(nodes)
    return maxnumber

def init():
    
#     maxnumber = getMaxNumber()
    #节点个数
    N = 33696 
    #标记
    V = [False] * N 
    #图
    M = [[] for i in range(N)] 
    fp = open("data\\data_2018-12-26\\Email-Enron_.txt",'r')
    k = 0   
    for line in fp.readlines():
        k=k+1
        if k%10000==0:
            print "计算了"+str(k)+"行数据了"
        line = line.strip()
        datas = line.split(",")
        num1 = int(datas[0])
        num2 = int(datas[1])
        #不能重复添加元素，这里考虑的只是网络，并没有考虑权重的问题，所以可以这样写
        if num2 not in M[num1]:
            M[num1].append(num2)
        #在这处理一步,按无向图处理,就不用处理源文件了(源文件中1,0 但是没有0,1这一项)
        if num1 not in M[num2]:
            M[num2].append(num1)
       
    return N,V,M


'''
通过广度优先搜索的方式来判断图是不是连通图.可以得到具体的连通分支的个数
'''
def bfs(node,N,V,M):
    global number
    Q.append(node)
    V[node]=True
    temp = []
    while(len(Q)>0):
        cur = Q.pop(0)
        temp.append(cur)
        number = number+1
        V[cur]=True
        listcur = M[cur]
        for i in range(len(listcur)):
            if V[listcur[i]]!=True:
                V[listcur[i]]=True
                Q.append(listcur[i])
    return temp   
    

def maxgroupCreate(maxgroup):
    groupmap = {}
    for i in range(len(maxgroup)):
        groupmap[maxgroup[i]] = i
#     print groupmap
    fp = open("data\\data_2018-12-26\\yuanshishuju\\Email-Enron.txt",'r')
    fp1 = open("data\\data_2018-12-26\\Email-Enron_.txt",'w')
    k=0
    for line in fp.readlines():
        k=k+1
        if k%10000==0:
            print "计算了"+str(k)+"行数据了"
        line = line.strip()
        datas = line.split(",")
        num1 = int(datas[0])
        num2 = int(datas[1])
        if num1 in maxgroup or num2 in maxgroup:
            fp1.write(str(groupmap[num1])+","+str(groupmap[num2])+"\n")
    fp1.close()
    fp.close()
    

    
if __name__=="__main__":
    N,V,M = init()
    group = []
    count = 0
    for i in range(N):
        if V[i]!=True:
            temp = bfs(i,N,V,M)
            group.append(temp)
            count=count+1
    print number
    maxgroup = []
    for i in group:
        #找到最大连通分量
        if len(i)>len(maxgroup):
            maxgroup = i
        if len(i)<1000:
            print i
    print len(maxgroup)
#     maxgroupCreate(maxgroup)
#     groupmap = {}
#     for i in range(len(maxgroup)):
#         groupmap[maxgroup[i]]=i
#     maxgroup()
#     prepare()
    
     

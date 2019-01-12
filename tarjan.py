# encoding: utf-8
from math import *
import sys   
sys.setrecursionlimit(50000) #例如这里设置为一百万  


N = 54573
n = [0 for i in range(N)]
m = [[] for i in range(N)]
biao = [];
vis = [0 for i in range(N)]
dfn = [0 for i in range(N)]
low = [0 for i in range(N)]
subnets = [0 for i in range(N)]
deep=0
rson=0

def init():
    fp = open("G:\\ruanjian\\develop\\workspace_oxgen\\jiedianpaixu\\data\\newdata2018-10-22\\gemsec_deezer_dataset\\HR_edges.csv",'r')
    # fp = open("data\\newdata\\2220\\number_number.txt",'r')
    # fp = open("data\\Twitter mentions and retweets_\\number_number.txt",'r')
    # fp = open("data\\newdata2018-10-22\\test.txt",'r')
    
    for line in fp.readlines():
        datas = line.split(",")
        num1 = int(datas[0])
        num2 = int(datas[1])
        #不能重复添加元素，这里考虑的只是网络，并没有考虑权重的问题，所以可以这样写
        if num2 not in m[num1]:
            m[num1].append(num2)
        #在这处理异步,按无向图处理,就不用处理源文件了(源文件中1,0 但是没有0,1这一项)
        if num1 not in m[num2]:
            m[num2].append(num1)
    
    
def getBiao():
    fp = open("G:\\ruanjian\\develop\\workspace_oxgen\\jiedianpaixu\\data\\newdata2018-10-22\gemsec_deezer_dataset\\HR_edges_biaohao.txt",'r')
    for line in fp.readlines():
        index = int(line.strip())
        biao.append(index)
    fp.close()
    
def dfs(u):
    global deep
    global m
    global N
    global vis
    global dfn
    global low
    for v in range(N):
        if v in m[u]:
            if vis[v]==0:
                #标记节点已经搜索过
                vis[v]=1;
                deep = deep+1
                print str(deep)
                #第一次搜索到这个节点时,初始化dfn,low
                dfn[v]=deep
                low[v]=deep
                dfs(v)
                #回溯之后维护low,low[u] = min(low[u],low[v])
                low[u]=min(low[u],low[v]);
                if low[v]>=dfn[u]:
                    if u==1:
                        rson = rson+1
                    else:
                        subnets[u] = subnets[u]+1
            else:
                low[u]=min(low[u],dfn[v]);
    return ;
    
    
    
if __name__=="__main__":
    rootIndex = 43244
    init()
    dfs(rootIndex)
    sub = []
    res = []
    for i in range(N):
        if subnets[i]!=0:
            sub.append(i)
    getBiao()
    for k in biao:
        if k in sub:
            res.append(k)
        if len(res)==10:
            break
    print res    
    
    
     
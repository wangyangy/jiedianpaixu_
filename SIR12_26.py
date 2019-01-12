# -*- coding: utf-8 -*-
import random
import copy


def init():
    #总节点数
    N = 7066
    # N = 2220
    m = [[] for i in range(N)]
    
    #A是所有的节点
    A = []
    for i in range(N):
        A.append(i)
    
    #处理图的关系
    fp = open("data\\data_2019_1_11\\wiki-vote\\7066-node_number_number.txt", 'r')
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
    
    fp.close()
    return m,A

def run(m,A,infection,num=-1):
    #先定义三种节点
    #可被感染的节点
    S = []
    #已经被感染的节点
    I = []
    #已经痊愈的节点
    R = []
    #传染率
#     infection = 0.5
    #回复率
    recover = 0.3
    
    II = [
            [699,286,2374,408,1052,2013,3712,517,483,1221],
            [699,286,409,410,902,1052,1146,666,656,7],
            [905,326,409,711,666,286,626,1141,1005,247],
            [326,409,1332,656,686,711,905,2,3,7],
            [326,656,488,686,409,1224,177,1374,926,1141],
            [699,286,2347,1052,2013,3712,408,2,517,483],
        ]
          
    
    print "当前感染率为:"+str(infection)
    ff = open("d:\\duibi.txt",'a')
    ff.write(str(num)+"--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"+"\n")
    k=0
    tou = ""
    for I in II:
        if k==0:
            #print "度:**************************************"
            tou = "度:**************************************"
        elif k==1: 
            #print "between:**************************************"
            tou = "between:**************************************"
        elif k==2:
            #print "Eigenvector:**************************************"
            tou = "Eigenvector:**************************************"
        elif k==3:
            #print "PageRank:**************************************"
            tou = "PageRank:**************************************"
        elif k==4:
            #print "moxing:**************************************"
            tou = "moxing:**************************************"
        else:
            #print "C:**************************************"
            tou = "C:**************************************"
        print tou
        #初始化S,除了I就全是S,R初始化时为0
        for i in A:
            if i in I:
                continue
            S.append(int(i))
            
        #计步器(时间步)
        count = 0
        while True:
            '''有一个问题是先传染还是先康复??????'''
            #遍历感染者人群去传染未感染者
            tempI = copy.copy(I)
            for i in tempI:
                #遍历当前感染者的邻居
                for j in m[i]:
                    #如果当前感染者的邻居是感染者或者是恢复者,继续循环
                    if j in I or j in R:
                        continue
                    else:
                        #有一定的概率被传染并不一定会被传染
                        p = random.uniform(0, 1)
                        if p<infection:
                            I.append(j)
                            S.remove(j)
                #感染者人群也会有一定的概率痊愈
                q = random.uniform(0, 1)
                if q < recover:
                    I.remove(i)
                    R.append(i)
            count+=1
            print str(count)+":I:"+str(len(I))
            print str(count)+":R:"+str(len(R))
            print str(count)+":S:"+str(len(S))
            datas = tou.split(":")
            if len(I)==0:
                ff.write(str(datas[0])+":"+str(count)+":R:"+str(len(R))+"\n")
                break
        k+=1
        S = []
        I = []
        R = []
    ff.write("\n")
    ff.close()
        
if __name__=="__main__":
    m,A=init()
#     for i in range(10):
#         print str(i)+"--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
#         run(m,A,0.5)
#     for i in range(10):
#         print str(i)+"--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
#         run(m,A,0.1)
    for i in range(30):
        print str(i)+"--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        run(m,A,0.01,i)
    
        
    
        
    
    

# -*- coding: utf-8 -*-
import random
import copy

#先定义三种节点
#可被感染的节点
S = []
#已经被感染的节点
I = []
#已经痊愈的节点
R = []
#总节点数
N = 4039
# N = 2220
m = [[] for i in range(N)]
#传染率
infection = 0.5
#回复率
recover = 0.5

#A是所有的节点
A = []
fp = open("data\\data_2018-12-26\\Email-Enron_.txt",'r')
# fp = open("data\\newdata\\2220\\name_number.txt",'r')
#先读入所有节点
for line in fp.readlines():
    temp = []
    line = line.strip()
    data = line.split(",")
    index = int(data[0])
    name = data[1]
    temp.append(index)
    temp.append(name)
    A.append(temp)
fp.close()

#处理图的关系  
# fp = open("data\\Twitter mentions and retweets_\\number_number.txt",'r')
# fp = open("data\\newdata\\2220\\number_number.txt",'r')
# fp = open("data\\test.txt",'r')
fp = open("data\\data_2018-12-26\\Email-Enron_.txt",'r')
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

# print A[0][0]
# print A[0][1]

#初始化10个源节点
#这是按照度排序前10的节点
# I = [237,19,265,147,276,11,12,39,279,981]
#这是模型排序前10的标号
# I = [237,265,393,28,39,19,279,888,981,971]
#这是贪心排序前10的标号
# I = [237,651,1220,1387,1177,963,1476,710,229,1566]
#介数 I = [19,265,28,147,237,12,11,276,680,39]
#pagerank I = [19,265,237,28,147,12,276,11,39,981]

#1893的一个结果
# II = [
# [8,3,18,111,149,47,130,24,20,314],
# [2845,35,224,13,1560,95,248,63,801,446],
# [8,99,2192,1748,214,2572,2830,727,1059,2086],
# [8,3,149,18,111,314,25,47,130,169],
# [8,3,18,111,149,314,47,130,13,24]
#       ]

II = [
            [107,1684,1912,3437,0,2543,2347,1888,1800,1663],
            [107,1684,3437,1912,1085,0,698,567,58,428],
            [1912,2347,2266,2233,2543,2206,1985,2142,2464,2218],
            [3437,107,1684,0,1912,348,686,3980,414,483],
            [3437,107,1684,1912,0,3980,414,348,686,698]
    ]
      
# pkl_file = open('data\\Twitter mentions and retweets_\\biaohao.pkl', 'rb')
# data = pickle.load(pkl_file)
# for i in range(10):
#     I.append(data[i][0])
print "当前感染率为:"+str(infection)
k=0
for I in II:
    if k==0:
        print "度:------------------------"
    elif k==1: 
        print "模型:-----------------------"
    elif k==2:
        print "贪心:------------------------"
    elif k==3:
        print "介数:------------------------"
    else:
        print "PageRank:------------------------"
    #初始化S,除了I就全是S,R初始化时为0
    for i in A:
        if i[0] in I:
            continue
        S.append(int(i[0]))
        
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
        print str(count)+"时刻已经感染的节点有:"+str(len(I))
        print str(count)+"时刻恢复的节点有:"+str(len(R))
        print str(count)+"时刻可能被感染的节点有:"+str(len(S))
        print "总节点数:"+str(len(I)+len(R)+len(S))
        
        if len(I)==0:
            break
    k+=1
    S = []
    I = []
    R = []

    

    

    



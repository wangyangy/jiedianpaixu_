# encoding: utf-8
import random
import copy
import time

#节点数目
N = 1893
# N = 3656
#种子节点集合,最后要选出10个节点,贪心算法初始时S是为空的,实验时设置S初始节点是度最大的节点
# S = [8]
S = [237]
#构建网络拓扑结构
m = [[] for i in range(N)]
#所有网络节点,初始时都没被激活,记录的是每个节点的索引
nodes = [i for i in range(N)]

fp = open("data\\newdata\\1893\\number_number.txt",'r')
# fp = open("data\\Twitter mentions and retweets_\\number_number.txt",'r')
# fp = open("data\\test.txt",'r')
for line in fp.readlines():
    datas = line.split(",")
    num1 = int(datas[0])
    num2 = int(datas[1])
    m[num1].append(num2)
    #在这处理一步,按无向图处理,就不用处理源文件了
    m[num2].append(num1)



'''
影响传播模型采用独立级联模型
    1．初始时(t=0)，网络中只有少量节点处于激活状态，这些节点被称为种子节点。
    2．对任意时刻t≥1，任意一个在t一1时刻被激活的节点u有且仅有一次
        机会去尝试激活它所有的、仍处于非激活状态的邻居v，激活成功的概率为Puv。
    3．当有多个处于激活状态的节点u1，u2，u3．．：…尝试激活它们共同的未激活
        邻居v时，这些节点尝试激活的顺序是随机的，且相互之间独立。
    4. 节点v被激活后，也会尝试去激活它所有邻居中仍处于未激活状态的节
        点。
    5．以上过程不断重复，直到某一时刻网络中不再有新的节点被激活。传播
        终止时，网络中被激活节点的数目就是本次模拟中种子节点的影响力。
'''


#函数的返回值是当前种子集合的|RS(S)}|,即d(S)
def computeRS_(u):
    if u!=None:
        #把函数外部的S拷贝一个副本到函数内部,不要污染外部变量
        tempS = copy.copy(S)
        if u not in tempS:
            tempS.append(u)
        copyS = tempS
#         print copyS
    else:
        #把函数外部的S拷贝一个副本到函数内部,不要污染外部变量
        copyS = copy.copy(S)    
    noInfluency = []
    cur_2_active = copyS
    #自定义的阈值,阈值可以控制运行随时间,当设置为0.75的时候度最大的节点影响范围是3655,就有一个节点没影响,要继续提高
    threshold = 0.9
    #时间步
    count = 0
    while True:
        flag = True
        active_node = []
        #遍历所有激活节点进行激活
        for node in cur_2_active:
            for child in m[node]:
                #在独立级联影响力传播模型中，节点只有一次激活的机会
                if child in noInfluency:
                    continue

                #有一定的概率被激活
                p = random.uniform(0, 1)
                #激活了
                if p>threshold:
                    flag = False
                    active_node.append(child)
        #把新扩展的激活节点加进来,要把重复的节点去掉
        noInfluency.extend(list(set(cur_2_active)))
        cur_2_active = list(set(active_node))
#         print "增加的长度："+str(len(list(set(active_node))))
        #进行了一步影响力传播
        count+=1
#         print "时间步为:"+str(count)
#         print "当前激活的节点数为"+str(len(copyS))
        #此时刻没有新的节点被激活,就停止影响传播,可以自己改写一下,当一部激活的节点数小于30的时候就认为传播停止也可以,这样可以减少运行时间
        if flag == True:
            break
#         if u==None:
#             if len(list(set(active_node)))<30:
#                 break
#         #一步激活节点数的设置要根据总结点数目来调整,这样可以把前期激活节点少的一次性淘汰,也可以截断后期影响传播
#         #150的数值是根据节点度最大的节点测试的值设定的,度最大的点第一次添加大约190个节点，如果当前节点第一次添加的
#         #少于150，就直接以第一次扩充的节点数为当前节点影响力len(list(set(active_node)))<160
#         else:
#             if len(list(set(active_node)))<len(copyS)*0.3 or len(list(set(active_node)))<160:
#                 break
    #返回激活范围
    return len(noInfluency)
    

#调试阈值和激活概率使用
# start = time.time()
# print str(computeRS(237))
# end = time.time()
# print "一个节点计算一次的时间:"+str(end-start)+"秒" 


#定义一个函数计算所有未被激活节点的边际影响增量,应该是模拟R次取平均值,在此只模拟一次,因为时间复杂度太高
def compute(S):
    '''
        RS(S):以S为源节点集合,图G中最终被激活的节点集合
        S的影响范围:d(S) = |RS(S)|,即图中最终的活跃节点数目
                    节点u边际增量的定义是:
                     d(u|S) = d(S∪u)-d(S)
    '''
    while True:
        start = time.time()
        print "当前S为:"+','.join(str(s) for s in S if s not in [None])
        #首先计算d(S)，在没有添加新节点的时候种子集合的影响范围
        ds = computeRS_(None)
        print "ds的值是"+str(ds)
        #用来存储每个节点的边际增量
        maxds = -100000
        maxnode = -1
        j=0
        #遍历nodes,计算每个节点的边际增量
        for node in nodes:
            j+=1
            #如果是激活的源节点就跳过,不计算
            if node in S:
                continue
#             start1 = time.time()
            #添加了一个新节点到种子集合中在去计算影响范围
            curDs = computeRS_(node)
#             print str(curDs)
#             end1 = time.time()
#             print "一个节点计算一次的时间:"+str(end1-start1)+"秒" 
            if maxds<curDs:
                maxds = curDs
                maxnode = node
            #注释性内容
            if j%100==0:
                print "计算了"+str(j)+"个节点了"
        S.append(maxnode)
        end = time.time()
        print "贪心算法添加一个节点的时间:"+str(end-start)+"秒"
        if len(S)==10:
            print "贪心算法的是个节点添加完成"
            break
    print "当前S为:"+','.join(str(s) for s in S if s not in [None])
    return S
    
compute(S) 

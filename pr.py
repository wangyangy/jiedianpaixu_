# encoding: utf-8
'''这个脚本是按照过程一的约束指标,最基本的约束指标'''
# yse

# N = 3656
N = 15
m = [[] for i in range(N)]
res = [0 for i in range(N)]

fp = open("data\\Twitter mentions and retweets_\\number_number.txt",'r')
# fp = open("data\\newdata2018-10-22\\test.txt",'r')
# fp = open("data\\test.txt",'r')

for line in fp.readlines():
    datas = line.split(",")
    num1 = int(datas[0])
    num2 = int(datas[1])
    m[num1].append(num2)
    #在这处理异步,按无向图处理,就不用处理源文件了
    m[num2].append(num1)


#当前节点是i
for i in range(N):
    #遍历i节点的每个直接相邻节点
    temp = 0.0
    for j in m[i]:
        degree = len(m[i])
        temp+=1.0/degree
        #检查均相邻的节点
        for k in m[j]:
            if i in m[k]:
                temp+=(1.0/degree)*(1.0/len(m[k]))
        res[i] += temp*temp
        temp = 0.0
          
#res.sort()
print res
# print res[5]
    
    
    
    
    
    
    
    
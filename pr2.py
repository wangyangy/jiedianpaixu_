# encoding: utf-8
import pickle
'''这个脚本是约束二的指标'''


'''
因为给的数据id不是从0开始的所以,自己处理一下,重新将id和数量对应起来
'''
def prepareName_name():
    fp = open("data\\newdata\\2220\\2220Nodes.txt",'r')
    fp1 = open("data\\newdata\\2220\\name_number.txt",'w')
    i=-1
    j=0
    for line in fp.readlines():
#         print line
        i+=1
        if i==0:
            continue
        line = line.strip()
        data = line.split(",")
        id = int(data[0])
        fp1.write(str(j)+","+str(id)+"\n")
        j+=1
    fp.close()
    fp1.close()
    
def prepareNumber_number():
    fp = open("data\\newdata\\2220\\2220Edges.txt",'r')
    fp1 = open("data\\newdata\\2220\\name_number.txt",'r')
    fp2 = open("data\\newdata\\2220\\number_number.txt",'w')
    name_number = {}
    for line in fp1.readlines():
        line = line.strip()
        data = line.split(",")
        id = int(data[0])
        name = int(data[1])
        name_number[name] = id
    for item in name_number.iteritems():
        print str(item[0])+","+str(item[1])
        
    for line in fp.readlines():
        line = line.strip()
        data = line.split(",")
        source = int(data[0])
        target = int(data[1])
        source_ = name_number.get(source)
        target_ = name_number.get(target)
        fp2.write(str(source_)+","+str(target_)+"\n")
    fp.close()
    fp1.close()
    
# prepareName_name()
# prepareNumber_number()

def paixu_du():
    fp = open("data\\newdata\\2220\\2220Nodes.txt",'r')
    fp1 = open("data\\newdata\\2220\\2220Nodes_paixu.txt",'w')
    i=-1
    dus = {}
    for line in fp.readlines():
#         print line
        i+=1
        if i==0:
            continue
        line = line.strip()
        data = line.split(",")
        du = int(data[2])
        dus[du] = line
    fp.close()
    t = sorted(dus.items(),key = lambda x:x[0],reverse = True)
#     for item_ in dus.iteritems():
#         print str(item_[0])+"---"+str(item_(1))
        
    for i in range(len(dus)):
#         print str(t[i][0])+"------"+t[i][1]+"\n"
        fp1.write(str(t[i][0])+","+t[i][1]+"\n")
    fp1.close()
 
# paixu_du()
 
def getname_number():
    name_number = {}
    fp = open("data\\gouzaoshuju\\name_number.txt",'r')
    for line in fp.readlines():
        line = line.strip()
        data = line.split(",")
        name_number[str(data[0])]=data[1]
    fp.close()
    return name_number



def getTarget():
    #节点的个数
    N = 1893
    #分别初始化好各个指标的存储空间    
    n = [0 for i in range(N)]
    res = [0 for i in range(N)]
    Q = [0 for i in range(N)]
    C = [0 for i in range(N)]
    m = [[] for i in range(N)]
    
    
    # fp = open("data\\newdata2018-10-22\\gemsec_facebook_dataset\\tvshow_edges.csv",'r')
    # fp = open("data\\newdata\\2220\\number_number.txt",'r')
    # fp = open("data\\Twitter mentions and retweets_\\number_number.txt",'r')
    fp = open("data\\data_2019_1_11\\OClink\\1893-node_number_number.txt",'r')
    
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
               
    #计算N
    for i in range(N):
        tempn = []
        for j in m[i]:
            tempn.append(j)
            if i in m[j]:
                tempn.extend(m[j])
                tempn.remove(i)
                continue
            tempn.extend(m[j])
        #这里去掉重复的元素了
        tempn = list(set(tempn))
        n[i] = len(tempn)
            
    #计算Q和C
    #当前节点是i
    for i in range(N):
        #遍历i节点的每个直接相邻节点
        q = 0.0
        for j in m[i]:
            q+=n[j]
        Q[i] = q
       
    #当前节点是i,在word中的公式表示是有错误的,,要理解一下
    for i in range(N):
        #遍历i节点的每个直接相邻节点
        c = 0.0
        for j in m[i]:
            c+=Q[j]
        C[i] = c
    
    #计算结果
    #当前节点是i,看公式确定pij是什么,下面的temp相当于是公式小括号里面的值
    for i in range(N):
        #遍历i节点的每个直接相邻节点
        temp = 0.0
        for j in m[i]:
            #转换成浮点数来计算
            temp+=(float)(Q[j])/(float)(C[i])#(这里是pij有的'的没办法描述而已)
            #检查均相邻的节点
            for k in m[j]:
                if i in m[k]:
                    temp+=(Q[k]/C[i])*(Q[j]/C[k])
            res[i] += temp*temp
            temp = 0.0
#         if res[i]==0.0:
#             print "有res是0,节点标号"+str(i)

       
    table = {}
    for i in range(len(res)):
        table[i] = res[i]  
    
    '''升序排序,这里其实就相当于是按照过程二重新标号'''
    t = sorted(table.items(),key = lambda x:x[1],reverse = False)
       
#     name_number =  getname_number()
#     for item in name_number.items():
#         print item[0]+":"+item[1]
    
    #将产生的结果写入文件中把,每次计算的时候都太费时间了
    f = open("data\\data_2019_1_11\\OClink\\1893-node_ED.txt",'w')
    result = {}
    '''排序前十的节点'''
    for i in range(N):
#         if str(t[i][0])=='0':
#             continue
#         print name_number[str(t[i][0])]+"  " +str(t[i][1])
#         print str(t[i][0])+"  " +str(t[i][1])
        result[str(t[i][0])] = float(t[i][1])
        f.write(str(t[i][0])+","+str(t[i][1])+"\n")
    
    f.close()
    return result 
     
       
if __name__=="__main__":
    result = getTarget()
#     for key in result.keys():
#         print str(key)+":"+str(result[key])
     
     
     
     
     
     
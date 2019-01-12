# encoding: utf-8


#排序的函数
# fp = open("data\\data_2018-12-26\\soc-Epinions1_Ti.txt",'r')
# data = {}
# for line in fp.readlines():
#     datas = line.strip().split(",")
#     num1 = int(datas[0])
#     num2 = float(datas[1])
#     data[num1]=num2
# fp.close()
# t = sorted(data.items(),key = lambda x:x[1],reverse = False)
# f = open("data\\data_2018-12-26\\soc-Epinions1_Ti_paixu.txt",'w')
# '''排序前十的节点'''
# for i in range(len(t)):
#     f.write(str(t[i][0])+","+str(t[i][1])+"\n")
# f.close()

'''
获取个指标的前10的节点
'''
def getTop10():
    fp = open("data\\data_2019_1_11\\wiki-vote\\7066-node_name_number.txt",'r')
    k=-1
    res = {}
    for line in fp.readlines():
        k=k+1
        if k==0:
            continue
        line = line.strip()
        #还是一个一个的来吧
        datas = line.split(",")
        num = int(datas[0])
        value = float(datas[3])
        res[num]=value
    '''升序排序,这里其实就相当于是按照过程二重新标号'''
    '''reverse = True表示是降序排序'''
    t = sorted(res.items(),key = lambda x:x[1],reverse = True)
    for i in range(10):
        print str(t[i][0])+","+str(t[i][1])         
    
      
'''
节点不是按照0,1,2,,,,排序的,重新将节点进行排序
'''

def prepareName_name():
    fp = open("data\\data_2019_1_11\\wiki-vote\\7066-nodes.csv",'r')
    fp1 = open("data\\data_2019_1_11\\wiki-vote\\7066-nodes_name_number.txt",'w')
    i=-1
    j=0
    for line in fp.readlines():
        #跳过行标
        i+=1
        if i==0:
            continue
        fp1.write(str(j)+","+line)
#         line = line.strip()
#         data = line.split(",")
#         id = int(data[0])
#         fp1.write(str(j)+","+str(id)+"\n")
        j+=1
    fp.close()
    fp1.close()


def prepareNumber_number():
    fp = open("data\\data_2019_1_11\\wiki-vote\\7066-edges.csv",'r')
    fp1 = open("data\\data_2019_1_11\\wiki-vote\\7066-nodes_name_number.txt",'r')
    fp2 = open("data\\data_2019_1_11\\wiki-vote\\7066-nodes_number_number.txt",'w')
    name_number = {}
    k=-1
    for line in fp1.readlines():
        k=k+1
        if k==0:
            continue
        line = line.strip()
        data = line.split(",")
        id = int(data[0])
        name = int(data[1])
        name_number[name] = id
#     for item in name_number.iteritems():
#         print str(item[0])+","+str(item[1])
        
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
    
if __name__=="__main__":
#     prepareName_name()
#     prepareNumber_number()
    getTop10()  
    
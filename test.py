# encoding: utf-8


# fp = open('data\\number_number.txt','r')
# fp1 = open('data\\number_number_buchong.txt','w')
# for line in fp.readlines():
#     line = line.strip()
#     datas = line.split("--&&--")
#     num1 = datas[1]
#     num2 = datas[0]
#     fp1.write(num1+"--&&--"+num2+"\n")
# fp1.close()
# fp.close()
# 
# a = [12,3,4,4,4,5,5,6,6,6,6,7,7,7,7]
# s = list(set(a))
# print s
# 
# print str(0.0034232/99887766553987897942342)

# fp = open("data\\number_number_xiuzheng.txt",'r')
# fp1 = open("data\\number_number_xiuzheng_buzhong.txt",'w')
# for line in fp.readlines():
#     line = line.strip()
#     datas = line.split("--&&--") 
#     num1 = datas[1]
#     num2 = datas[0]
#     fp1.write(num1+"--&&--"+num2+"\n")
# fp1.close()
# fp.close()

# t = {1:2,3:"4"}
# for item in t.items():
#     print str(item[0])
#     print str(item[1])

# a = [1,2,3,4,3,5,6]
# b = [5,6,7,8,4,5,6,8]
# c = []
# c.extend(list(set(b)))
# print c
# c.extend(list(set(a)))
# print c

# N = 10
# # N = 16
# 
# res = [0 for i in range(N)]
# print res

# fp = open("data\\Twitter mentions and retweets_\\duibishiyong.csv")
# i=0
# du = {}
# for line in fp.readlines():
#     if i==0:
#         i+=1
#         continue
#     i+=1
#     line = line.strip()
#     data = line.split(",")
#     index = int(data[0])
#     d = int(data[1])
#     du[index]=d
# 
# fp.close() 
# '''降序排序,这里其实就相当于是按照过程二重新标号'''
# t = sorted(du.items(),key = lambda x:x[1],reverse = True)
# 
# fp = open("data\\Twitter mentions and retweets_\\du_qian10.txt",'w')
# for i in range(10):
#     index = t[i][0]
#     fp.write(str(index)+'\n')
# fp.close()

# import pickle
# pkl_file = open('data\\Twitter mentions and retweets_\\biaohao.pkl', 'rb')
# data = pickle.load(pkl_file)
# 
# fp = open("data\\Twitter mentions and retweets_\\biaohao.txt",'w')
# for item in data:

# node = [i for i in range(10)]
# node.remove(8)
# print node
# n = [1,2,3]
# node.extend([])
# print node
#     fp.write(str(item[0])+"\n");

# list = [1, 2, 3, 4, 5]
# print ''.join(str(s) for s in list if s not in [None])
# 
# print 1600*0.3

# n = [0 for i in range(10)]
# print n

# A = {}
# fp = open("data\\newdata\\2220\\name_number.txt",'r')
# #先读入所有节点
# for line in fp.readlines():
#     line = line.strip()
#     data = line.split(",")
#     index = int(data[0])
#     name = data[1]
#     A[index] = name
#     
# fp.close()
# 
# B = [1720,552,1392,86,1924,677,548,2039,1298,554]
# for id in B:
#     print str(A.get(id))


# for t in range(10):
#     print t
#     
# for v in xrange(10):
#     print v


# a =  [("c",1)]
# a.append(("c",2))
# print a[0]
# print a
# 
# for i in range(15):
#     print i
#     
# c = [1,2,3]
# t = c.pop(0)
# print c
# print t

# def a():
#     v=[False,False,False]
#     return v
# 
# def b(v):
#     v[0]=True
#     return v
# 
# if __name__=="__main__":
#     v = a()
#     c = b(v)
#     print c

a = [1,2,3]
b = [3,4,5]
a.extend(b)
print a
print (float)(4.59670757091e-05)

e={1:2,3:"4"}
print len(e)

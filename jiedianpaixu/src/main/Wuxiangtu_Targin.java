package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;


public class Wuxiangtu_Targin {
	public static int maxn = 3656;
	//����洢�ռ�̫��,ֻ��ת��Ϊ�ڽӱ�Ľṹ
	//int [][]E = new int[maxn][100];
	static int []vis = new int[maxn];
	static int []dfn = new int[maxn];
	static int []low = new int[maxn];
	static int []father = new int[maxn];
	static int []subnets = new int[maxn];
	static int nodes;
	static int deep;
	static int rson;
	//�ڽӱ�
	static HashMap<Integer,ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
	
	public void init() throws Exception{
		low[1]=dfn[1]=1;
//		low[2845]=dfn[2845]=1;
		deep=1;rson=0;
		//��ǳ�ʼ�ڵ��Ѿ�������
		vis[1]=1;
//		File file = new File("data\\number_number_xiuzheng_buchong.txt");
//		File file = new File("data\\OClinks_w-1893_xiuzheng.txt");
//		File file = new File("data\\Twitter mentions and retweets_\\number_number.txt");
		File file = new File("data\\test.txt");
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		String str = "";
		while((str = br.readLine())!=null){
			str = str.trim();
			String []ss = str.split(",");
			int num1 = Integer.parseInt(ss[0]);
			int num2 = Integer.parseInt(ss[1]);
			if(map.containsKey(num1)){
				map.get(num1).add(num2);
			}else{
				ArrayList<Integer> list = new ArrayList<Integer>();
				list.add(num2);
				map.put(num1, list);
			}
			
//			if(map.containsKey(num2)){
//				map.get(num2).add(num1);
//			}else{
//				ArrayList<Integer> list = new ArrayList<Integer>();
//				list.add(num1);
//				map.put(num2, list);
//			}
		}
		nodes = map.size();
		return ;
	}

	public static void dfs(int u,int Father)
	{
		father[u] = Father;
		dfn[u]=low[u]=deep++;
		for(int v=0;v<nodes;v++)
		{
			if(map.get(u).contains(v))
			{
				if(vis[v]==0)
				{
					//��ǽڵ��Ѿ�������
					vis[v]=1;
					//��һ������������ڵ�ʱ,��ʼ��dfn,low
					dfs(v,u);
					//����֮��ά��low,low[u] = min(low[u],low[v])
					low[u]=Math.min(low[u],low[v]);
					if(low[v]>=dfn[u])
					{
						if(u==1) rson++;
						else subnets[u]++;
					}
				}
				else low[u]=Math.min(low[u],dfn[v]);
			}
		}
		return ;
	}

	public static void main(String[] args) throws Exception {
		Tree t = new Tree();
		t.init();
//		System.out.println(nodes);
		//����ѡ��һ����Ź������ֵ����б���
//		dfs(2845);
		dfs(1);
		if(rson>=2) subnets[1]=rson-1;
		for(int i=0;i<nodes;i++)
		{
			if(subnets[i]!=0)
			{
				System.out.println("SPF node "+i+" leaves "+subnets[i]+1+" subnets ");
			}
		}

	}
}

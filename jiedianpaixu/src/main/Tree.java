package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;


public class Tree {
	public static int maxn = 3656;
	//所需存储空间太大,只能转换为邻接表的结构
	//int [][]E = new int[maxn][100];
	static int []vis = new int[maxn];
	static int []dfn = new int[maxn];
	static int []low = new int[maxn];
	static int []subnets = new int[maxn];
	static int nodes;
	static int deep;
	static int rson;
	//邻接表
	static HashMap<Integer,ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
	
	public void init(int rootIndex) throws Exception{
		//标记初始节点已经搜索过
		vis[rootIndex]=1;low[rootIndex]=dfn[rootIndex]=1;
//		low[2845]=dfn[2845]=1;
		deep=1;rson=0;
//		File file = new File("data\\number_number_xiuzheng_buchong.txt");
//		File file = new File("data\\OClinks_w-1893_xiuzheng.txt");
		File file = new File("data\\Twitter mentions and retweets_\\number_number.txt");
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
			
			if(map.containsKey(num2)){
				map.get(num2).add(num1);
			}else{
				ArrayList<Integer> list = new ArrayList<Integer>();
				list.add(num1);
				map.put(num2, list);
			}
		}
		nodes = map.size();
		return ;
	}

	public static void dfs(int u)
	{
		for(int v=0;v<=nodes;v++)
		{
			if(map.get(u).contains(v))
			{
				if(vis[v]==0)
				{
					//标记节点已经搜索过
					vis[v]=1;
					++deep;
					//第一次搜索到这个节点时,初始化dfn,low
					dfn[v]=low[v]=deep;
					dfs(v);
					//回溯之后维护low,low[u] = min(low[u],low[v])
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
	
	public static ArrayList<Integer> getBiaohao() throws Exception{
		ArrayList<Integer> list = new ArrayList<Integer>();
		File file = new File("data\\Twitter mentions and retweets_\\biaohao.txt");
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		String str = "";
		while((str = br.readLine())!=null){
			str = str.trim();
			int num = Integer.parseInt(str);
			list.add(num);
		}
		br.close();
		return list;
	}

	public static void main(String[] args) throws Exception {
		Tree t = new Tree();
		int rootIndex = 2845;
		t.init(rootIndex);
		//这里选择一个标号过的最大值点进行遍历
		dfs(rootIndex);
		ArrayList<Integer> list = new ArrayList<Integer>();
		ArrayList<Integer> list_top10 = new ArrayList<Integer>();
		//list_top10.add(rootIndex);
		if(rson>=2) subnets[1]=rson-1;
		for(int i=0;i<nodes;i++)
		{
			if(subnets[i]!=0)
			{
				//System.out.println("SPF node "+i+" leaves "+subnets[i]+1+" subnets ");
				list.add(i);
			}
		}
		//System.out.println(list.size());  171
		ArrayList<Integer> biaohao = getBiaohao();
		//System.out.println(biaohao.size()); 3656
		for(int i=0;i<biaohao.size();i++){
			int num = biaohao.get(i);
			if(list.contains(num)){
				list_top10.add(num);
				if(list_top10.size()>=10){
					break;
				}
			}		
		}
		for(int i=0;i<list_top10.size();i++){
			System.out.println(list_top10.get(i));
		}

	}
}

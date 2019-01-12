package util;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

import domain.Point;


public class ReadUtils {
	private static String path;

	public ReadUtils(String path) {
		super();
		this.path = path;
	}
	
	public ArrayList<Point> read(ArrayList<Point> list){
		try {
			File file = new File(path);
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String str = "";
			//跳过标题栏
			br.readLine();
			while((str = br.readLine())!=null){
				String []args = str.split(","); 
				String id = args[0];
				String from_id = args[1];
				String to_id = args[2];
				String from_type = args[3];
				String to_type = args[4];
				String share_time = args[5];
				String read_time = args[6];
				String time_diff = args[7];
				String article_id = args[8];
				String link_type = args[9];
				Point p = new Point(id, from_id, to_id, from_type, to_type, share_time, read_time, time_diff, article_id, link_type);
				list.add(p);
			}
			return list;			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}
	
	
	public static void tran_name_number(){
		try {
			File file = new File(path);
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String str = "";
			File newfile = new File("data\\name_zong_number.txt");
			//跳过标题栏
			br.readLine();
			HashSet<String> set = new HashSet<String>();
			while((str = br.readLine())!=null){
				String []args = str.split(","); 
				String from_id = args[1];
				String to_id = args[2];
				set.add(from_id);
				set.add(to_id);
			}
			Iterator<String> it = set.iterator();
			System.out.println("一共有:"+set.size()+"个节点");
			FileWriter fw = new FileWriter(newfile);
			for(int i=0;i<set.size();i++){
				String s =i+","+it.next();
				fw.write(s+"\n");
			}
			fw.close();
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	
	public static void tran_number_number(){
		try {
			File file = new File("data\\name_zong_number.txt");
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String str = "";
			//跳过标题栏
			br.readLine();
			//先加载所有的用户
			ArrayList<String> list = new ArrayList<String>();
			while((str = br.readLine())!=null){
				String []ss = str.split(",");
				String name = ss[1];
				list.add(name);
			}
			System.out.println(list.size());
			br.close();
			File newfile = new File("data\\number_number.txt");
			FileWriter fw = new FileWriter(newfile);
			File file1 = new File("data\\原始数据-247712条.csv");
			FileReader fr1 = new FileReader(file1);
			BufferedReader br1 = new BufferedReader(fr1);
			br1.readLine();
			while((str = br1.readLine())!=null){
				String []ss = str.split(",");
				String name1 = ss[1];
				String name2 = ss[2];
				int num1 = list.indexOf(name1);
				int num2 = list.indexOf(name2);
				String s = num1+"--&&--" +num2;
				fw.write(s+"\n");
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void tran_() throws IOException{
		File file = new File("data\\Twitter mentions and retweets_\\Twitter mentions and retweets");
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		String str = "";
		//把表头跳过
		br.readLine();
		HashMap<String, Integer> names = new HashMap<String, Integer>();
		int i=0;
		while((str = br.readLine())!=null){
			if(str.contains("}")){
				continue;
			}
			String []ss = str.split("\"");
			String name1 = ss[1].trim();
			//System.out.println(name1);
			String name2 = ss[3].trim();
			//System.out.println(name2);
			//String w = ss[4];
		//	String []tt = w.split("=");
			//int weight = Integer.parseInt(tt[1].split("]")[0]);
			//先把用户添加进去
			if(!names.containsKey(name1)){
				names.put(name1,i++);
				//System.out.println(name1+":"+i);
			}
			if(!names.containsKey(name2)){
				names.put(name2,i++);
				//System.out.println(name2+":"+i);
			}
		}
		br.close();
		fr.close();
		System.out.println(names.size());
		//在读取一次
		fr = new FileReader(file);
		br = new BufferedReader(fr);
		br.readLine();
		
		
		File file_ = new File("data\\Twitter mentions and retweets_\\number_number.txt");
		FileWriter fw = new FileWriter(file_);
		BufferedWriter bw = new BufferedWriter(fw);
		HashMap<String, String> name_name = new HashMap<String, String>();
		while((str = br.readLine())!=null){
			if(str.contains("}")){
				continue;
			}
			String []ss = str.split("\"");
			String name1 = ss[1].trim();
//			System.out.println(name1);
			String name2 = ss[3].trim();
			int num1 = names.get(name1);
			int num2 = names.get(name2);
			String s = num1+","+num2+"\n";
			bw.write(s);
		}
		bw.flush();
		bw.close();

		
		//先把名字和嘴硬的标号存进去
//		File file_name = new File("data\\name_number.txt");
//		FileWriter fw = new FileWriter(file_name);
//		Set<String> set = names.keySet();
//		System.out.println(set.size());
//		int j=0;
//		for(String name:set){
//			int index = names.get(name);
//			String s = index+","+name+"\n";
//			fw.write(s);
//			j++;
//			//一定要记住刷新一下,java和python的区别,不刷新会有部分数据写入不进去
//			if(j%100==0){
//				fw.flush();
//			}
//		}
//		fw.flush();
//		System.out.println(j);
	}
	
	
	
	
	public static void main(String[] args) throws Exception {
		ReadUtils r = new ReadUtils("data\\原始数据-247712条.csv");
		tran_();
	}
}

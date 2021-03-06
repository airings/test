package com.zxyairings.codelib.generic;

import java.util.*;
class GenericTreeSet 
{
	public static void main(String[] args) 
	{
		TreeSet<String> ts = new TreeSet<String>(new LenComparator());

		ts.add("abcd");
		ts.add("cc");
		ts.add("cba");
		ts.add("aaa");
		ts.add("z");
		ts.add("hahaha");


		//迭代器可以加上泛型
		Iterator<String> it = ts.iterator();

		while(it.hasNext())
		{
			String s = it.next();
			System.out.println(s);
		}
	}
}

//比较器可以加上泛型
class LenComparator implements Comparator<String>
{
	public int compare(String o1,String o2)
	{
		int num = new Integer(o2.length()).compareTo(new Integer(o1.length()));

		if(num==0)
			return o2.compareTo(o1);
		return num;
	}
}
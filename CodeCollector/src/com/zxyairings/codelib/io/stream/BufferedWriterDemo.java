package com.zxyairings.codelib.io.stream;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

/*
??????????????????????????????????????????????????????????????????

????????????????????????????????????????????????????????????

??????????????????????????????????????????????????????
newLine();

*/



class  BufferedWriterDemo
{
	public static void main(String[] args) throws IOException
	{
		//????????????????????????????????????
		FileWriter fw = new FileWriter("buf.txt");

		//?????????????????????????????????????????????????????????????????????????????????????????????????????????
		//????????????????????????????????????????????????????????????????????????????????????????????????
		BufferedWriter bufw = new BufferedWriter(fw);

		for(int x=1; x<5; x++)
		{
			bufw.write("abcd"+x);
			bufw.newLine();// win:\r\n  linux:\n  newline???????????????
			//??????????????????????????????????????????????????????flush????????????
			bufw.flush();
		}

		//??????????????????????????????????????????????????????
		//??????????????????????????????????????????????????????flush????????????
		//bufw.flush();

		//??????????????????????????????????????????????????????????????????
		bufw.close();


	}
}

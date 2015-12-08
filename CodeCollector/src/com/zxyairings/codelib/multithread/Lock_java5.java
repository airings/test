package com.zxyairings.codelib.multithread;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Lock_java5 {
	public static void main(String[] args) {
		final Business business = new Business();
		ExecutorService executor =  Executors.newFixedThreadPool(3);
		for(int i=0;i<3;i++)
		{
			executor.execute(
					new Runnable()
					{
						public void run()
						{
							business.service();
						}
					}
			
			);
		}
		executor.shutdown();
	}
	
	private static class Business
	{
		private int count;
		Lock lock = new ReentrantLock();
		public void service()
		{
			lock.lock();
			try {
				count++;
				try {
					Thread.sleep(1);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				System.out.println(count);
			} catch (RuntimeException e) {
				e.printStackTrace();
			}
			finally
			{
				lock.unlock();
			}
		}
	}		
	
}

package com.zxyairings.codelib.multithread;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ThreeThreadInTurnRunning {

	public static void main(String[] args) {
	
		new ThreeThreadInTurnRunning().init();
		
	}
	
	private void init(){
		final Business b = new Business();
		new Thread(){
			public void run(){
				for(int i=0;i<50;i++)
					b.main();
			}
			
		}.start();
		new Thread(){
			public void run(){
				for(int i=0;i<50;i++)				
					b.sub();
			}			
		}.start();
		
		new Thread(){
			public void run(){
				for(int i=0;i<50;i++)				
					b.sub2();
			}			
		}.start();		
	}

	private class Business{
		int status = 1;
		Lock lock = new ReentrantLock();
		Condition cond1 = lock.newCondition();
		Condition cond2 = lock.newCondition();
		Condition cond3 = lock.newCondition();		
		public  void main(){
			lock.lock();
					while(status != 1){
						try{cond1.await();}catch(Exception e){}
					}
					for(int i=1;i<=5;i++){
						try{Thread.sleep(200);}catch(Exception e){}
						System.out.println(Thread.currentThread().getName() + ":" + i);
					}
					status = 2;
					cond2.signal();
			lock.unlock();
		}
		
		public  void sub(){
			lock.lock();			
					while(status != 2){
						try{cond2.await();}catch(Exception e){}
					}
					for(int i=1;i<=10;i++){
						try{Thread.sleep(200);}catch(Exception e){}
						System.out.println(Thread.currentThread().getName() + ":" + i);
					}
					status = 3;
					cond3.signal();
			lock.unlock();
		}
		
		public  void sub2(){
			lock.lock();	
					while(status != 3){
						try{cond3.await();}catch(Exception e){}
					}
					for(int i=1;i<=10;i++){
						try{Thread.sleep(200);}catch(Exception e){}
						System.out.println(Thread.currentThread().getName() + ":" + i);
					}
					status = 1;
					cond1.signal();
			lock.unlock();
		}		
	}
}

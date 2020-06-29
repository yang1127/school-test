package user;

import car.Audi;
import car.Cars;
import car.QQ;
import factory.CarFactory;

public class Driver {
	
	//驾驶车辆
	public void driver() {
		
		//代码的问题点：如果需要修改车辆，那么驾驶类的代码需要频繁的修改
		//代码违背了面向对象的设计原则：OCP(开闭:对扩展开放，对修改关闭)原则
		//设计模式:一套固定的套路
		//工厂模式(简单工厂模式)
		//Audi au = new Audi();
		//System.out.println("驾驶员驾驶：" + au);
		
		//QQ qq = new QQ();
		//System.out.println("驾驶员驾驶：" + qq);
		
		Cars au = CarFactory.createCar("au");
		System.out.println("驾驶员驾驶：" + au);
		
		Cars qq = CarFactory.createCar("qq");
		System.out.println("驾驶员驾驶：" + qq);
	}
}

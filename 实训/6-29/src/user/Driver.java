package user;

import car.Audi;
import car.Cars;
import car.QQ;
import factory.CarFactory;

public class Driver {
	
	//��ʻ����
	public void driver() {
		
		//���������㣺�����Ҫ�޸ĳ�������ô��ʻ��Ĵ�����ҪƵ�����޸�
		//����Υ���������������ԭ��OCP(����:����չ���ţ����޸Ĺر�)ԭ��
		//���ģʽ:һ�׹̶�����·
		//����ģʽ(�򵥹���ģʽ)
		//Audi au = new Audi();
		//System.out.println("��ʻԱ��ʻ��" + au);
		
		//QQ qq = new QQ();
		//System.out.println("��ʻԱ��ʻ��" + qq);
		
		Cars au = CarFactory.createCar("au");
		System.out.println("��ʻԱ��ʻ��" + au);
		
		Cars qq = CarFactory.createCar("qq");
		System.out.println("��ʻԱ��ʻ��" + qq);
	}
}

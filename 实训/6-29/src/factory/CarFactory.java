package factory;

import car.Audi;
import car.BMW;
import car.Cars;
import car.QQ;

public class CarFactory {
	
	public static Cars createCar(String carName) {
		
		if("au".equals(carName)) {
			return new Audi();
		}
		if("bmw".equals(carName)) {
			return new BMW();
		}
		if("qq".equals(carName)) {
			return new QQ();
		}
		return null;
	}

}

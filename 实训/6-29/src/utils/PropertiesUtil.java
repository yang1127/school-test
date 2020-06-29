package utils;

import java.io.FileInputStream;
import java.util.Properties;

public class PropertiesUtil {

	private static String car;

	public static String read() {
		Properties prop = new Properties();
		try {
			FileInputStream fis = new FileInputStream("config.properties");
			prop.load(fis);
			String car = (String) prop.get("car");
			//System.out.println(car);
			return car;
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			return null;
		}
	}
	
	public static void main(String[] args) {
		PropertiesUtil.read();
	}
}

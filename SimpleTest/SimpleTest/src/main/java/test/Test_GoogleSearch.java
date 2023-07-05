package test;

import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Test_GoogleSearch {

	public static void main(String[] args) {
		googlesearch();
		
		// TODO Auto-generated method stub

	}
	
	public static void googlesearch() {
		
		
		WebDriverManager.chromedriver().setup(); 
		ChromeDriver driver = new ChromeDriver(); //Chrome setup
		
		driver.get("https://www.google.com/");//go to google
		
		driver.findElement(By.xpath("//*[@name='q']")).sendKeys("junit");//enter text
		
		driver.findElement(By.xpath("//*[@class='gNO89b']")).click();//Click Search button.
		
		driver.close();//close browser
		
		
	}

}


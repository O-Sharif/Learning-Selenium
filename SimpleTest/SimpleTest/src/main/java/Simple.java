
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;


public class Simple {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//System.setProperty("Webdriver.chrome.dirver","C:\\Users\\user\\Downloads\\chromedriver_win32 (1)");
		WebDriverManager.chromedriver().setup(); 
		WebDriver driver =new ChromeDriver();   //WebdriverSetup.
		
		
		driver.get("https://www.google.com/");
		
		driver.findElement(By.id("APjFqb")).sendKeys("junit");
		
		//driver.findElement(By.xpath("//*[@class='gNO89b']")).click();
		
		driver.findElement(By.xpath("//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]")).click();
		
		driver.findElement(By.xpath("(//*[@class='LC20lb MBeuO DKV0Md'])[1]")).click();
		
		
		driver.findElement(By.xpath("(//*[@class='btn btn-primary btn-lg'])[1]")).click();
		
		driver.findElement(By.linkText("PDF download")).click();
		
		//driver.close()
		
		
		

	}

}

import java.util.*;

public class Klausur02 {

	public static void main(String[] args) {
		Scanner eingabe = new Scanner (System.in);
		
		int n = eingabe.nextInt();
		
		for(int i = 1; i<=n;i ++) {
			
			 if (i%2 <= n) {     
				 
				 System.out.print(i+n);
			 }
			 else {
				 (i%3 <= n);
				 System.out.print(i-n);		 
			 }
		}
	}

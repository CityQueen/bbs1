package N;

import java.util.Scanner;
public class N {

	public static void main(String[] args) {
		
		final int ENDE = 0;
		boolean ende = false;
		
		 
		  Scanner eingabe = new Scanner(System.in);
		 
		  do {
			  System.out.print("\nSekunden : ");
			  int sekunden = eingabe.nextInt();
			  if (sekunden > ENDE) {
				  int tage = sekunden / (24 * 60 * 60);
				  sekunden = sekunden % (24 * 60 * 60);   // der Rest
				  int stunden = sekunden / (60 * 60);
				  sekunden = sekunden % (60 * 60);  // der Rest
				  int minuten = sekunden / 60;
				  sekunden = sekunden % 60;  // der Rest
				  System.out.println(" Tage     = " + tage);
				  System.out.println(" Stunden  = " + stunden);
				  System.out.println(" Minuten  = " + minuten);
				  System.out.println(" Sekunden = " + sekunden);
		  }
		  else {
			  System.out.println("Good Bye.");
			  ende = true;
		  }
	  } while(!ende); 
	}

}

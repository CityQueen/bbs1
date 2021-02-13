import java.util.*;

public class Aufgabe05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner eingabe = new Scanner (System.in);
		
		System.out.println("Gib eine Zahl an: ");
		int n = eingabe.nextInt();
		
		int summe = 0;
		for(int i=0; i<= n; i++) {
			
			if (i%2==0 ) {
				summe = summe + n;
			}
			else {
				summe = summe - n;
			}
			
		}
		System.out.println("Das Ergebniss ist: " + summe);
		
		
	}

}

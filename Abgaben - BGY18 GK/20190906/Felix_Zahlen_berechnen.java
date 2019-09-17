package Jean;

import java.util.*;

public class Zahlen_berechnen {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner eingabe = new Scanner (System.in);
		
		System.out.println("Bitte Zahl 1 eingeben:");
		System.out.println("Bitte Zahl 2 eingeben:");
		System.out.println("Bitte Zahl 3 eingeben:");
		
		int Zahl1 = eingabe.nextInt();
		int Zahl2 = eingabe.nextInt();
		int Zahl3 = eingabe.nextInt();
		
		int Summe1 = Zahl1 + Zahl2 + Zahl3;
		
		System.out.println("Die Summe lautet: " + Summe1);
		
		System.out.println("Bitte noch eine weitere Zahl eingeben:");
		
		int Zahl4 = eingabe.nextInt();
		
		int Summe2 = Zahl4 * Summe1;
		
		System.out.println("Das Produkt lautet " + Summe2);
		
	}

}

package unterricht_3;

import java.util.Scanner;

public class Eingabe_von_Zahlen {

	public static void main(String[] args) {
	
		Scanner eingabe = new Scanner (System.in);
		
		System.out.println("Zahl 1 eingeben");
		System.out.println("Zahl 2 eingeben");
		System.out.println("Zahl 3 eingeben");
		
		int Zahl1 = eingabe.nextInt();
		int Zahl2 = eingabe.nextInt();
		int Zahl3 = eingabe.nextInt();
		
		int Ergebnis = Zahl1 + Zahl2 + Zahl3;
		
		System.out.println("Das Ergebnis lautet:" + Ergebnis);
		
		System.out.println("eine weitere Zahl eingebemn:");
		
		int Zahl4 = eingabe.nextInt();
		int ergebnis2 = Zahl4 * Ergebnis;
		
		System.out.println("Ergebnis2");
		
		

	}

}

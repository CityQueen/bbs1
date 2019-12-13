package Jean;

import java.util.*;

public class Grundrechnen1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner eingabe = new Scanner(System.in);
		
		System.out.println("Bitte geben sie eine Basis ein:");
		System.out.println("Bitte geben sie eine Potenz ein:");
		
		int Basis = eingabe.nextInt();
		int Potenz = eingabe.nextInt();
		
		System.out.println("Das Ergebnis (Basis hoch Potenz) lautet: " + (int)(Math.pow(Basis, Potenz)));
		System.out.println("Das andere Ergebnis (Potenz hoch Basis) lautet: " + (int)Math.pow(Potenz, Basis) );
		
		
		
		
		
	}

}

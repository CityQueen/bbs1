package unterricht_3;

import java.util.Scanner;

public class Zahlen_einlesen {

	public static void main(String[] args) {
		
	Scanner eingabe = new Scanner (System.in);
	
	System.out.println (" ,)     (;    trage fünf Kommazahlen ein:    ;)     (,   ");
	
	double eins = eingabe.nextDouble();
	double zwei = eingabe.nextDouble();
	double drei = eingabe.nextDouble();
	double vier = eingabe.nextDouble();
	double fünf = eingabe.nextDouble();
	
	System.out.println(" (;  hier sind die Kommezahlen rückwärts ausgeben  ;) " + fünf + " " + vier + " " + drei + " " + zwei + " " + eins);
	
	

	}

}

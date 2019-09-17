package aufgabe;

import java.util.Scanner;

public class aufgabe {

	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		
		double z1, z2, z3, z4, z5;
		
		System.out.println("Geben Sie fünf Kommazahlen ein");
		z1 = eingabe.nextDouble();
		z2 = eingabe.nextDouble();
		z3 = eingabe.nextDouble();
		z4 = eingabe.nextDouble();
		z5 = eingabe.nextDouble();
		
		System.out.println(z5 + " " + z4 + " " + z3 + " " + z2 + " " + z1);
		
	}

}

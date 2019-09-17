package aufgabe;

import java.util.Scanner;

public class aufgabe2 {

	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		
		double z1, z2, z3;
		
		System.out.println("Geben Sie drei Kommazahlen ein");
		z1 = eingabe.nextDouble();
		z2 = eingabe.nextDouble();
		z3 = eingabe.nextDouble();
		
		
		System.out.println( z3 + z2 + z1 );
		
		
		double z4;
		System.out.println(" Geben Sie eine weitere Zahl ein");
		z4 = eingabe.nextDouble();
		
		System.out.println( (z1 + z2+ z3) * z4 );
	}

}
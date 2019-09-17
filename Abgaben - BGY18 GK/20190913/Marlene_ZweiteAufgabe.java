package javazweiteklase;

import java.util.Scanner;

public class ZweiteAufgabe {

	public static void main(String[] args) {
		
		Scanner eingabe = new Scanner (System.in);
	
		int z1, z2, z3;
		System.out.println("Geben sie Zahl 1 Ein");
		z1 = eingabe.nextInt();
		System.out.println("Geben sie Zahl 2 Ein");
		z2 = eingabe.nextInt();
		System.out.println("Geben sie Zahl 3 Ein");
		z3 = eingabe.nextInt();
		
		int z4 = z1 + z2 + z3;
		
		System.out.println("Die Summe lautet" + z4);
		Scanner eingabe2 = new Scanner(System.in);
		int z5;
		System.out.println("Geben sie eine weitere Zahl ein:");
		z5 = eingabe.nextInt();
		int z6 = z5 * z4;
		System.out.println("Die Summe ist:" + z6 );
		

	}

}

import java.util.*;

public class Aufgabe04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// System.out.print("Geben sie eine Ganzzahlie Obergrenze ein");
		/*
		 * Scanner eingabe = new Scanner(System.in); int a = eingabe.nextInt(); Scanner
		 * eingabe = new Scanner(System.in); int b = eingabe.nextInt();
		 * 
		 * a = a + b;
		 * 
		 */
		Scanner eingabe = new Scanner(System.in);
		System.out.print("Geben sie eine Ganzzahlie Obergrenze ein:");
		int Obergrenze = eingabe.nextInt();

		for (int i = 1; i < Obergrenze; i = i + 2) {
			System.out.print("Die Summe " + i + " ergibt sich aus" + " " + "ungeraden Zahlen ");

		}
	}
}
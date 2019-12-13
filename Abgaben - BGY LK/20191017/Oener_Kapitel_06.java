import java.util.*;
public class Kapitel_06 {

	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		double c;
		double f;
		
		System.out.println("Geben sie ein Celsiuswert ein");
		c = eingabe.nextDouble();
		
		f = umrechnung(c);
		
		System.out.println("Die Temperatur in Fahrenheit beträgt " + f);

	}
	
	public static double umrechnung (double c){
		double f = (c * 9 / 5) + 32;
		return f;
	}

}

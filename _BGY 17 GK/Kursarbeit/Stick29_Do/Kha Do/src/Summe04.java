import java.util.*;

public class Summe04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

Scanner eingabe = new Scanner (System.in);
		
		System.out.println ("Geben Sie eine Obergrenze an:");
		int Obergrenze = eingabe.nextInt();
		
		int s=0;
		int a=0;
	for (int i=1; i<Obergrenze; i=i+2) {
		
		a++;
		s=s+i;
	}
	System.out.println ("Die Summe " +s+ " ergibt sich als Summe aus " +a+" ungeraden Zahlen");
	}
}
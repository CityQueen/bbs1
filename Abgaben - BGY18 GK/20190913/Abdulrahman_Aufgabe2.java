import java.util.Scanner;

public class Aufgabe2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		
		Scanner eingabe =new Scanner (System.in);
		
		double t1, t2, t3, t4, x1;
		
		System.out.println("bitte geben Sie drei Zahlen ein:");
		
		t1=eingabe.nextDouble();
		t2=eingabe.nextDouble();
		t3=eingabe.nextDouble();
		
		System.out.println( t1 + t2 + t3 );
		
		System.out.println ("bitte geben Sie eine weitere Zahl ein: ");
		x1=t1 + t2 +t3; 
		t4=eingabe.nextDouble();
		System.out.println( x1*t4);
		System.out.println();
		
		
	
		
		
		
		
		
		
		
		
		
	}

}

import java.util.*;

public class aufgabe4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner eingabe = new Scanner(System.in);
		int a,i;
		int b;		 
		System.out.println("bitte geben sie eine ganzzahlige Obergrenze ein");
		a = eingabe.nextInt();
		for (i=1; i<=a; i+2) {
			b = b + 2;
		}
		System.out.println("Die Summe " +a+ " ergibt sich als Summe aus " +b + " ungeraden Zahlen");
	}
}

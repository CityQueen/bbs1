import java.util.*;

public class Obergrenze {
	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		System.out.println("Bitte geben sie eine Obergrenze ein:");
		int a = eingabe.nextInt();
		int i = 1;
		int b = 0;
		int c = 0;
		do {
			b = b + 2;
			i = i + 2;
			c++;
		} while (i < a);
		if (a % 2 == 1) {
			int e = c - 1;
			System.out.println("Die Summe " + a + " ergibt sich als Summe aus " + e + " ungeraden Zahlen");
		} else {
			int d = a - 1;
			int f = c - 1;
			System.out.println("Die Summe " + d + " ergibt sich als Summe aus " + c + " ungeraden Zahlen");
		}
	}
}
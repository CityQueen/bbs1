import java.util.Scanner;

public class Aufgabe04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner obergrenze = new Scanner(System.in);

		System.out.println("Geben sie eine ganzahlige obergrenze an:");

		int a = obergrenze.nextInt();
		int summe = 0;
		for (int b = 1; b <= a; b++) {
			if (b % 2 > 0) {
				summe = summe + b;
			} else {

			}
		}

		if (a % 2 > 0) {
			System.out.println("die Anzahl der summanden ist: " + (a / 2 + 1));
		} else {

			System.out.println("die Anzahl der summanden ist :" + a / 2);
		}

		System.out.println("die summe aller ungeraden zahlen ist:" + summe);

	}
}
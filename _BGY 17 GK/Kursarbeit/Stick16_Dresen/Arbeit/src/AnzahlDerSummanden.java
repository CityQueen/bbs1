import java.util.*;

public class AnzahlDerSummanden {
	public static void main(String[] args) {
		Scanner name = new Scanner(System.in);
		System.out.println("bitte geben Sie eine ganzzahlige obergrenze an:");
		int a = name.nextInt();
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
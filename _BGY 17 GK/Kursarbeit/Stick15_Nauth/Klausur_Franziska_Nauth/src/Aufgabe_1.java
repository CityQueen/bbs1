import java.util.*;

public class Aufgabe_1 {

	public static void main(String[] args) {
		System.out.println("Geben Sie eine Zahl ein!");
		Scanner eingabe = new Scanner(System.in);
		int x = eingabe.nextInt();
		int y;
		int s = 0;
		for (y = 1; y <= x; y++) {
			int c = y % 2;
			if (c > 0) {
				y = 0 + y;
				s = s + y;
				System.out.print(s);

			}
		}
	}
}
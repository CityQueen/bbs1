import java.util.*;

public class Aufagbe_5 {

	public static void main(String[] args) {
		System.out.println("Geben Sie eine Zahl ein");
		Scanner eingabe = new Scanner(System.in);
		int n = eingabe.nextInt();
		int y;
		for (y = 1; y <= n; y++) {
			int h = y + 1;
			System.out.print(h);
			if (y % 2 > 0) {
				int x = h + y;
			} else {
				int x = h - y;
			}

		}
	}
}
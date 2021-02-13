import java.util.*;

public class EinsBisEinschlieﬂlich {
	public static void main(String[] args) {
		Scanner name = new Scanner(System.in);
		System.out.println("geben sie die zahl an:");
		int a = name.nextInt();
		int summe = 0;
		System.out.print("rechnet man");
		for (int b = 1; b <= a; b++) {
			if (b % 2 > 0) {
				summe = summe - b;
				System.out.print(summe);
			} else {
				summe = summe + b;
				System.out.print(summe);
			}
		}
		System.out.println("erh‰lt man :" + summe);
	}
}

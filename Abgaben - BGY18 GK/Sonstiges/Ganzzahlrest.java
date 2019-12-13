package projekt1;

import java.util.Scanner;

public class Ganzzahlrest
{

	public static void main(String[] args)
	{
		int iZahl1, iZahl2, iErgebnis;
		Scanner input = new Scanner(System.in);
		System.out.print(" Geben Sie die erste Zahl ein : ");

		iZahl1 = printInt(input.nextLine());
		System.out.print(" Geben Sie die zweite Zahl ein : ");

		iZahl2 = input.nextInt();
		iErgebnis = iZahl1 + iZahl2;

		System.out.println(" Die Summe von " + iZahl1 + " und " + iZahl2
				+ " ist " + iErgebnis);

	}
}

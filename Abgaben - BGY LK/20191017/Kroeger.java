import java.util.*;

public class Mohamedy {

	public static void main(String[] args) {
		/* Aufgabe A01
		
		double BenzinP = 0.67;
		double OlP = 0.0006;
		double KM = 0;
		
		Scanner S = new Scanner(System.in);
		
		System.out.println("Wie viele KM fährst du?");
		
		KM = S.nextDouble();
		
		System.out.println("Du verbrauchst:");
		
		System.out.println(KM * BenzinP + "l Benzin");
		
		System.out.println(KM * OlP + "l Öl");
		
		*/
		
		double AutosJahr1 = 0;
		double Investition = 0;
		
		double Gewinn = 0;
		
		int Jahr = 0;
		
		boolean BereitsGewinn = false;
		
		Scanner S = new Scanner(System.in);
		System.out.println("Wie viel Investierst du?");
		Investition = S.nextDouble();
		System.out.println("Wie viele verkauftst du im Jahr 1?");
		AutosJahr1 = S.nextInt();
		
		if (AutosJahr1 == 0) {
			System.out.println("So wird das nichts...");
		}
		
		while (Gewinn <= 1000000) {
			if (Jahr > 0) {
				AutosJahr1 = AutosJahr1 * 1.05;
			}
			
			Jahr++;
			
			Gewinn = Gewinn + (2500 * Math.round(AutosJahr1));
			
			if (Gewinn >= Investition && BereitsGewinn == false) {
				if (Jahr == 1) {
					System.out.println("Du machst Gewinn nach " + Jahr + " Jahr.");
				} else {
					System.out.println("Du machst Gewinn nach " + Jahr + " Jahren.");
				}
				BereitsGewinn = true;
			}
			
		}
		
		if (Jahr == 1) {
			System.out.println("Nach " + Jahr + " Jahr bist du Millionär. Yey!");
		} else {
			System.out.println("Nach " + Jahr + " Jahren bist du Millionär. Yey!");
		}
		
	}
}
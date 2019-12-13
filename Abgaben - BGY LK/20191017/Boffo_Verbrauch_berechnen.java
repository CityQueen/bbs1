import java.util.*;
public class Verbrauch_berechnen {

	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		
		double fs;
		
		System.out.println("Geben sie die zu fahrende Strecke in km an!");
		fs = eingabe.nextDouble();
		
		double bv = 6.7;
		double oelv = 0.6;
		
		bv = bv/10 * fs;
		oelv = oelv/1000 * fs;
		
		System.out.println("Bei der Strecke von " + fs + " km verbraucht das Auto " + bv + " Liter Benzin und " + oelv + " Liter Öl.");
		
	}

}

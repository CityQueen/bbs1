import java.util.*;
public class A01 {

	public static void main(String[] args) {
		
		Scanner eingabe = new Scanner(System.in);
		
		System.out.print("Gefahrende Strecke eingeben: ");
		double km;
		km = eingabe.nextDouble();

		double nbv, n�v, ber, �er, br, �r;
		nbv= 6.7;
		n�v= 0.6;
		
		br= km/10;
		�r= km/1000;
		
		ber= br*nbv;
		ber= Math.round(ber*100)/100.0;
		
		�er= �r*n�v;
		�er= Math.round(�er*100)/100.0;
		
		System.out.print("W�hrend der Fahrt wird "+ ber+ 
				" Liter Bezin und "+ �er+ " Liter �l"
						+ " verbraucht");
		
	}

}

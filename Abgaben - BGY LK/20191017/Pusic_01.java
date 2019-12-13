import java.util.*;
public class A01 {

	public static void main(String[] args) {
		
		Scanner eingabe = new Scanner(System.in);
		
		System.out.print("Gefahrende Strecke eingeben: ");
		double km;
		km = eingabe.nextDouble();

		double nbv, növ, ber, öer, br, ör;
		nbv= 6.7;
		növ= 0.6;
		
		br= km/10;
		ör= km/1000;
		
		ber= br*nbv;
		ber= Math.round(ber*100)/100.0;
		
		öer= ör*növ;
		öer= Math.round(öer*100)/100.0;
		
		System.out.print("Während der Fahrt wird "+ ber+ 
				" Liter Bezin und "+ öer+ " Liter Öl"
						+ " verbraucht");
		
	}

}

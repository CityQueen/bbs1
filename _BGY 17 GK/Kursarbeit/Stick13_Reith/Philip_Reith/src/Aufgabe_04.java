import java.util.*;
public class Aufgabe_04 {
	public static void main(String[] fghdfhfd) {
		Scanner uff=new Scanner(System.in);
		int o=0, s=0, a=0;
		System.out.print("Geben Sie eine Obergrenze an: ");
		o=uff.nextInt();
		for (int i=1;i<=o;i=i+2) {
			s=s+i;
			a++;
		}
		System.out.print("Die Summe "+s+" ergibt sich als Summe aus "+a+" ungeraden Zahlen.");
	}
}
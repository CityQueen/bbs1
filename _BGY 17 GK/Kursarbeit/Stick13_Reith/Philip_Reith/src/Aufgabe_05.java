import java.util.*;
public class Aufgabe_05 {
	public static void main(String[] fghdfhfd) {
		Scanner uff=new Scanner(System.in);
		int s=0, r=0, z=1, n=0;
		System.out.print("Geben Sie die Anzahl der zu verwendenden Elemente an: ");
		n=uff.nextInt();
		System.out.print("Rechnet man");
		while (z<=n){
			r=z%2;
			if (r==0) {
				s=s+z;
				System.out.print(" + "+z);
			}else if (r==1) {
				s=s-z;
				System.out.print(" - "+z);
			}
			z++;
		}
		System.out.print(" erh�lt man "+s+".");
	}
}
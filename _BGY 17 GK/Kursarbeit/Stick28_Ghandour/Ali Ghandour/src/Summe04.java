import java.util.*;
public class Summe04 {

	public static void main(String[] args) {
		Scanner Summe01 = new Scanner (System.in);
		System.out.print("geben sie eine obergrenze an");
		int y = Summe01.nextInt();
		
			int Summe = 0;
			int x;
			for(x=1;x<y;x=x+2) {
			Summe = Summe + 1;
				
			}
			System.out.print("Die Summe " +  Summe + " ergibt sich als Summe aus der ungeraden zahlen");
		
			

	}

}

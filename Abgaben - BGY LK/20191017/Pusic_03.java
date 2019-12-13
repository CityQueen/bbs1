import java.util.*;
public class A03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner eingabe= new Scanner (System.in);
		
		double ver, p= 0.045, mon;
		int n= 6 ,m= 72, ein;
		
		System.out.print("Geben sie ihr Monatliches Gehalt ein: ");
		ein= eingabe.nextInt();
		
		ver=0;
		for(int i= 1; i<m; i++){
			ver+=ein;
			if(i== 12 || i== 24 || i==36 || i==48 || i==60 || i==72) {
				ver= ver*(1+p);
				ver= Math.round(ver*100)/100.0;
			}
			System.out.println(ver);
		}
		
	}

}

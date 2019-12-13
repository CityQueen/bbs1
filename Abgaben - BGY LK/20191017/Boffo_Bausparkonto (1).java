import java.util.*;
public class Bausparkonto {

	public static void main(String[] args) {
		
Scanner eingabe = new Scanner(System.in);

	Double einzahlung;
	
	System.out.println("Was wollen sie pro Monat einzahlen?");
	einzahlung = eingabe.nextDouble();

	Double zinssatz = 4.5;
	Double ersparnis;
	Double monate = 12.0;
	
	for(int i= 1; i>monate; i++ ) {
		
	einzahlung += einzahlung;
		
	
		
	}

System.out.println(einzahlung);









	}

}

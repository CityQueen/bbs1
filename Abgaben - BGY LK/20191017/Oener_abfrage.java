import java.util.*;

public class abfrage {

	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		boolean a = true;
		boolean b = true;
		boolean c = true;
		String Name;
		int Alter;
		String MW = null;

		do {
			System.out.println("Wie Heiﬂen sie?");
			Name = eingabe.next();
			System.out.println("Sie Heiﬂen " + Name
					+ " ist das Richtig? (ja = 1 /nein = 2)");
			int jn = eingabe.nextInt();
			switch (jn) {
			case 1:
				a = true;
				break;
			case 2:
				a = false;
				break;
			default:
				a = false;
				break;
			}

		} while (a == false);
		
		do {
			System.out.println("wie alt sind sie?");
			Alter = eingabe.nextInt();
			System.out.println("Sie sind " + Alter
					+ " Jahre alt ist das Richtig? (ja = 1 /nein = 2)");
			int jn = eingabe.nextInt();
			switch (jn) {
			case 1:
				b = true;
				break;
			case 2:
				b = false;
				break;
			default:
				b = false;
				break;
			}
			
		} while (b == false);
		
		do {
			System.out.println("Sind Sie M‰nlich = 1 oder Weiblich = 2 ?");
			int jn = eingabe.nextInt();
			switch (jn) {
			case 1:
				c = true; MW = "M‰nnlich";
				break;
			case 2:
				c = true; MW = "Weiblich";
				break;
			default:
				c = false;
				break;
			}
			
		} while (c == false);
		System.out.println("Hallo " + Name + " sie sind " + MW + " und " + Alter + " Jahre alt");
	}

}

import java.util.*;

public class Verbrauch {

	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	double benzin100, oel1000, strecke2;
	benzin100 = 67;
	oel1000 = 0.6;
	strecke2 = 0;
	System.out.println("Geben sie die zu fahrende Strecke in km ein:");
	double strecke1 = input.nextInt();
	strecke2 = strecke1;
	strecke1 /= 100;
	strecke1 *= benzin100;
	strecke2 /= 1000;
	strecke2 *= oel1000;
	System.out.println("Ihr Benzinverbrauch liegt bei " + strecke1 + "L");
	System.out.println("Und ihr Ölverbrauch liegt bei " + strecke2 + "L");
	}

}

import java.util.*;
public class Pin_Eingabe {
	
	public static void main(String[] args) {
		Scanner eingabe = new Scanner(System.in);
		int counter = 3;
		int cc;
		int Passwort = 0;
		int Pweingabe;
		int Best�tigung;
		boolean Richtig = true;
		
		while(Richtig == true){
		System.out.print("Geben Sie Ihre neue PIN ein: ");
		Passwort = eingabe.nextInt();
			System.out.print("Geben Sie Ihre neue PIN nochmal ein um sie zu Best�tigen: ");
			Best�tigung = eingabe.nextInt();
			
			if(Passwort == Best�tigung){
				Richtig = false;
			} else{
				
			}
		}
			System.out.println("Ihre PIN wurde eingerichtet!");
			System.out.print("Geben Sie Ihre PIN ein um das Programm zu �ffnen: ");
		
		while(counter >= 0) {
			Pweingabe = eingabe.nextInt();
			
			if (Pweingabe == Passwort){
				System.out.println("Ihr passwort ist Richtig");
				System.out.println("hier sind die Internet seiten f�r Kuchenrezepte");
				System.out.println("https://www.chefkoch.de/rs/s0/kuchen/Rezepte.html \nhttps://www.oetker.de/kuchen-rezepte \nhttps://www.lecker.de/rezepte/kuchen");
			} else if(Pweingabe != Passwort) {
				counter--;
				System.out.println("Passwort ist Falsch sie haben noch "+ counter +" Versuche");
			}
		}	
	}
}

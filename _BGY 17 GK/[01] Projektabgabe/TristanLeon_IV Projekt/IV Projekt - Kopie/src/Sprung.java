
public class Sprung extends Thread {
	static boolean fertig = true;
	static boolean hochpunkt = false;

	int sprungh�he = 80;// max sprungh�he
	static int ursprungY = 230;// laufh�he
	static int sprungposition = ursprungY;// abfrage wo er sich gerade befindet

	public Sprung() {

	}

	public void run() {
		fertig = false;
		int verz�gerung = 3;
		while (fertig == false) {
			Sprung();
			try {
				Thread.sleep(verz�gerung);
				// durch thread wird gew�hrleistet das er beim springen nicht stoppt sondern
				// weiter l�uft
			} catch (Exception e) {

			}
		}

		hochpunkt = false;
	}

	public void Sprung() {
		// hier wird der sprung selbst gemacht , so dass er eine schrittweise kurve
		// macht
		// bei java wird von oben nach unten gez�hlt deswegen f�r hoch - und runter +

		if (hochpunkt == false) {
			sprungposition--;
		}
		if (sprungposition == (ursprungY - sprungh�he)) {
			hochpunkt = true;
		}
		if (hochpunkt == true && sprungposition <= ursprungY) {
			sprungposition++;
			if (sprungposition == ursprungY) {
				fertig = true;
			}
		}
	}
}

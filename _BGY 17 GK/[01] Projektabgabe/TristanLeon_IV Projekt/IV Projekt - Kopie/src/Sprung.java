
public class Sprung extends Thread {
	static boolean fertig = true;
	static boolean hochpunkt = false;

	int sprunghöhe = 80;// max sprunghöhe
	static int ursprungY = 230;// laufhöhe
	static int sprungposition = ursprungY;// abfrage wo er sich gerade befindet

	public Sprung() {

	}

	public void run() {
		fertig = false;
		int verzögerung = 3;
		while (fertig == false) {
			Sprung();
			try {
				Thread.sleep(verzögerung);
				// durch thread wird gewährleistet das er beim springen nicht stoppt sondern
				// weiter läuft
			} catch (Exception e) {

			}
		}

		hochpunkt = false;
	}

	public void Sprung() {
		// hier wird der sprung selbst gemacht , so dass er eine schrittweise kurve
		// macht
		// bei java wird von oben nach unten gezählt deswegen für hoch - und runter +

		if (hochpunkt == false) {
			sprungposition--;
		}
		if (sprungposition == (ursprungY - sprunghöhe)) {
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

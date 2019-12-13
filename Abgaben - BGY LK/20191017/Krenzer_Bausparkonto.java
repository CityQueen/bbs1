
public class Bausparkonto {

	public static void main(String[] args) {
		double einzahlung = 200, zinssatz = 1.045, ersparnisse = 0;
		for (double monate = 1; monate <= 72; monate++) {
			ersparnisse += einzahlung;
			if (monate == 12 || monate == 24 || monate == 36 || monate == 48 || monate == 60 || monate == 72) {
				ersparnisse *= zinssatz;
			}
		}
		ersparnisse = Math.round(ersparnisse*100)/100.0;
		System.out.print("nach 6 Jahren haben sie " + ersparnisse + "€ angespart.");
	}

}

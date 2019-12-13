public class zuweisung
{

	public static void main(String[] args)
	{
		int a = 5;
		a = a + 5; // Neuer wert wird zugewiesen
		a -= +1; // Alter Wert wird manipuliert
		System.out.println(a);

		int x = -5;
		x = x - 8;
		x = 12;
		x = --x + x--;
		x = x + x;
		x -= -1;
		System.out.println(x);

		double c = 3;
		c = c - 5;
		c /= 16;
		System.out.println(c);
	}
}
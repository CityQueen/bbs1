package aufgabe;

public class A3 {

	public static void main(String[] args) {
		// a)
		int x = 5, y = 5;
		x = x + 1; // NEUER wert wird zugewiesen
		y += 1; // ALTER Wert wird manipoliert
		System.out.println(x);
		System.out.println(y);
		
		// b)
		int a = 10;
		a -= 8;
		System.out.println(a);

		// c)
		int c = 10;
		c = 3 - c;
		System.out.println(c);
		
		// d)
		int r = 10, s = 10, t = 10;
		s *= r*t;
		System.out.println(s);
		
		// e)
		int A = 10, b = 10;
		A = 4 * b + A;
		System.out.println(A);
		
		// f)
		int z = 10, u = 10;
		z = z * 4 + u;
		System.out.println(z);
		
		// g)
		int Z = 10, U = 10;
		Z = Z * (U + 4);
		System.out.println(Z);
	}

}

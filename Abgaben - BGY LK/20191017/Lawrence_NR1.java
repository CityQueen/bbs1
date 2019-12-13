import java.util.Scanner;

public class NR1 {

    public static void main(String[] args) {
        int n;
        Scanner input = new Scanner(System.in);

        System.out.print("Bitte gib eine ganze Zahl n ein: ");
        String s = input.next();

        try {
            n = Integer.parseInt(s);
        } catch(Exception e) {
            n = 0;
            System.out.println("Die Eingabe muss eine ganze Zahl sein!");
        }

        if(n != 0) {
            if (a(n))
                System.out.println(n + " ist eine gerade Zahl.");
            else
                System.out.println(n + " ist eine ungerade Zahl.");
            b(n);
            System.out.println("Die Summe aller Zahlen von 1 bis " + n + " beträgt " + c(n) + ".");
            d(n);
            System.out.println("Die Summe aller geraden Zahlen bis " + n + " beträgt " + e(n) + ".");
        }
    }

    private static boolean a(int n) {
        return n%2 == 0;
    }

    private static void b(int n) {
        System.out.println("Alle Zahlen von 1 bis " + n + ":");
        int i = 1;
        while(i < n) {
            System.out.print(i + ", ");
            i++;
        }
        System.out.println(n);
    }

    private static int c(int n) {
        int summe = 0;

        for(int i = 1; i <= n; i++)
            summe += i;

        return summe;
    }

    private static void d(int n) {
        System.out.println("Alle geraden Zahlen bis " + n + ":");
        for(int i = 2; i <= n; i+=2) {
            if(i == n || i == (n-1))
                System.out.println(i);
            else
                System.out.print(i + ", ");
        }
    }

    private static int e(int n) {
        int summe = 0;

        for(int i = 2; i <= n; i+=2) {
            summe += i;
        }

        return summe;
    }
}

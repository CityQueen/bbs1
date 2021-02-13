package projekt;

public class Frageantwort {
	static String ri_frage = null;
	static String op1 = null; 
	static String op2 = null;
	static String op3 = null;
	static String op4 = null;
	static int lösung= 0;
	
	static quiz quiz;
	static fragen frage_klasse;
	static String akt_frage;
	
	public Frageantwort() {
		new quiz();
		neuefrage();
		
	}

	private void neuefrage() {
		// TODO Auto-generated method stub
		
	}
	public static void  neuefrage1() {
		frage_klasse= new fragen();
				akt_frage= fragen.frage; 
		parser();
	}
public static void parser() {
	String[] frage = akt_frage.split(akt_frage); 
	for (int x =0; x< frage.length;x++){ 
		
		switch(x) {
		case 0:
			ri_frage = frage[x]; 
			break;
			
		case 1:
		op1 = frage[x];
		break;
		
		case 2:
			op2 = frage[x];
			break;
			
		case 3:
			op3= frage[x];
			break;
			
		case 4:
			op4 = frage[x];
			break;
			
		case 5:
		lösung = Integer.parseInt(frage[x]); 
		break; 
			
		}
		
	}
	System.out.println(ri_frage);
			}
}

package projekt;

public class fragen {
	int zufall;
	String fragen[] = new String[19]; 
	static String frage;
	
	public fragen() {
		 fragen[1] ="Hat Kolumbus die Welt bereist??strjastrneinstr1";
		 fragen[2] = "Der erste Weltkrieg war 1914-1918Strjstrneinstr1";
		 fragen[3] = "Ist pi eine rationale Zahl?strjastrneinstr2";
		 fragen[4] = "Die Wurzel aus 2 ist 2strjastrneinstr2";
		 frage =fragen [zufall(1,5)]; 
		 
	}
	public int zufall(int min, int max) {
		zufall = (int)((max-min)*Math.random()+min); 
		
	return zufall;
			
}

}

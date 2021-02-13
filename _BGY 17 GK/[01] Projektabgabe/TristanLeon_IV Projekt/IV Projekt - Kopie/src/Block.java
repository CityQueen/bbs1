import java.awt.Color;

public class Block {
	
	final int X , Y;//für Koordinaten des Blocks
	final int WIDTH, HIGHT;//für weite höhe des blocks
	boolean coin = false;
	final Color COLOR;//für die Farbe des Blocks
	
	public Block(int p_x, int p_y, int p_width, int p_higth, Color p_color ) {
		X= p_x;
		Y= p_y;
		WIDTH= p_width;
		HIGHT = p_higth;
		COLOR =p_color;
		
		
	}
	
	public boolean Kolisionsabfrage(int x_block, int y_block, int x_char, int y_char) {
		//also um zu bestimmen wann der char den block trifft o. überhaupt treffen kann
		//Bedingung x von anfang cha > als anfang block und x ende char < ende block
		
		if(x_char >= x_block && y_char>= y_block && y_char<= y_block+HIGHT) {
			
			if(x_char<= x_block+WIDTH){
			coin = true;
			return true;
				
			}else {
				
				if(x_char-40<= x_block+WIDTH) {
				coin = true;
				return true;
					
				}
			}
			
		}else {
			return false;
		}
	return false;	
		
		
	}
	
	
	public int getX_Block() {
		return X;
	}
	
	public int getY_Block() {
		return Y;
	}
	
	public int getWidth() {
		return WIDTH;
	}
	
	public int getHight() {
		return HIGHT;
	}
	
	public Color getFarbe() {
		return COLOR;
	}
	
	public boolean coin() {
		return coin;
	}

}

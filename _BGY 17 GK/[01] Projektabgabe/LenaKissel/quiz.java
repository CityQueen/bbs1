package projekt;

import java.awt.Dimension;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JProgressBar;

public class quiz {
	Dimension dim= java.awt.Toolkit.getDefaultToolkit().getScreenSize();
	JLabel frage ;
	JButton ant [] = new JButton[2]; 
	
	JFrame f1; 
	JProgressBar a;
	private Dimension dim2;
	public static void main(String[] arga) {
	}
	public quiz () {	
		f1= new JFrame();
		f1.setSize(400, 300);
		dim2 = null;
		f1.setLocation((int) (dim2.getWidth()-400/2), (int) (dim2.getHeight()-300/2));
		f1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f1.setVisible(true);
		f1.setLayout(null); 
		
		ant[0] = new JButton("");
		ant[0].setBounds(52, 90, 120, 40);
		f1.add(ant[0]);
		
		ant[1] = new JButton("");
		ant[1].setBounds(52, 160, 120, 40);
		f1.add(ant[0]);
		
		frage = new JLabel("Hier steht eine Frage");
		frage.setBounds(52, 15, 250, 40);
		f1.add(frage);
		
		a= new JProgressBar(0, 100);
		a.setBounds(120, 220, 140, 25);
		a.setValue(0);
		a.setStringPainted(true); 
		f1.add(a);
	}
		
		
		

}

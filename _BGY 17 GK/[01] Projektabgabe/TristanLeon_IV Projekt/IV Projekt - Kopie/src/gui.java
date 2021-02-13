import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class gui extends JPanel implements ActionListener {

	Timer time;
	Image img;
	Image img2;
	int key;
	int nx, nx2;

	int figur_y = 230;

	int left = 0;

	int X_Bild;
	int lauf;

	Block block1;
	int coin_score;

	int anzahl = 0;
	int anzahl2 = 0;

	public gui() {

		nx = 0;
		nx2 = 690;

		key = 0;
		lauf = 0;

		setFocusable(true);
		// aufrufe von den bildern vom speicher
		ImageIcon u = new ImageIcon("C:/Users/carso/Documents/bbs1/BGY 17 GK/[01] Projektabgabe/TristanLeon_IV Projekt/IV Projekt - Kopie/background.jpg");
		img = u.getImage();

		addKeyListener(new AL());

		block1 = new Block(250, 110, 50, 50, Color.YELLOW);

		Sprung sprung = new Sprung();// zugriff auf die klasse sprung

		ImageIcon s = new ImageIcon("C:/Users/carso/Documents/bbs1/BGY 17 GK/[01] Projektabgabe/TristanLeon_IV Projekt/IV Projekt - Kopie/character2.png");
		img2 = s.getImage();

		time = new Timer(5, this);
		time.start();

	}

	public void actionPerformed(ActionEvent e) {
		bewegen();
		figur_y = Sprung.sprungposition;
		repaint();

	}

	public void paint(Graphics g) { // Bild wird eingefügt

		super.paint(g);
		Graphics2D f2 = (Graphics2D) g;

		// wieder neu einfügung des bildes nach ende (leider nicht die selbe bild größe
		// wie im toutorial
		// und auch bei mehreren rumprobieren mit den werten nicht hinbekommen da nicht
		// erklärt wird für was welcher ist)

		if (getXBild() == 510 + (anzahl * 2350)) {
			anzahl += 1;
			nx = 0;

		}
		if (getXBild() == 1690 + (anzahl2 * 2350)) {
			anzahl2 += 1;
			nx2 = 0;
		}
		if (getXBild() >= 510) {
			f2.drawImage(img, 685 - nx, 0, null);
		}

		f2.drawImage(img, 685 - nx2, 0, null);
		// einfügen vom charakter
		f2.drawImage(img2, left, figur_y, null);

		f2.setColor(block1.getFarbe());
		f2.fillRect(block1.getX_Block() - getXBild(), block1.getY_Block(), block1.getWidth(), block1.getHight());
		// zeichnet das gefüllte quadrat; durch-getXBild verhindern wir das er stehen
		// bleibt

		block1.Kolisionsabfrage(block1.getX_Block() - getXBild(), block1.getY_Block() + block1.getHight(),
				left + (74 - 12), figur_y);
		// überführung der werte

		if (block1.coin() == true) {
			coin_score = 1;
		} // wenn der block getroffen wird

		f2.drawString("Score  :" + coin_score, 10, 15);
		// erschaffen vom score board
	}

	private int getXBild() {
		// TODO Auto-generated method stub
		return X_Bild;
	}

	// Bild possition wird verändert
	public void bewegen() {
		// einstellen das der charackter nur bis zum linken ende vom bildschirm laufen
		// kann
		if (lauf != -5) {
			if (left + lauf <= 75) {
				left += lauf;
			} else {
				X_Bild += lauf;
				nx += lauf;
				nx2 += lauf;

			}
		} else {
			if (left + lauf > 0) {
				left += lauf;
			}
		}

	}

	private class AL extends KeyAdapter {
		// Al = ActionListener
		public AL() {

		}

		public void keyPressed(KeyEvent e) {
			// was passiert wenn ich die linke oder die rechte pfeil taste drücke

			key = e.getKeyCode();

			if (key == KeyEvent.VK_LEFT) {
				lauf = -5;
			}
			if (key == KeyEvent.VK_RIGHT) {
				lauf = +5;
			}
			if (key == KeyEvent.VK_ESCAPE) {
				System.exit(0);
			}
			if (key == KeyEvent.VK_SPACE) {
				Sprung();
			}
		}

		public void keyReleased(KeyEvent e) {
			// was passiert wenn ich die tasten nicht mehr berühre
			key = e.getKeyCode();
			if (key == KeyEvent.VK_LEFT || key == KeyEvent.VK_RIGHT) {
				lauf = 0;
			}

		}

	}

	public void Sprung() {
		Sprung SprungAnimation = new Sprung();
		SprungAnimation.start();

	}

}
//video 1-6 geschaut
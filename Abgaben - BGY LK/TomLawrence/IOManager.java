import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class IOManager {
	private String url = DBVariables.url;
	private String username = DBVariables.username;
	private String passwd = DBVariables.passwd;
	private String db = DBVariables.db;
	
	private Connection conn;
	
	//Constructor building connection
	public IOManager() {
		try {
			conn = DriverManager.getConnection(url, username, passwd);
			System.out.println("Connection succeeded!");

			this.createTable();
		} catch (SQLException e) {
			System.out.println("Connection failed!");
			e.printStackTrace();
		}
	}

	//Create table "nametable" if not exists
	private void createTable() throws SQLException {
		String sqlCreate = "CREATE TABLE IF NOT EXISTS " + db + ".nametable" +
				"  (id INT NOT NULL AUTO_INCREMENT," +
				"first_name VARCHAR(45) NULL," +
				"PRIMARY KEY (id))";

		Statement myStmt = conn.createStatement();
		myStmt.execute(sqlCreate);
	}
	
	//See if user entry exists in database
	public boolean userExists(String name) {
		try {
			Statement myStmt = conn.createStatement();
			ResultSet myRs = myStmt.executeQuery("SELECT * FROM " + db + ".nametable");
			
			while(myRs.next()) {
				if(myRs.getString("first_name").equalsIgnoreCase(name)) {
					return true;
				}
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
	}

	//make an entry for a new user
	public void makeEntry(String name) {
		try {
			PreparedStatement myStmt = conn.prepareStatement("INSERT INTO " + db + ".nametable (first_name) VALUES ('" + name + "')");
			myStmt.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
}

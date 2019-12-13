public class DBVariables {
	private static String host = "localhost";
	private static String port = "3306";
	private static String parameters = "?serverTimezone=UTC";

	public static String db = "testdb";
	public static String url = "jdbc:mysql://" + host + ":" + port + "/" + db + parameters;
	public static String username = "test";
	public static String passwd = "Eclipse#01";
}

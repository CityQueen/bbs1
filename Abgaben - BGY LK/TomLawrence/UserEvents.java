import java.util.Scanner;

public class UserEvents {
	private boolean terminate = false;
	private boolean state = false;
	private Scanner input;
	private IOManager mgr;
	
	public UserEvents() {
		mgr = new IOManager();
		input = new Scanner(System.in);
		
		System.out.print("Welcome! ");
		
		while(!terminate) {
			if(state) {
				this.commandHandler();
			} else {
				this.stateHandler();
			}
		}
	}
	
	private void stateHandler() {
		System.out.print("Please enter your name: ");
		String name = input.next();
		
		if(name.equalsIgnoreCase("terminate")) {
			terminate = true;
		}
		else if(mgr.userExists(name)) {
			System.out.println("Hello, " +  name.toLowerCase() + "!\nNow, please enter a command: ");
			state = true;
		} else {
			System.out.print("I am sorry, no match found for your name! Would you like to make an entry for that name?"
					+ "\nIf you do, please type yes: ");
			String condition = input.next();
			
			if(condition.equalsIgnoreCase("y") || condition.equalsIgnoreCase("yes")) {
				mgr.makeEntry(name.toLowerCase());
				System.out.println("Your name was added!");
			}
		}
	}
	
	private void commandHandler() {
		System.out.print("> ");
		String cmd = input.next();
		
		if(cmd.equalsIgnoreCase("terminate")) {
			terminate = true;
		} else if(cmd.equalsIgnoreCase("logout")) {
			state = false;
		} else if(cmd.equalsIgnoreCase("sqsum")) {
			forSum();
		}
		else {
			System.out.println("Command not found!");
		}
	}

	private void forSum() {
		System.out.print("Please enter a number: ");
		int n = validateInt(input.next());

		if(n != 0) {
			int sum = 0;
			for(int i = 1; i <= n; i++) {
				sum += i*i;
			}
			System.out.println("Summing up all square roots up to your given number -> " + sum);
		} else {
			System.out.println("Your input must be valid and not 0!");
		}
	}

	private int validateInt(String n) {
		try {
			int i = Integer.parseInt(n);
			return i;
		} catch(Exception e) {
		}
		return 0;
	}
}

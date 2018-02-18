import java.util.Scanner;

public class PosNeg {
	public static void main(String[] args) {
		int n;
		Scanner scan = new Scanner(System.in);
		n=scan.nextInt();
		scan.close();
		if (n<0) {
			System.out.println("Negative");
		}
		else if(n>0) {
			System.out.println("Positive");
		}
		else {
			System.out.println("Zero");
		}
	}

}

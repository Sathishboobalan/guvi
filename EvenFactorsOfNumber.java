import java.util.Scanner;

public class EvenFactorsOfNumber {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();//input number to check how many factors based on this
		for(int i=2;i<=n;i++) {
			if(i%2==0 && n%i==0) {
				System.out.print(i+" ");
			}
		}
	}

}

import java.util.Scanner;

public class CountDigit {
	public static void main(String[] args) {
		int n;
		int count=0;
		Scanner scan = new Scanner(System.in);
		n=scan.nextInt();
		scan.close();
		while (n!=0) {
			if (n%10!=0) {
				count++;
				n=n/10;
				}
			}
			
		System.out.println(count);
	}

}

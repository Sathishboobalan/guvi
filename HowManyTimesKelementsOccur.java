import java.util.*;
public class HowManyTimesKelementsOccur {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		long count=0;
		long n = scan.nextLong();
		long k = scan.nextLong();
		while(n>0) {
			long digit = n%10;
			if(k==digit) {
				count+=1;
			}
			n/=10;
		}
		System.out.println(count);
		
	}

}

import java.util.Scanner;

public class HunterSet01SumIsClosestToZero {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int min1=99;
		int min2=99;
		String str = "";
		int n = scan.nextInt();
		int [] a =  new int [n];
		for(int i=0;i<n;i++) {
			a[i]=scan.nextInt();
		}
		for(int i=0;i<n;i++) {
			for(int j=i+1;j<n;j++) {
				int sum=a[i]+a[j];
				if(sum<(min1+min2) && sum>=0) {
					min1=a[i];
					min2=a[j];
				}
			}
		}
		System.out.print(min1 + " "+min2);
	}
}

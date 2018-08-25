import java.util.Arrays;
import java.util.Scanner;

public class ArraySortAndSearchingKelements {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int count=0;
		int n = scan.nextInt();
		int a[] = new int [n];
		System.out.println("enter Array Elements");
		for(int i=0;i<n;i++) {
			a[i]=scan .nextInt();
		}
		Arrays.sort(a);
		System.out.println("enter two num to serach");
		int n1 = scan.nextInt();
		int n2 =scan.nextInt();
		for(int i=0;i<n;i++) {
			if(n1==a[i] ) {
				count+=1;
				break;
			}
		}
		for(int i=0;i<n;i++) {
			if(n2==a[i] ) {
				count+=1;
				break;
			}
		}
		if(count==2) {
			System.out.println("Yes");
		}
		else {
			System.out.println("No");
		}
	}

}

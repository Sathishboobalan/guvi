import java.util.Arrays;
import java.util.Scanner;

public class HunterSet01RepeatedNumberWithArraySort {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int count=0;
		int count1=0;
		int n = scan.nextInt();
		int [] a = new int [n];
		String str = "";
		for(int i=0;i<n;i++) {
			a[i]=scan.nextInt();
		}
		for(int i=0;i<n;i++) {
			count=0;
			for(int j=i;j<n;j++) {
				if(a[i]==a[j]) {
					count+=1;
				}
			}
			if(count>1) {
				str =str + Integer.toString(a[i]);
			}
			
		}
		
		char [] arr = str.toCharArray();
		Arrays.sort(arr);
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}
	}

}

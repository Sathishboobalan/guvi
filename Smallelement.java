import java.util.Scanner;

public class LargestElement {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int arrsize;
		int small=0;;
		System.out.println("Enter the size of array");
		arrsize=scan.nextInt();
		int [] arr = new int [arrsize];
		System.out.println("Enter the size of array");
		for(int loopvar=0;loopvar<arrsize;loopvar++) {
			arr[loopvar]=scan.nextInt();
		}
		scan.close();
		small=arr[0];
		for(int loopvar=0;loopvar<arrsize;loopvar++) {
			if(arr[loopvar]<small){
				small=arr[loopvar];
			}
		}
		System.out.println("The largest element is"+" " +small);
	}
	

}

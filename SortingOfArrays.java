import java.util.Scanner;

public class SortingOfArrays {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num;
		num=scan.nextInt();
		int [] arr = new int[num];
		for (int i=0;i<num;i++) {
			arr[i]=scan.nextInt();
		}
		scan.close();
		for (int i=0;i<num;i++) {
			for(int j=0;j<num;j++) {
				if(arr[i]<arr[j]) {
					int temp=arr[i];
					arr[i]=arr[j];
					arr[j]=temp;
				}
			}
		}
		for (int i=0;i<num;i++) {
			System.out.println(arr[i]);
		}
	}

}

import java.util.Scanner;

public class Median {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num;
		int medi = 0;
		float count=0;
		num=scan.nextInt();
		int [] arr = new int[num];
		for (int i=0;i<num;i++) {
			arr[i]=scan.nextInt();
			count=count+1;
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
		for(int i=1;i<=Math.floor(count/2);i++) {
			
			medi=arr[i];
		}
		System.out.println(medi);
	}

}

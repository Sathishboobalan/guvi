import java.util.Scanner;

public class CheckingParanthesisEqualOrNot {
	public static void main(String args[]) {
		Scanner scan = new Scanner (System.in);
		String str = scan.next();
		int count=0,count1=0;
		for(int i=0;i<str.length();i++) {
			if(str.charAt(i)=='(') {
				count+=1;
			}
			if(str.charAt(i)==')') {
				count1+=1;
			}
			
		}
		if(count==count1) {
			System.out.println("yes");
		}
		else {
			System.out.println("no");
		}
	}
	

}

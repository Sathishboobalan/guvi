

import java.util.Scanner;

public class RevesrseStringOfRemovedVowels {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String str1 = "";
		String str2 = "";
		String str = scan.nextLine();
		int length=str.length();
		scan.close();
		for(int i=0;i<length;i++) {
			if((str.charAt(i)=='a') || (str.charAt(i)=='e') || (str.charAt(i)=='o') || (str.charAt(i)=='i') || (str.charAt(i)=='u')){
				continue;
				
			}
			else {
				str1= str1+str.substring(i,i+1);
			}
		}
		for(int i=str1.length()-1;i>=0;i--) {
			str2 = str2 + str1.charAt(i);
		}
		System.out.println(str2);
	}

}

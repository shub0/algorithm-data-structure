/**
 * 
 * DecodeWays.java
 * Nov 25, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class DecodeWays {
	public int decodeWays(String str){
		if (str.length() == 0) return 0;
		else if (str.charAt(0) == '0' ) return 0;
		else if (str.length() == 1) return 1;
		else if (str.length() == 2){
			if (Integer.valueOf(str) > 26)	return (str.charAt(1) == '0') ? 0 : 1;
			else if (Integer.valueOf(str) == 10) return 1;
			else return 2;
		}
		else{
			int decodeWays = 0;
			int singleChar = decodeWays(str.substring(1));
			int doubleChar = decodeWays(str.substring(2));
			String doubleStr = str.substring(0,2);
			String singleStr = str.substring(0,1);
			if (Integer.valueOf(singleStr) > 0) 	decodeWays += singleChar;
			if (Integer.valueOf(doubleStr) < 27 && Integer.valueOf(doubleStr) > 9)	decodeWays += doubleChar;
			return decodeWays;
		}
	}
	public static void main(String[] args){
		System.out.println(new DecodeWays().decodeWays("61658122"));
	}
}

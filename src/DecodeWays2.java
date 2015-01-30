import java.util.ArrayList;

/**
 * 
 * DecodeWays2.java
 * Nov 25, 2012
 */

/**
 * @author Shubo Liu
 *	Better than DecodeWays()
 * Study this code to understand split string and convert to integer issues by considering corner case
 */
public class DecodeWays2 {
	public int decodeWays(String str){
		if (str.length() == 0) return 0;
		else if (str.charAt(0) == '0' ) return 0;
		else if (str.length() == 1) return 1;
		else{
			int[] ways = new int[str.length()];
			ways[0] = 1;
			int value = Integer.valueOf(str.substring(0,2));
			if (value > 26) ways[1] = (value % 10 == 0) ? 0 : 1;
			else if (value == 10 || value == 20) ways[1] = 1;
			else ways[1] = 2;
			for (int index = 2; index < str.length(); index++){
				if (str.charAt(index) != '0') ways[index] += ways[index - 1];
				value = Integer.valueOf(str.substring(index - 1, index + 1));
				if (value > 9 && value < 27) ways[index] += ways[index - 2];
			}
			return ways[str.length() - 1];
		}
	}
	public ArrayList<String> decode(String str){
		ArrayList<String> code = new ArrayList<String>();
		if (str.length() == 0)	return code;
		else{
			decode(code, str, new StringBuffer());
			return code;
		}
	}
	// decode digit input by mapping rules
	private void decode(ArrayList<String> code, String input, StringBuffer currentCode){
		if (input.length() == 0){
			code.add(currentCode.toString());
			return;
		}
		if (input.startsWith("0")) return;
		if (input.length() >= 2){
			int value = Integer.valueOf(input.substring(0,2));
			if (value < 27){
				char map = (char) (value - 1 + 'a');
				int size = currentCode.length();
				currentCode.append(map);
				decode(code, input.substring(2), currentCode);
				currentCode.delete(size, currentCode.length() - 1);
			}
		}	
		char currentChar = input.charAt(0);
		char map = (char) (currentChar - '1' + 'a');
		int size = currentCode.length();
		currentCode.append(map);
		decode(code, input.substring(1), currentCode);
		currentCode.delete(size, currentCode.length() - 1);
	}
	public static void main(String[] args){
		System.out.println(new DecodeWays2().decodeWays("61658122"));
		System.out.println(new DecodeWays2().decode("61658122"));

	}
}

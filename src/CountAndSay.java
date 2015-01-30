/**
 * 
 * CountAndSay.java
 * Nov 25, 2012
 */

/**
 * @author huangsp
 *
 */
public class CountAndSay {
	public String countAndSay(int n){
		String[] sequence = new String[n];
		sequence[0] = "1";
		for (int index = 1; index < n; index++){
			sequence[index] = generateString(sequence[index - 1]);
		}
		return sequence[n - 1];
	}
	public String generateString(String str){

		if (str.length() == 1) return "11";
		else{
			int count = 1;
			StringBuffer out = new StringBuffer();
			for(int index = 1; index < str.length(); index++){
				if (str.charAt(index) == str.charAt(index - 1))
					count++;
				else{
					out.append(Integer.toString(count));
					out.append(str.charAt(index - 1));
					count = 1;
				}
			}
			out.append(Integer.toString(count));
			out.append(str.charAt(str.length() - 1));
			return out.toString();
		}
	}
	public static void main(String[] args){
		System.out.println(new CountAndSay().countAndSay(5));
	}
}

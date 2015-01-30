/**
 * 
 * LongestValidParentheses.java
 * Nov 27, 2012
 */

/**
 * @author huangsp
 *
 */
public class LongestValidParentheses {
	public int longestValidParentheses(String s){
		int len = s.length();
		if (len < 2) return 0;
		else{
			int maxLen = 0;
			int count = 0;
			int result = 0;
			char[] charArray = s.toCharArray();
			for (int index = 0; index < len; index++){
				if (charArray[index] == '(')
					count ++;
				else{
					if (count > 0) count--;
					else{
						count = 0;
						charArray[index] = '*';
					}
				}
			}
			count = 0;
			for (int index = len - 1; index >= 0; index--){
				if (charArray[index] == '*'){
					maxLen = Math.max(maxLen, result);
					result = 0;
					count = 0;
					continue;
				}
				if (charArray[index] == ')') count++;
				else {
					if (count > 0){
						result++;
						count--;
					}else{
						maxLen = Math.max(maxLen, result);
						result = 0;
						count = 0;
					}
				}
			}
			maxLen = Math.max(maxLen, result);
			return 2 * maxLen ;
		}
	}
	
	// more readable algorithm
	public int longestValidParentheses2(String s){
		int currentLength = 0;
		int maxLength = 0;
		int length = s.length();
		int count = 0;
		// read forward
		for (int index = 0; index < length; index++){
			if (s.charAt(index) == '(')	count++;
			else count--;
			currentLength++;
			// a matched position
			if (count == 0){
				maxLength = Math.max(currentLength, maxLength);
			}
			// invalid position
			if (count < 0){
				count = 0;
				currentLength = 0;
			}
		}
		count = 0;
		currentLength = 0;
		// read backward
		for (int index = length - 1; index > - 1; index--){
			if (s.charAt(index) == ')')	count++;
			else count--;
			currentLength++;
			if (count == 0){
				maxLength = Math.max(currentLength, maxLength);
			}
			if (count < 0){
				count = 0;
				currentLength = 0;
			}
		}
		return maxLength;
	}
	
	public static void main(String[] args){
		System.out.println(new LongestValidParentheses().longestValidParentheses2("))()())("));
	}
}

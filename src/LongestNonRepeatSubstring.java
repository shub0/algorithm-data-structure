/**
 * 
 * LongestNonRepeatSubstring.java
 * Nov 27, 2012
 */
import java.util.HashMap;
/**
 * @author huangsp
 *
 */
public class LongestNonRepeatSubstring {
	public int lengthOfLongestSubstring(String s){
		if (s.length() == 0) return 0;
		else if (s.length() == 1) return 1;
		else{
			// initialize hash table is -1;
			// hash value is the pos of char in the string
			int[] hashtable = new int[256];
			for (int index = 0; index < 256; index ++){
				hashtable[index] = -1;
			}
			int startIndex = 0;
			int endIndex = 0;
			
			int maxSubstring = endIndex - startIndex + 1;
			for (int index = 0; index < s.length(); index++){
				// never appear in the string
				if (hashtable[(int)s.charAt(index)] == -1){
					endIndex = index;
					hashtable[(int)s.charAt(index)] = index;
				}else{
					// repeated char position
					int repeatedCharPos = hashtable[(int)s.charAt(index)];
					maxSubstring = Math.max(maxSubstring, index - startIndex);
					// clear all appearance record before repeated char
					for (int clearIndex = startIndex; clearIndex <= repeatedCharPos; clearIndex++){
						hashtable[(int)s.charAt(clearIndex)] = -1;
					}
					startIndex = repeatedCharPos + 1;
					hashtable[(int)s.charAt(index)] = index;
				}
			}
			//if (endIndex == s.length() - 1)
				maxSubstring = Math.max(maxSubstring, s.length() - startIndex);
			return maxSubstring;
		}
	}
	
	public int lengthOfLongestSubstring2(String s){
		if (s.length() < 2)	return s.length();
		HashMap<Character, Integer> positionInString = new HashMap<Character, Integer>();
		int maxLength = 1;
		int length = s.length();
		int startPosition = 0;
		for (int index = 0; index < length; index++){
			char currentChar = s.charAt(index);
			if (positionInString.containsKey(currentChar)){
				maxLength = Math.max(index - startPosition, maxLength);
				int repeatedPosition = positionInString.get(currentChar);
				while(startPosition <= repeatedPosition){
					char removeChar = s.charAt(startPosition);
					positionInString.remove(removeChar);
					startPosition ++;
				}		
			}
			positionInString.put(currentChar, index);
		}
		maxLength = Math.max(length - startPosition, maxLength);
		return maxLength;
	}
	public static void main(String[] args){
		System.out.println(new LongestNonRepeatSubstring().lengthOfLongestSubstring("abcabcdea"));
	}
}

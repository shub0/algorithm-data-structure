import java.util.HashMap;

/**
 * 
 * MinWindow.java
 * Nov 28, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class MinWindow {
	public String minWindow(String S, String T){
		int lenS = S.length();
		int lenT = T.length();
		if (lenS == 0 || lenT == 0) return "";
		else if (S.equals(T)) return S;
		int[] hashtableS = new int[256];
		int[] hashtableT = new int[256];
		int charKind = 0;
		int matchedKind = 0;
		for (int index = 0; index < lenT; index++){
			if (hashtableT[(int)T.charAt(index)] == 0)
				charKind++;
			hashtableT[(int)T.charAt(index)] ++;
		}
		int start = 0;
		int end = 0;
		String windowString = S;
		boolean flag = false;
		while(end < lenS){
			int currentChar = (int)S.charAt(end);
			hashtableS[currentChar] ++;
			if (hashtableS[currentChar] == hashtableT[currentChar]){
				matchedKind ++;
			}
			if (matchedKind == charKind){
				flag = true;
				while (start <= end){
					int current = (int) S.charAt(start);
					hashtableS[current] --;
					start++;
					if (hashtableS[current] < hashtableT[current]){
						matchedKind --;
						break;
					}
				}
				if (end - start + 2 < windowString.length()){
					windowString = S.substring(start - 1,end + 1);
				}
			}
			end++;
		}
		if (flag)
			return windowString;
		else return "";
	}
	
	public String minWindow2(String S, String T){
		HashMap<Character, Integer> charInS = new HashMap<Character, Integer>();
		HashMap<Character, Integer> charInT = new HashMap<Character, Integer>();
		int lenS = S.length();
		int lenT = T.length();
		int patternChar = 0;
		int matchedChar = 0;
		// form HashMap for pattern string T
		for (int index = 0; index < lenT; index++){
			char currentChar = T.charAt(index);
			if (charInT.containsKey(currentChar)){
				int frequency = charInT.get(currentChar);
				charInT.put(currentChar, ++frequency);
			}else{
				charInT.put(currentChar, 1);
				patternChar++;
			}
		}
		String minWindowString = S;
		int startPosition = 0;
		int endPosition = 0;
		boolean matched = false;
		while(endPosition < lenS){
			char tailChar = S.charAt(endPosition);
			if (charInS.containsKey(tailChar)){
				int frequency = charInS.get(tailChar);
				charInS.put(tailChar, ++frequency);
			}else{
				charInS.put(tailChar, 1);
			}
			if(charInT.containsKey(tailChar) && charInT.get(tailChar) == charInS.get(tailChar)){
				matchedChar++;
			}
			// find a window
			if (matchedChar == patternChar){
				matched = true;
				while (startPosition <= endPosition){
					char headChar = S.charAt(startPosition);
					
					int frequency = charInS.get(headChar);
					if (charInT.containsKey(headChar) && charInT.get(headChar) == frequency){
						matchedChar --;					
					}
					if (frequency > 1)
						charInS.put(headChar, -- frequency);
					else{
						charInS.remove(headChar);
					}
					
					if (matchedChar < patternChar){
						int newLength = endPosition - startPosition + 1;
						if (newLength < minWindowString.length()){
							minWindowString = S.substring(startPosition, endPosition + 1);
						}
						startPosition++;
						break;
					}
					startPosition++;
				}
			}
			endPosition ++;
		}
		if (!matched)	return "";
		return minWindowString;
	}
	public static void main(String[] args){
		System.out.println(new MinWindow().minWindow2("abcabdaebac", "ceaa"));
	}
}

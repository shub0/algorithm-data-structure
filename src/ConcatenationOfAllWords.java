import java.util.ArrayList;
import java.util.HashMap;

/**
 * 
 * ConcatenationOfAllWords.java
 * Feb 4, 2013
 */

/**
 * @author huangsp
 *
 */
public class ConcatenationOfAllWords {
	public ArrayList<Integer> findSubstring(String S, String[] words){
		int numberOfWords = words.length;
		int lengthOfWord = words[0].length();
		int substringLength = numberOfWords * lengthOfWord;
		ArrayList<Integer> indices = new ArrayList<Integer>();
		if (S.length() < substringLength)	return indices;
		else{
			HashMap<String, Integer> wordsMap = new HashMap<String, Integer>();
			for (int index = 0; index < numberOfWords; index++){
				if (wordsMap.containsKey(words[index])){
					int freq = wordsMap.get(words[index]);
					wordsMap.put(words[index], ++freq);
				}else{
					wordsMap.put(words[index],1);
				}
			}
			for (int index = 0; index <= S.length() - substringLength; index++){
				String substring = S.substring(index, index + substringLength);
				if (check(substring, wordsMap, lengthOfWord, numberOfWords))	indices.add(index);
			}
			return indices;
		}
	}
	private boolean check(String S, HashMap<String,Integer> words, int lengthOfWord, int numberOfWords){
		HashMap<String,Integer> wordsInString = new HashMap<String, Integer>();
		for (int index = 0; index < numberOfWords; index ++){
			String currentWord = S.substring(index * lengthOfWord, (index + 1) * lengthOfWord);
			if (!words.containsKey(currentWord))		return false;
			int freqInMap = words.get(currentWord);
			if (wordsInString.containsKey(currentWord)){
				int freqInString = wordsInString.get(currentWord);
				if (freqInString == freqInMap)	return false;
				wordsInString.put(currentWord, ++freqInString);
			}else{
				wordsInString.put(currentWord, 1);
			}
		}
		return true;
	}
	public static void main(String[] args){
		String[] words = {"a","b","a"};
		String S = "abababab";
		ConcatenationOfAllWords myObject = new ConcatenationOfAllWords();
		System.out.println(myObject.findSubstring(S, words));
	}
}

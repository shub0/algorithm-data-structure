/**
 * 
 * LetterCombination.java
 * Nov 27, 2012
 */
import java.util.*;
/**
 * @author huangsp
 *
 */
public class LetterCombination {
	String[] keyboard = {"0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
	ArrayList<String> list = new ArrayList<String>();
	public ArrayList<String> letterCombinations(String digits) {
		makeCombination(digits, new StringBuffer());
		return list;
    }
	// non-recursive algorithm
	public ArrayList<String> letterCombinations2(String digits) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (digits == null || digits.length() == 0) return new ArrayList<String>();
        else{
            ArrayList<String> solutionList = new ArrayList<String>();
            int len = digits.length();
            int digit = digits.charAt(0) - '0';
            for (int index = 0; index < keyboard[digit].length(); index ++){
            	String newWord = keyboard[digit].charAt(index) + "";
            	solutionList.add(newWord);
            }
            for (int index = 1; index < len; index ++){
                digit = digits.charAt(index) - '0';
				int size = solutionList.size();
                while(size > 0){
                	size --;
                    String currentWord = solutionList.remove(solutionList.size() - 1);
                    for (int indexD = 0; indexD < keyboard[digit].length(); indexD ++){
                        char newChar = keyboard[digit].charAt(indexD);
                        solutionList.add(0,currentWord + newChar);
                    }
                }
                
            }
            return solutionList;
        }
    }
	private void makeCombination(String digits, StringBuffer out){
		if (digits.length() == 0){
			list.add(out.toString());
		}
		else{
			int num = digits.charAt(0) - '0';
			for (int index = 0; index < keyboard[num].length(); index++){
				out.append(keyboard[num].charAt(index));
				makeCombination(digits.substring(1), out);
				out.setLength(out.length() - 1);
			}
		}
	}
	public static void main(String[] args){
		System.out.println(new LetterCombination().letterCombinations2("23"));
	}
}

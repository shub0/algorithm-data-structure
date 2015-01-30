import java.util.ArrayList;

/**
 * 
 * TextJustification.java
 * Dec 11, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class TextJustification {
	ArrayList<String> justifiedText = new ArrayList<String>();
	public ArrayList<String> fullJustify(String[] words, int L) {
        // Start typing your Java solution below
        // DO NOT write main() function
		int len = words.length;
		if (len == 0)	return	justifiedText;
		else{
			int currentLineLength = 0;
			int start = 0;
			int index = 0;
			while(index < len){
				if (currentLineLength + words[index].length() < L){
					currentLineLength += words[index].length() + 1;
					index++;
				}else{
					String currentLine = fillString(words, start, index, currentLineLength, L);
					start = index;
					justifiedText.add(currentLine);
					currentLineLength = 0;
				}
			}
			if (start < index){
				int wordsLeft = index - start;
				String currentLine = new String();
				if (wordsLeft == 1){
					int space = L - words[index - 1].length();
					currentLine += words[index - 1];
					for(int spaceIndex = 0; spaceIndex < space; spaceIndex++){
						currentLine += " ";
					}
				}
				else{
					currentLineLength = 0;
					for (int index2 = start; index2 < index; index2++)
						currentLineLength += (words[index2].length() + 1);
					currentLine = fillString(words, start, index, currentLineLength, L);
				}
				justifiedText.add(currentLine);
				
			}
			return justifiedText;
		}
	}
	
	private String fillString(String[] words, int start, int index, int currentLineLength, int L){
		String currentLine = new String();
		if (currentLineLength + words[index].length() == L){
			for (;start < index; start++){
				currentLine += (words[start] + " ");
			}
			currentLine += words[start];
		}else{
			int spaceCount = L - currentLineLength;
			int wordsCount = index - start;
			if (wordsCount == 1){
				currentLine += words[index - 1];
				spaceCount = L - words[index - 1].length();
				for (int spaceIndex = 0; spaceIndex < spaceCount; spaceIndex++){
					currentLine += " ";
				}
			}
			int space = spaceCount  / ( wordsCount - 1);
			currentLine += (words[start++] + " ");
			for (; start < index - 1; start++){
				for(int spaceIndex = 0; spaceIndex < space; spaceIndex++){
					currentLine += " ";
				}
				currentLine += (words[start] + " ");
			}
			space = L - currentLine.length() - words[index - 1].length();
			for(int spaceIndex = 0; spaceIndex < space; spaceIndex++){
				currentLine += " ";
			}
			currentLine += words[start];
		}
		return currentLine;
	}
	public static void main(String[] args){
		String str = "This is an example of text justification!";
		String[] words = str.split("\\s");
		System.out.println(new TextJustification().fullJustify(words, 16));
	}
}

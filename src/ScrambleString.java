/**
 * 
 * ScrambleString.java
 * Feb 6, 2013
 */
import java.util.ArrayList;
import java.util.Stack;
/**
 * @author huangsp
 *
 */
public class ScrambleString {
	public boolean scrambleString(String S, String T){
		Stack<String> S1 = new Stack<String>();
		Stack<String> S2 = new Stack<String>();
		int len = S.length();
		for (int index = 0; index < len; index ++){
			String current = "" + T.charAt(index);
			if (!S.contains(current))	return false;
			S1.push(current);
		}
		return scrambleString(S, S1, S2);
	}
	
	@SuppressWarnings("unchecked")
	private boolean scrambleString(String S, Stack<String> S1, Stack<String> S2){
		ArrayList<String> candidateString = new ArrayList<String>();
		while(S1.size() > 0){
			candidateString.add(S1.pop());
			ArrayList<String> qualifiedString = new ArrayList<String>();
			while(S2.size() > 0){
				for (String peek: candidateString){
					if(S.contains(peek + S2.peek()) && !qualifiedString.contains(peek + S2.peek())){
						qualifiedString.add(peek + S2.peek());
					}
					if(S.contains(S2.peek() + peek) && !qualifiedString.contains(S2.peek() + peek)){
						qualifiedString.add(S2.peek() + peek);
					}
				}
				// S2.push("UNqualifiedString")
				if (qualifiedString.size() == 0)	break;
				else{
					S2.pop();
					candidateString = (ArrayList<String>) qualifiedString.clone();
					qualifiedString.clear();
				}
			}
			// S.contains(peek + S2.peek()) && S.contains(S2.peek() + peek);
			// go one further step
			if (candidateString.size() > 1){
				while(S1.size() > 0){
					// peek = S2.peek();
					for (String peek : candidateString){
						if (S.contains(peek + S1.peek()) && !qualifiedString.contains(peek + S1.peek())){
							qualifiedString.add(peek + S1.peek());
						}
						if (S.contains(S1.peek() + peek) && !qualifiedString.contains(S1.peek() + peek)){
							qualifiedString.add(S1.peek() + peek);
						} 
					}
					if (qualifiedString.size() == 0)	break;
					else{
						S1.pop();
						candidateString = (ArrayList<String>) qualifiedString.clone();
						qualifiedString.clear();
					}
				}
			}		
			S2.push(candidateString.get(0));
			candidateString.clear();
		}
		return (S2.size() == 1);
	}
	public static void main(String[] args){
		System.out.println(new ScrambleString().scrambleString("babab", "babab"));
	}
}

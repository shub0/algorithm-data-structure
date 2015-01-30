import java.util.ArrayList;
import java.util.HashSet;
import java.util.Stack;

/**
 * 
 * Parenthesis.java
 * Dec 11, 2012
 */

/**
 * @author huangsp
 *
 */
public class Parenthesis {
	 HashSet<String> stringSet;
	    public ArrayList<String> generateParenthesis(int n){
	        // Start typing your Java solution below
	        // DO NOT write main() function
	        stringSet = new HashSet<String>();
	        if (n == 0) return new ArrayList<String>();
	        else{
	            int len = 2 * n;
	            int offset = 0;
	            StringBuffer out = new StringBuffer();
	            wellFormedParenthesis(out, offset, len);
	            ArrayList<String> stringList = new ArrayList<String>();
	            for(String ex:stringSet)
	                stringList.add(ex);
	            return stringList;
	        }
	    }
	    private boolean wellFormedParenthesis(StringBuffer out, int offset, int len){
	        if (out.length() == len && offset == 0) {
	            return true;
	        }else if(out.length() == len){
	            return false;
	        }else{
	            out.append("(");
	            if(wellFormedParenthesis(out, offset + 1, len)){
	            	String aSolution = out.toString();
	            	stringSet.add(aSolution);
	            }
	            out.setLength(out.length() - 1);
	            if (offset > 0){
	                out.append(")");
	                if(wellFormedParenthesis(out, offset - 1, len)){
		            	String aSolution = out.toString();
		            	stringSet.add(aSolution);
		            }
	                out.setLength(out.length() - 1);
	            }
	            return false;
	        }
	    }
	    public boolean validParenthesis(String s){
	    	int len = s.length();
	    	if (len == 0)	return true;
	    	else if (len % 2 == 1)	return false;
	    	else{
	    		Stack<Character> string = new Stack<Character>();
	    		for (int index = 0; index < len; index++){
	    			char currentChar = s.charAt(index);
	    			if(currentChar == '(' || currentChar == '[' || currentChar == '{'){
	    				string.push(currentChar);
	    			}else if (currentChar == ')'){
	    				if (string.isEmpty())	return false;
	    				else if (string.pop() != '(')	return false;
	    			}else if (currentChar == ']'){
	    				if (string.isEmpty())	return false;
	    				else if (string.pop() != '[')	return false;
	    			}else if (currentChar == '}'){
	    				if (string.isEmpty())	return false;
	    				else if (string.pop() != '{')	return false;
	    			}
	    		}
	    		if (string.isEmpty())	return true;
	    		else return false;
	    	}
	    	
	    }
	    public static void main(String[] args){
	    	System.out.println(new Parenthesis().generateParenthesis(2));
	    }
}

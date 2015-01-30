

/**
 * 
 * Regex.java
 * Dec 3, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class Regex {
	public boolean isMatch(String s, String p){
		if (p.isEmpty()) return s.isEmpty();
		else if (s.isEmpty()){
			if (p.isEmpty()) return true;
			else if (p.length() == 2 && p.charAt(1) == '*')	return true;
			if (p.length() > 2)
					return p.charAt(1) == '*' && isMatch(s, p.substring(2));
			return false;
		}
		else{
			if(p.length() == 1 || (p.length() > 1 && p.charAt(1) != '*')){
				boolean firstMatch = (p.charAt(0) == s.charAt(0));
				boolean secondMatch = (p.charAt(0) == '?' && !s.isEmpty());
				boolean thirdMatch = isMatch(s.substring(1), p.substring(1));
				return (firstMatch || secondMatch) && thirdMatch;
			}
			// deal with '*'
			while( (s.length() > 0 && p.charAt(0) == s.charAt(0))
					|| ( p.charAt(0) == '?' && s.length() > 0) ){
				if (isMatch(s,p.substring(2)))	return true;
				s = s.substring(1);
			}
			return isMatch(s, p.substring(2));
		}
	}
	public static void main(String[] args){
		//String s = "aa";
		//String p = "aa";
		String s = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba";
		String p = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*";
		System.out.println(new Regex().wildMatch(s, p));
	}
	
	public boolean wildMatch(String s, String p){
		if (p.isEmpty())	return s.isEmpty();
		else {
			StringBuffer pattern = new StringBuffer();
			for (int index = 0; index < p.length() - 1; index++){
				if (p.charAt(index) == '*' && p.charAt(index + 1) == '*')
					continue;
				else pattern.append(p.charAt(index));
			}
			pattern.append(p.charAt(p.length() - 1));
			return wildcatMatch(s, pattern.toString());
		}
	}
	private boolean wildcatMatch(String s, String p){
		if (p.isEmpty())	return s.isEmpty();
		else if (s.isEmpty()){
			if (p.isEmpty())	return true;
			else if (p.charAt(0) == '*') return wildcatMatch(s, p.substring(1));
			return false;
		}else if (p.equals("*")){
			return true;
		}else{	
			if (p.charAt(0) != '*'){
				boolean first = (s.charAt(0) == p.charAt(0));
				boolean second = (p.charAt(0) == '?' && !s.isEmpty());
				boolean third = wildcatMatch(s.substring(1), p.substring(1));
				return (first || second) && third;
			}else{
				while (s.length() > 0){
					if (wildcatMatch(s, p.substring(1)))	return true;
					s = s.substring(1);
				}
				return false;
			}
		}
	}
}

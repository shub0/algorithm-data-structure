/**
 * 
 * Palindrome.java
 * Jan 29, 2013
 */

/**
 * @author huangsp
 *
 */
public class Palindrome {
	public boolean palindrome(String s){
		if (s.length() == 0){
			return true;
		}else{
			int left = 0;
			int right = s.length() - 1;
			s = s.toLowerCase();
			while(left < right){
				while(left < right && !checkChar(s.charAt(left)))
					left++;
				while(left < right && !checkChar(s.charAt(right)))
					right--;
				if (s.charAt(left) != s.charAt(right)){
					return false;
				}
				left++;
				right--;
			}
			return true;
		}
	}
	private boolean checkChar(char c){
		if (c >= 'a' && c <= 'z')	return true;
		if (c >= '0' && c <= '9')	return true;
		return false;
	}
	public static void main(String[] args){
		String test = "1a2";
		System.out.println(new Palindrome().palindrome(test));
		
	}
}

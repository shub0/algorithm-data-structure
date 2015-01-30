/**
 * 
 * AddBinary.java
 * Nov 22, 2012
 */
import java.util.HashMap;
/**
 * @author Shubo Liu
 *
 */
public class AddBinary {
	 HashMap<Integer, Character> charMap = new HashMap<Integer, Character>();
	 public String addBinary(String a, String b){
	        if (a == null) return b;
	        else if(b == null) return b;
	        else{
	        	// set a int - char map (hex, binary, decimal and so on) 
	        	charMap.put(1, '1');
	        	charMap.put(0, '0');
	            return stringAdd(a, b, 2);
	        }
		}
		private String stringAdd(String a, String b, int base){
			if (a.length() < b.length() )	return stringAdd(b, a, base);
			else{
				int carry = 0;
				int lenB = b.length();
				int lenA = a.length();
				StringBuffer out = new StringBuffer();
				for (int pointer = 0; pointer <= lenA - 1; pointer++){
					int sum = carry;
					//int digitA = a.charAt(lenA - 1 - pointer) - '0';
					int digitA = Integer.valueOf(a.substring(lenA - 1 - pointer, lenA - pointer), base);
					sum += digitA;
					if (pointer < lenB){
						int digitB = Integer.valueOf(b.substring(lenB - 1 - pointer, lenB - pointer), base);
						sum += digitB;
					}
					int digit = sum % base;
					carry = sum / base;
					out.append(charMap.get(digit));	
					}
				if (carry != 0) out.append((char) (charMap.get(carry)));
				return out.reverse().toString();
			}
		}
		public String addBinary2(String a, String b) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
	        int lenA = a.length();
	        int lenB = b.length();
	        if (lenA == 0)  return b;
	        else if (lenB == 0) return a;
	        else if (lenA < lenB)   return addBinary(b, a);
	        else{
	            int carry = 0;
	            int indexA = lenA - 1;
	            int indexB = lenB - 1;
	            StringBuffer sum = new StringBuffer();
	            while (indexA >= 0){
	                carry += (a.charAt(indexA--) - '0');
	                if (indexB >= 0)
	                	carry += (b.charAt(indexB--) - '0');
	                sum.append((char) (carry % 2 + '0'));
	                carry /= 2;
	            }
	            if ( carry != 0)    sum.append("1");
	            return sum.reverse().toString();
	        }
	    }
	public static void main(String[] args){
		System.out.println(new AddBinary().addBinary2("101", "10"));
	}
}

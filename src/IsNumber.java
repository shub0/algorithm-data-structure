/**
 * 
 * isNumber.java
 * Dec 6, 2012
 */

/**
 * @author huangsp
 * Requirement is important
 */
public class IsNumber {
	public boolean isNumber(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
		s = s.trim();
        if (s.length() == 0)    return false;
        else if (s.length() == 1){
        	if (s.charAt(0) >= '0' && s.charAt(0) <= '9')	return true;
        	else return false;
        }
        else{
            boolean d = false;
            boolean e = false;
            int len = s.length();
            if ((s.charAt(0) < '0' || s.charAt(0) > '9') && (s.charAt(0) != '+') && (s.charAt(0) != '-') )	return false;
            if ((s.charAt(0) == '0') && s.charAt(1) != '.')	return false;
            for (int index = 1; index < len; index++){
                if (s.charAt(index) == 'e'){
                    if(e)   return   false;
                    else e = true;
                }else if( s.charAt(index) == '.'){
                    if (d)  return false;
                    else d = true;
                }else if ( s.charAt(index) < '0' || s.charAt(index) > '9'){
                    return false;
                }
            }
            return true;
        }
    }
	public static void main(String[] args){
		System.out.println(new IsNumber().isNumber("    +0.1"));
	}
}

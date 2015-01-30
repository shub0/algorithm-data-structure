/**
 * 
 * ReverseInteger.java
 * Dec 4, 2012
 */

/**
 * @author huangsp
 *
 */
public class ReverseInteger {
	public int reverseInt(int num){
		if (num == 0) return 0;
		if (num < 0)	return -reverseInt(-num);
		else{
			int reverseInt = 0;
			while(num > 0){
				reverseInt = reverseInt * 10 + num % 10;
				num /= 10;
			}
			return reverseInt;
		}
	}
	public static void main(String[] args){
		System.out.println(new ReverseInteger().reverseInt(-123));
	}
}

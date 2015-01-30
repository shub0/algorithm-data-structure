/**
 * 
 * Multiplier.java
 * Nov 28, 2012
 */

/**
 * @author huangsp
 *
 */
public class Multiplier {
	public String multiply(String num1, String num2){
		if (num2.equals("0") || num1.equals("0")) return "0";
		else if (num2.length() > num1.length()) return multiply(num2, num1);
		else{
			String[] products = new String[num2.length()];
			for (int index = num2.length() - 1; index >= 0; index--){
				products[num2.length() - 1 - index] = singleMultiply(num1, num2.charAt(index));
				for (int index2 = num2.length() - 1; index2 > index; index2--)
					products[num2.length() - 1 - index] +=0;
			}
			return add(products);
		}
		
	}
	private String add(String[] numbers){
		int size = numbers.length;
		int carry = 0;
		StringBuffer sum = new StringBuffer();
		for (int offset = 0; offset < numbers[size - 1].length(); offset++){
			int currentSum = carry;
			for (int index = size - 1; index >=  0; index --){
				if (numbers[index].length() > offset){
					currentSum += (int) (numbers[index].charAt(numbers[index].length() - 1 - offset) - '0');
				}
			}
			carry = currentSum / 10;
			sum.append((char) (currentSum % 10 + '0'));
		}
		if (carry != 0) sum.append((char) (carry + '0'));
		return sum.reverse().toString();
	}
	private String singleMultiply(String num1, char digit){
		StringBuffer num = new StringBuffer(num1).reverse();
		StringBuffer out = new StringBuffer();
		int carry = 0;
		for (int index = 0; index < num.length(); index++){
			int products = (num.charAt(index) - '0') * (digit - '0') + carry;
			int currentDigit = products % 10;
			carry = products / 10;
			out.append((char)(currentDigit+'0'));
		}
		if (carry != 0) out.append((char)(carry + '0'));
		return out.reverse().toString();
	}
	public static void main(String[] args){
		System.out.println(new Multiplier().multiply("523123456","1156678"));
	}
}

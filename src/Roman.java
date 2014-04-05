import java.util.HashMap;


public class Roman {
	HashMap<Character, Integer> romanDigitToInteger;
	char[] romanOnes = {'I','X','C','M'};
	char[] romanFives = {'V','L','D'};
	public Roman() {
		romanDigitToInteger = new HashMap<Character, Integer>();
		romanDigitToInteger.put('I', 1);
		romanDigitToInteger.put('X', 10);
		romanDigitToInteger.put('C', (int)100);
		romanDigitToInteger.put('M', (int)1000);
		romanDigitToInteger.put('V', 5);
		romanDigitToInteger.put('L', (int) 50);
		romanDigitToInteger.put('D', (int) 500);
	}
	public String intToRoman(int num) {
		if (num < 1) return "";
		else {
			int offset = 0;
			StringBuffer romanNumbers = new StringBuffer();
			while (num > 0) {
				int digit = num % 10;
				boolean flag = false;
				if (digit == 9) {
					romanNumbers.append(romanOnes[offset + 1]);
					romanNumbers.append(romanOnes[offset]);
					digit = 0;
				} else if (digit == 4) {
					romanNumbers.append(romanFives[offset]);
					romanNumbers.append(romanOnes[offset]);
					digit = 0;
				} else if (digit >= 5) {
					flag = true;
					digit -= 5;
				}
				while (digit > 0) {
					romanNumbers.append(romanOnes[offset]);
					digit --;
				} 
				if (flag) {
					romanNumbers.append(romanFives[offset]);
				}
				offset ++;
				num /= 10;
			}
			return romanNumbers.reverse().toString();
		}
	}
	public int romanToInteger(String roman) {
		if (roman == null || roman.length() == 0) {
			return 0;
		} else {
			int currentNumber = 0;
			int previousNumber = 0;
			int output = 0;
			for (int index = 0; index < roman.length(); index ++) {
				currentNumber = romanDigitToInteger.get(roman.charAt(index));
				if (currentNumber > previousNumber) {
					output -= 2* previousNumber;
				}
				output += currentNumber;
				previousNumber = currentNumber;
			}
			return output;
		}
	}
	public static void main(String[] args) {
		Roman coverter = new Roman();
		int input = 100;
		System.out.println(input == coverter.romanToInteger(coverter.intToRoman(input)));
	}
}

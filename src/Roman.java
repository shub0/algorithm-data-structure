import java.util.HashMap;

/**
 * 
 * Roman.java
 * Nov 26, 2012
 */

/**
 * @author huangsp
 *
 */
public class Roman {
	char[] TENS = {'I','X', 'C', 'M'};
	char[] FIVES = {'V', 'L', 'D'};
	public String intToRoman(int num){
		int len = 0;
		String[] romanCode = new String[4];
		while ( num > 0){
			romanCode[len] = "";
			int res = num % 10;
			num /= 10;
			if (res == 9){
				romanCode[len] += TENS[len];
				romanCode[len] += TENS[len + 1];
				res = 0;
			}else if (res == 4){
				romanCode[len] += TENS[len];
				romanCode[len] += FIVES[len];
				res = 0;
			}else if(res >= 5){
				romanCode[len] += FIVES[len];
				res -= 5;
			}
			while (res > 0){
				romanCode[len] += TENS[len];
				res --;
			}
			len ++;
		}
		String out = new String();
		for (int index = len - 1; index >= 0; index--){
			out += romanCode[index];
		}
		return out;
	}
	public String intToRoman2(int num){
		if (num < 1)	return "";
		else{
			int offset = 0;
			StringBuffer roman = new StringBuffer();
			while(num > 0){
				int digit = num % 10;
				boolean flag = false;
				if (digit == 9){
					roman.append(TENS[offset + 1]);
					roman.append(TENS[offset]);
					digit = 0;
				}else if(digit == 4){
					roman.append(FIVES[offset]);
					roman.append(TENS[offset]);
					digit = 0;
				}else if (digit >=5 ){
					flag = true;
					digit -= 5;
				}
				for (int index = 0; index < digit; index++){
					roman.append(TENS[offset]);
				}
				if (flag)	roman.append(FIVES[offset]);
				offset++;
				num /= 10;
			}
			roman.reverse();
			return roman.toString();
		}
	}
	public int RomanToInt2(String s){
		HashMap<Character, Integer> romanChar = new HashMap<Character, Integer>();
		romanChar.put('I',1);
		romanChar.put('V', 5);
		romanChar.put('X', 10);
		romanChar.put('L', 50);
		romanChar.put('C',100);
		romanChar.put('D', 500);
		romanChar.put('M', 1000);
		int previous = Integer.MAX_VALUE;
		int len = s.length();
		int number = 0;
		
		for (int index = 0; index < len; index++){
			char currentRoman = s.charAt(index);
			int currentNum = romanChar.get(currentRoman);
			number += currentNum;
			if (currentNum > previous)
				number -= 2*previous;
			previous = currentNum;
		}
		return number;
	}
	public int RomanToInt(String s){
		int len = s.length();
		if (len == 0)	return 0;
		else{
			int number = 0;
			for (int index = 0; index < len; index++){
				char currentChar = s.charAt(index);
				if (currentChar == 'M')		number += 1000;
				else if (currentChar == 'D') 	number += 500;
				else if (currentChar ==  'L')	number += 50;
				else if (currentChar ==  'V')	number += 5;
				else if (currentChar == 'C'){
					if (index < len -1 && (s.charAt(index+1) == 'M' || s.charAt(index+1) == 'D'))
								number -= 100;
					else number += 100;
				}else if(currentChar  == 'X'){
					if (index < len -1 && (s.charAt(index+1) == 'C' || s.charAt(index + 1) == 'L'))
						number -= 10;
					else number += 10;
				}else if(currentChar == 'I'){
					if (index < len - 1 && (s.charAt(index+1) == 'X' || s.charAt(index + 1) == 'V'))
						number -= 1;
					else number += 1;
				}
			}
			return number;
		}
	}
	
	public static void main(String[] args){
		Roman converter = new Roman();
		System.out.println(converter.RomanToInt2("DCCXCVII"));
		System.out.println(converter.intToRoman2(797));
	}
}

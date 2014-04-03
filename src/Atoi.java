
public class Atoi {
	public int atoi(String str) {
		if (str == null || str.trim().length() == 0) {
			return 0;
		} else if (str.trim().charAt(0) == '-') {
			return atoi(str.trim().substring(1), -1);
		} else if (str.trim().charAt(0) == '+') {
			return atoi(str.trim().substring(1), 1);
		} else {
			return atoi(str.trim(), 1);
		}
	}

	private int atoi(String str, int sign) {
		int INT_MAX = 2147483647;
		int INT_MIN = -2147483648;
		int output = 0;
		int len = str.length();
		for (int index = 0; index < len; index ++) {
			char digit = str.charAt(index);
			if (digit > '9' || digit < '0')
				return sign * output;
			output *= 10;
			output += (int)(digit - '0');
			if (output < 0) {
				if (sign < 0) {
					return INT_MIN;
				} else {
					return INT_MAX;
				}
			}
		}
		return sign * output;
	}
	public static void main(String[] args) {
		System.out.println(new Atoi().atoi("  - 321"));
	}
}

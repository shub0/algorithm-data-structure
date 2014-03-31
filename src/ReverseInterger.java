public class ReverseInterger {
	public static int ReverseInteger(int input) {
		if (input == 0)
			return 0;
		else if (input < 0) {
			return -1 * ReverseInteger(-1 * input);
		} else {
			int output = 0;
			while (input > 0) {
				output *= 10;
				output += (input % 10);
				input /= 10;
			}
			return output;
		}
	}
	public static void main(String[] args) {
		System.out.println(ReverseInteger(120));
		System.out.println(ReverseInteger(-123));
	}
}

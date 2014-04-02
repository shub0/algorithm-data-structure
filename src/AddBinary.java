
public class AddBinary {
	public String addBinary(String a, String b) {
		if (a == null || a.length() == 0) {
			return b;
		} else if (b == null || b.length() == 0) {
			return a;
		} else {
			int lenA = a.length();
			int lenB = b.length();
			if (lenA < lenB) return addBinary(b, a);
			int indexA = lenA - 1;
			int indexB = lenB - 1;
			int carry = 0;
			StringBuffer sum = new StringBuffer();
			while(indexA >= 0) {
				carry += (a.charAt(indexA --) - '0');
				if (indexB >= 0) {
					carry += (b.charAt(indexB --) - '0');
				}
				sum.append((char) (carry % 2 + '0'));
				carry /= 2;
			}
			if (carry != 0) sum.append('1');
			return sum.reverse().toString();
		}
	}
	public String addString(String a, String b, int base) throws Exception{
		if (base < 2) {
			throw new Exception("Invalid base");
		}
		int lenA = a.length();
		int lenB = b.length();
		if (lenB == 0) return a;
		if (lenA == 0) return b;
		if (lenA < lenB) return addBinary(b, a);
		int indexA = lenA - 1;
		int indexB = lenB - 1;
		int carry = 0;
		StringBuffer sum = new StringBuffer();
		while(indexA >= 0) {
			carry += (a.charAt(indexA --) - '0');
			if (indexB >= 0) {
				carry += (b.charAt(indexB --) - '0');
			}
			sum.append((char) (carry % base + '0'));
			carry /= base;
		}
		if (carry != 0) sum.append((char) (carry + '0'));
		return sum.reverse().toString();		
	}
	public static void main(String[] args) {
		System.out.println(new AddBinary().addBinary("101", "10"));
	}
}

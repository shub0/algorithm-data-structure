/**
 * 
 * IPAddress.java
 * Dec 4, 2012
 */
import java.util.ArrayList;
/**
 * @author huangsp
 *
 */
public class IPAddress {
	// ugly algorithm
	public ArrayList<String> restoreIpAddresses(String s) {
		ArrayList<String> ipAddressBook = new ArrayList<String>();
		if (s.length() < 4 || s.length() > 12) return ipAddressBook;
		else{
			int len = s.length();
			for (int i = 1; i < len; i++){
				for (int j = i+1; j < len; j++){
					for (int m = j+1; m < len; m++){
						String seg1 = s.substring(0,i);
						String seg2 = s.substring(i,j);
						String seg3 = s.substring(j,m);
						String seg4 = s.substring(m);
						if (isValid(seg1) && isValid(seg2) && isValid(seg3) && isValid(seg4)){
							String ipAddress = seg1 + "." + seg2 + "." + seg3 + "." + seg4;
							ipAddressBook.add(ipAddress);
						}
					}
				}
			}
			return ipAddressBook;
		}
	}
	
	//elegant algorithm
	public ArrayList<String> restoreIpAddresses2(String s) {
		ArrayList<String> ipAddressBook = new ArrayList<String>();
		if (s.length() < 4 || s.length() > 12) return ipAddressBook;
		else{
			generateIPAddress(s, new String(), new String(), 1, ipAddressBook);
			return ipAddressBook;
		}
	}
	
	private void generateIPAddress(String input, String output, String segment, int depth, ArrayList<String> addressBook){
		if (input.length() == 0){
			if (depth == 4 && !output.endsWith("."))
				addressBook.add(output);
		}else{
			segment += input.charAt(0);
			output += input.charAt(0);
			if (isValid(segment)){
				if (depth < 4){
					generateIPAddress(input.substring(1), output + '.', "", depth + 1, addressBook);
				}
				generateIPAddress(input.substring(1), output, segment, depth, addressBook);
			}
		}
	}
	
	private boolean isValid(String s){
		if (s.length() == 0 || s.length() > 3) return false;
		else{
			if (s.length() > 1 && s.startsWith("0")) return false;
			int num = Integer.valueOf(s, 10);
			if (num >= 0 && num < 256) return true;
			else return false;
		}
	}
	public static void main(String[] args){
		System.out.println(new IPAddress().restoreIpAddresses2("0100101"));
	}
}

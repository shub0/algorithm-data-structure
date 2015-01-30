/**
 * 
 * GrayDecoder.java
 * Nov 26, 2012
 */
import java.util.*;
/**
 * @author Shubo Liu
 *
 */
public class GrayDecoder {
	public ArrayList<Integer> grayCode(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
		ArrayList<Integer> grayCode = new ArrayList<Integer>();
		if (n < 1) return grayCode;
		else{
			ArrayList<String> binaryCode = generateCode(n);
			for (String ex: binaryCode){
				grayCode.add(Integer.valueOf(ex, 2));
			}
			return grayCode;
		}
    }
	private ArrayList<String> generateCode(int n){
		ArrayList<String> code = new ArrayList<String>();
		if (n == 1){
			code.add("0");
			code.add("1");
		}
		else{
			ArrayList<String> smallerCode = generateCode(n-1);
			for (int index = 0; index < smallerCode.size(); index++){
				String codeExample = smallerCode.get(index);
				code.add("0" + codeExample);
			}
			for (int index = smallerCode.size() - 1; index >= 0; index--){
				String codeExample = smallerCode.get(index);
				code.add("1" + codeExample);
			}	
		}
		return code;
	}
	public static void main(String[] args){
		System.out.println(new GrayDecoder().grayCode(4));
	}
}

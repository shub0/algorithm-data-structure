import java.util.ArrayList;

/**
 * 
 * PlusOne.java
 * Dec 1, 2012
 */

/**
 * @author huangsp
 *
 */
public class PlusOne {
	public int[] plueOne(int[] num){
		ArrayList<Integer> sum = new ArrayList<Integer>();
		if (num.length == 0) 	return null;
		else{
			int index = num.length - 1;
			int carry = 0;
			for (; index >= 0; index--){
				int sum1 = num[index] + carry;
				carry = sum1 / 10;
				int digit = sum1 % 10;
				sum.add(digit);
			}
			int[] solution = new int[sum.size()];
			for (index = sum.size() - 1; index >=0; index--){
				solution[sum.size() - 1 - index] = sum.get(index);
			}
			return solution;
		}
	}
}

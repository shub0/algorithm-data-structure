import java.util.ArrayList;

/**
 * 
 * PiscalTriangle.java
 * Dec 1, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class PiscalTriangle {
	public ArrayList<Integer> getRow(int rowIndex){
		ArrayList<Integer> row = new ArrayList<Integer>();
		if (rowIndex < 0)	return row;
		else{
			for (int index = 0; index <= rowIndex; index++){
				row.add(combine(rowIndex, index));
			}
			return row;
		}
	}
	private int combine(int base, int choose){
		if (choose == 0) return 1;
		if (choose > base /2) return combine(base, base - choose);
		else{
			double product = 1;
			for (int index = base; index > base - choose; index--){
				product *= index;
			}
			for (int index = 1; index <= choose; index++){
				product /= index;
			}
			return (int)product;
		}
	}
	public static void main(String[] args){
		System.out.println( new PiscalTriangle().getRow(32));
	
	}
}

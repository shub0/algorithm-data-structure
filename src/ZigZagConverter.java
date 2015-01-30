/**
 * 
 * ZigZagConverter.java
 * Dec 5, 2012
 */

/**
 * @author huangsp
 *
 */
public class ZigZagConverter {
	public String zigzagConverter(String str, int row){
		if (row == 1)	return str;
		StringBuffer output = new StringBuffer();
		int len = str.length();
		for (int indexR = 0; indexR < row; indexR++){
			int first = indexR;
			int second = 2 * (row  - 1) - indexR;
			for (int index = 0; index < len; index += 2*(row - 1)){
				if (index + first < len)	output.append(str.charAt(index + first));
				if (first != second && (first % (2 * row - 2) != 0) && index + second < len)	output.append(str.charAt(index + second));
			}
		}
		return output.toString();
	}
	// similar to spiral matrix problem 
	// elegant algorithm
	public String zigzagConverter2(String s, int nRows){
		if (nRows < 2) return s;
        else{
            String[] elements = new String[nRows];
            for (int index = 0; index < nRows; index++){
            	elements[index] = "";
            }
            int increment = 1;
            int index = 0;
            int len = s.length();
            int currentRow = 0;
            int nextRow = 0;
            
            while ( index < len){
                nextRow = increment + currentRow;
                if (nextRow < 0 || nextRow >= nRows){
                    increment *= -1;
                }else{
                    elements[currentRow] += s.charAt(index++);
                    currentRow = nextRow;
                }
            }
            for (index = 1; index < nRows; index++){
            	elements[0] += elements[index];
            }
            return elements[0];
            
        }
	}
	public static void main(String[] args){
		System.out.println(new ZigZagConverter().zigzagConverter("PAYPALISHIRING", 3));
	}
}

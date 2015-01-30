

/**
 * 
 * RotateImage.java
 * Dec 4, 2012
 */

/**
 * @author huangsp
 * Time complexity is O(logN) + O(logM)
 */
public class RotateImage {
	public void rotate(int[][] matrix){
		int size = matrix.length - 1;
		if (size == 0) return;
		for (int indexRow = 0; indexRow <= size; indexRow++){
			for (int indexCol = size - indexRow; indexCol >= 0; indexCol--){
				int newCol = size - indexRow;
				int newRow = size - indexCol;
				int tmp = matrix[indexRow][indexCol];
				matrix[indexRow][indexCol] = matrix[newRow][newCol];
				matrix[newRow][newCol] = tmp;
			}
		}
		for (int indexRow = 0; indexRow <= size/2; indexRow++){
			for (int indexCol = 0; indexCol <= size; indexCol++){
				int newRow = size - indexRow;
				int newCol = indexCol;
				int tmp = matrix[indexRow][indexCol];
				matrix[indexRow][indexCol] = matrix[newRow][newCol];
				matrix[newRow][newCol] = tmp;
			}
		}
	}
	public void rotate2(int[][] matrix) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int ROW = matrix.length;
        int COL = matrix[0].length;
        for (int indexR = 0; indexR < ROW; indexR++){
            for (int indexC = indexR + 1; indexC < COL; indexC++){
                int tmp = matrix[indexR][indexC];
                matrix[indexR][indexC] = matrix[indexC][indexR];
                matrix[indexC][indexR] = tmp;
            }
        }
        for (int indexR = 0; indexR < ROW; indexR++){
            for (int indexC = 0; indexC < COL/2; indexC++){
                int tmp = matrix[indexR][indexC];
                matrix[indexR][indexC] = matrix[indexR][COL - 1 - indexC];
                matrix[indexR][COL - 1 - indexC] = tmp;
            }
        }
    }
	public static void main(String[] args){
		int[][] num = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
		//int[][] num = {{1,3,5}};
		RotateImage myImage = new RotateImage();
		myImage.rotate2(num);
		System.out.println("Done!");
		//System.out.println(myImage.search(num, 3));
	}
}

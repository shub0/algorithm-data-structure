/**
 * 
 * SetZero.java
 * Dec 4, 2012
 */

/**
 * @author huangsp
 *
 */
public class SetZero {
	public void setZero(int[][] matrix){
		boolean firstRow = false;
		boolean firstCol = false;
		int ROW = matrix.length;
		int COL = matrix[0].length;
		for (int index = 0; index < ROW; index++){
			if (matrix[index][0] == 0){
				firstCol = true;
				break;
			}
		}
		for (int index = 0; index < COL; index++){
			if(matrix[0][index] == 0){
				firstRow = true;
				break;
			}
		}
		for (int indexRow = 1; indexRow < ROW; indexRow++){
			for (int indexCol = 1; indexCol < COL; indexCol++){
				if (matrix[indexRow][indexCol] == 0){
					matrix[0][indexCol] = 0;
					matrix[indexRow][0] = 0;
				}
			}
		}
		for (int index = 1; index < ROW; index++){
			if(matrix[index][0] == 0){
				for(int index2 = 0; index2 < COL; index2++){
					matrix[index][index2] = 0;
				}
			}
		}
		for (int index = 1; index < COL; index++){
			if (matrix[0][index] == 0){
				for (int index2 = 0; index2 < ROW; index2++){
					matrix[index2][index] = 0;
				}
			}
		}
		if (firstRow){
			for (int index = 0; index < COL; index++)
				matrix[0][index] = 0;
		}
		if (firstCol){
			for (int index = 0; index < ROW; index++)
				matrix[index][0] = 0;
		}
	}
	public static void main(String[] args){
		int[][] matrix = {{0,2,5,2,2},{2,2,5,8,9},{3,2,9,5,8},{8,6,9,8,9},{2147483647,5,1,6,1}	};	
		SetZero myTest = new SetZero();
		myTest.setZero(matrix);
		System.out.println("Done");
	}
}

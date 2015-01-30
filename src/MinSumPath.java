/**
 * 
 * MinSumPath.java
 * Nov 28, 2012
 */

/**
 * @author huangsp
 *
 */
public class MinSumPath {
	 public int minPathSum(int[][] grid){
		 int R = grid.length;
		 int C = grid[0].length;
		 if (R == 1 && C == 1) return grid[0][0];
		 else{
			 int[][] minCost = new int[R][C];
		     int[] minColumn = new int[C];
		     int[] minRow = new int[R];
		     minColumn[0] = grid[0][0];
		     minRow[0] = grid[0][0];
		     minCost[0][0] = grid[0][0];
		     for (int index = 1; index < R; index ++){
		    	 minCost[index][0] = grid[index][0] + grid[0][0];
		    	 minRow[index] = minCost[index][0];
		     }
		     for (int index = 1; index < C; index++){
		    	 minCost[0][index] = grid[0][index] + grid[0][0];
		    	 minColumn[index] = minCost[0][index];
		     }
		     int indexR = 0;
		     int indexC = 0;
		     for (indexR = 1; indexR < R; indexR++){
		    	 for (indexC = 1; indexC < C; indexC++){
		    		 minCost[indexR][indexC] = Math.min(minRow[indexR], minColumn[indexC]) + grid[indexR][indexC];
		    		 minRow[indexR] = Math.min(minRow[indexR], minCost[indexR][indexC]);
		    		 minColumn[indexC] = Math.min(minColumn[indexC], minCost[indexR][indexC]);
		    	 }
		     }
		     return minCost[indexR - 1][indexC - 1];
		 }
	 }
	 public int minPathSum2(int[][] grid){
		 int ROW = grid.length;
	        int COL = grid[0].length;
	        int[] minRow = new int[ROW];
	        int[] minCol = new int[COL];
	        minRow[0] = grid[0][0];
	        minCol[0] = grid[0][0];
	        for (int index = 1; index < ROW; index ++){
	            minRow[index] = minRow[0] + grid[index][0];
	        }
	        for (int index = 1; index < COL; index ++){
	            minCol[index] = minCol[0] + grid[0][index];
	        }
	        for (int indexRow = 1; indexRow < ROW; indexRow ++){
	            for (int indexCol = 1; indexCol < COL; indexCol ++){
	                int tmp = Math.min(minRow[indexRow], minCol[indexCol]) + grid[indexRow][indexCol];
	                minRow[indexRow] = Math.min(minRow[indexRow], tmp);
	                minCol[indexCol] = Math.min(minCol[indexCol], tmp);
	            }
	        }
	        if (ROW == 1)	return minCol[COL - 1];
	        if (COL == 1)	return minRow[ROW - 1];
	        return Math.min(minCol[COL - 1], minRow[ROW - 1]) + grid[ROW - 1][COL - 1];		 
	 }
	 
	 public static void main(String[] args){
		 int[][] grid = {{1,2,3},{4,5,6}};
		 //int[][] data = {{1,3,2,4},{5,8,9,10},{2,5,4,3},{1,8,10,9}};
		 System.out.println(new MinSumPath().minPathSum2(grid));
	 }
}

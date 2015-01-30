/**
 * 
 * SprilMatrix.java
 * Dec 5, 2012
 */

/**
 * @author huangsp
 *
 */
public class SpiralMatrix {
	
	public static void print(int[][] num){
		int[][] direction = {{0,1},{1,0},{0,-1},{-1,0}};
		boolean[][] visited = new boolean[num.length][num[0].length];
		int ROW = num.length;
		int COL = num[0].length;
		int row = 0, col = 0, i = 0, j = 0, m = 0;
		
		while (!visited[i][j]){
			row = i + direction[m][0];
			col = j + direction[m][1];
			if (row < ROW && row >= 0 && col < COL && col >= 0 && !visited[row][col]){
				System.out.printf("%d ",num[i][j]);
				visited[i][j] = true;
				i = row;
				j = col;
			}else{
				m++;
				if (m > 3)	m = 0;
				row = i + direction[m][0];
				col = j + direction[m][1];
				if (visited[row][col]){
					visited[i][j] = true;
					System.out.println(num[i][j]);	
				}
			}
		}
	}
	public static int[][] set(int N, int M){
		int[][] num = new int[N][M];
		int[][] direction = {{0,1},{1,0},{0,-1},{-1,0}};
		int current = 1;
		int row = 0;
		int col = 0;
		int i = 0, j = 0, m = 0;
		while (current <= N * M){
			row = i + direction[m][0];
			col = j + direction[m][1];
			if (row < N && row >= 0 && col < M && col >= 0 && num[row][col] == 0){
				num[i][j] = current++;
				i = row;
				j = col;
			}else{
				m++;
				if (m > 3) m = 0;
				row = i + direction[m][0];
				col = j + direction[m][1];
				if (num[row][col] != 0){
					num[i][j] = current++;
				}
			}
		}
		return num;
	}
	public static int sqrt(int x){
		if ( x < 2)		return x;
		else{
			double root = x;
			// Newton's recursive method
			for (int i = 0; i < 20; i++){
				root = (root + x / root) /2;
			}
			return (int)(root);
		}
	}
	public static void main(String[] args){
		@SuppressWarnings("unused")
		int matrix[][] = {{1,2,3,4,5},
				{16,17,18,19,6},
				{15,24,25,20,7},
				{14,23,22,21,8},
				{13,12,11,10,9}};
		print (set(5,4));
		//System.out.println(sqrt(16));
	}
}

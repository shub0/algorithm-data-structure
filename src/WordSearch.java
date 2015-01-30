public class WordSearch{
	public boolean exist(char[][] board, String word){
		int ROW = board.length;
		int COL = board[0].length;
		if (word.length() == 0)		return true;
		else if (word.length() > ROW * COL)		return false;
		boolean[][] visited = new boolean[ROW][COL];
		for (int indexR = 0; indexR < ROW; indexR++){
			for (int indexC = 0; indexC < COL; indexC++){
				if (board[indexR][indexC] == word.charAt(0)){
					visited[indexR][indexC] = true;
					if (search(board, indexR, indexC, visited, word.substring(1)))	return true;
					visited[indexR][indexC] = false;
				}
			}
		}
		return false;
	}
		
	private boolean search(char[][] board, int row, int col, boolean[][] visited, String word){
		if (word.length() == 0)	return true;
		int[][] pos = {{row + 1, col}, {row - 1, col}, {row, col + 1}, {row, col - 1}};
		for (int index = 0; index < 4; index++){
			int newRow = pos[index][0];
			int newCol = pos[index][1];
 			if (newRow < board.length && newRow >= 0 
							&& newCol < board[0].length && newCol >= 0 ){
				if (!visited[newRow][newCol] && board[newRow][newCol] == word.charAt(0)){
					visited[newRow][newCol] = true;
					if (search(board, newRow, newCol, visited, word.substring(1))) return true;
					visited[newRow][newCol] = false;
				}
			}
		}
		return false;
	}
	public static void main(String[] args){
		char[][] board= {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
		String word = "ABCCED";
		System.out.println(new WordSearch().exist(board, word));
	}
}
				
/**
 * 
 * Sudoku.java
 * Dec 6, 2012
 */

/**
 * @author huangsp
 *
 */
public class Sudoku {
	char[][] board = new char[9][9];
	int count = 0;
	private void set(int index, int number){
		int row = index / 9;
		int col = index % 9;
		board[row][col] = (char) (number + '0');
	}
	private boolean isValidSudoku(char[][] board) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int ROW = board.length;
        int COL = board[0].length;
        if (ROW != 9 || COL != 9)	return false;
        // check column wise
        for (int indexC = 0; indexC < COL; indexC++){
        boolean[] hashtable = new boolean[ROW];
        	for(int indexR = 0; indexR < ROW; indexR++){
        		if (board[indexR][indexC] == '.')	continue;
        		int currentDigit =  ((int) (board[indexR][indexC] - '0'));
        		if (currentDigit > 0 && currentDigit < 10){
        			if (hashtable[currentDigit - 1])	return false;
        			else hashtable[currentDigit - 1] = true;
        		}else 
        			return false;
        	}
        }
        // check row wise
        for (int indexR = 0; indexR < ROW; indexR++){
        boolean[] hashtable = new boolean[COL];
        	for(int indexC = 0; indexC < COL; indexC++){
        		if (board[indexR][indexC] == '.')	continue;
        		int currentDigit =  ((int) (board[indexR][indexC] - '0'));
        		if (currentDigit > 0 && currentDigit < 10){
        			if (hashtable[currentDigit - 1])	return false;
        			else hashtable[currentDigit - 1] = true;
        		}else 
        			return false;
        	}
        }
        // check each 3*3 cell
        for (int indexR = 0; indexR < ROW; indexR += 3){
        	for (int indexC = 0; indexC < COL; indexC += 3){
        		boolean[] hashtable = new boolean[9];
        		for (int r = 0; r < 3; r++){
        			for (int c = 0; c < 3; c++){
        				int currentRow = indexR + r;
        				int currentCol = indexC + c;
        				if (board[currentRow][currentCol]  == '.')	continue;
        				int currentDigit = ((int) board[currentRow][currentCol] - '0');
        				if (currentDigit > 0 && currentDigit < 10){
        					if (hashtable[currentDigit - 1])	return false;
        					else hashtable[currentDigit - 1] = true;
        				}
        			}
        		}
        	}
        }
        return true;        				
	}
	private void print(char[][] matrix){
		for (int indexR = 0; indexR < 9; indexR ++){
			for (int indexC = 0; indexC < 9; indexC++){
				System.out.printf("%s  ", matrix[indexR][indexC]);
			}
			System.out.println();
		}
	}
	private void copyBoard(char[][] src, char[][] dest){
		for (int indexR = 0; indexR < 9; indexR++)
			for (int indexC = 0; indexC < 9; indexC++)
				dest[indexR][indexC] = src[indexR][indexC];
	}
	private void fillBoard(char[][] draft, int index){
		// find a solution
		if (index == 81){
			copyBoard(draft, board);
			return;
		}
		else{
			int row = index / 9;
			int col = index % 9;
			// a pre-determined slot
			if (draft[row][col] != '.')		fillBoard(draft, index + 1);
			else{
				// brute force algorithm
				for (int num = 1; num < 10; num++){
					if (isValid(draft, row, col, num)){
						// try a number
						draft[row][col] = (char) (num + '0');
						fillBoard(draft, index + 1);
						// back-search
						draft[row][col] = '.';
					}
				}
			}
		}
	}
	private boolean isValid(char[][] board, int row, int col, int num){
		char currentChar = (char)(num + '0');
		// check column and row
		for (int index = 0; index < 9; index++){
			if (board[row][index] == currentChar || board[index][col] == currentChar)	return false;
		}
		// check 3*3 cell
		int cellRow = row / 3;
		int cellCol = col / 3;
		for (int r = cellRow * 3; r < cellRow * 3 + 3; r++)
			for (int c = cellCol * 3; c < cellCol * 3 + 3; c++)
				if (board[r][c] == currentChar)		return false;
		return true;
	}
	
	public Sudoku(int[][] initalNumber) throws IllegalArgumentException{
		for (int indexR = 0; indexR < 9; indexR++){
			for (int indexC = 0; indexC < 9; indexC++){
				board[indexR][indexC] = '.';
			}
		}
		int len = initalNumber.length;
		for (int index = 0; index < len; index++){
			if (initalNumber[index][0] < 0 || initalNumber[index][0] >= 81 
					|| initalNumber[index][1] <= 0 || initalNumber[index][1] > 9)
				throw new IllegalArgumentException("Illegal setting!");
			set(initalNumber[index][0], initalNumber[index][1]);
		}
		if (!isValidSudoku(board))	throw new IllegalArgumentException("Invalid sudoku!");
		System.out.println("A sudoku:");
		print(board);
	}
	public void solveSudoku(){
		char[][] draft = new char[9][9];
		copyBoard(board, draft);
		fillBoard(draft, 0);
		System.out.println("Solution board:");
		print(board);
	}
	public static void main(String[] args){
		int[][] setting = {{0,5}, {1,3}, {4,7}, {9,6}, {12,1},{13,9},{14,5},{19,9},{20,8},{25,6},{27,8},
				{31,6},{35,3},{36,4},{39,8},{41,3},{44,1},{45,7},{53,6},{55,6},{60,2},{61,8},{66,4},{67,1},
				{68,9},{71,5},{76,8},{79,7},{80,9}};
		Sudoku mySudoKu = new Sudoku(setting);
		mySudoKu.solveSudoku();
	}
}

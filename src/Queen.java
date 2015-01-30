/**
 * 
 * Queen.java
 * Nov 30, 2012
 */

/**
 * @author huangsp
 *
 */
public class Queen {
	int[] board ;
	final int INIT = -1000;
	int QUEENS;
	public Queen(int n){
		board = new int[n];
		QUEENS = n;
		for (int index = 0; index < n; index++){
			board[index]  = INIT;
		}
	}
	public void config(){
		int count = 0;
		int row = 0, col = 0;
		while(row < QUEENS){
			//search positions columnwise
			while ( col < QUEENS){
				if (valid(row, col)){		// find a solution
					board[row] = col;
					col = 0;
					break;
				}else{
					col ++;
				}
			}			
			// no valid solution for current row
			if (board[row] == INIT){
				if (row == 0)	break;		// back searching to first row, no more solutions
				else{
					row -- ;				// back searching to last row
					col = board[row] + 1;
					board[row] = INIT;
					continue;
				}
			}
			
			if (row == QUEENS - 1){
				// find a solution
				System.out.printf("Answer %d\n", ++count);
				print();
				col = board[row] + 1;	// search from next column for next solution
				board[row] = INIT;		// reset board
				continue;		
			}
			row++;
		}
	}
	private void print(){
		int i, j;
		for (i = 0; i < QUEENS; i++){
			for (j = 0; j < QUEENS; j++){
				if (board[i] != j)
					System.out.printf("%s", '#');
				else
					System.out.printf("%s", "Q");
			}
			System.out.println();
		}
	}
	// determine if we can put a queen at (row, col)
	private boolean valid(int row, int col){
		for (int index = 0; index < QUEENS; index++){
			// neither on the same column nor on the diagonal position
			if (board[index] == col || Math.abs(index - row) == Math.abs(board[index] - col))
				return false;
		}
		return true;
	}
	public static void main(String[] args){
		Queen myProblem = new Queen(8);
		myProblem.config();
	}
}

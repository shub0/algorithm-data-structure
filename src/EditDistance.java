/**
 * 
 * EditDistance.java
 * Nov 26, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class EditDistance {
	public int minDistance(String S, String T){
		if (S.length() == 0 && T.length() == 0)	return 0;
		else if (S.length() == 0) return T.length();
		else if (T.length() == 0) return S.length();
		else{
			int[][] dynamicMatrix = new int[S.length()][T.length()];
			dynamicMatrix[0][0] = (S.charAt(0) == T.charAt(0)) ? 0 : 1;
			boolean equal = false;
			if (dynamicMatrix[0][0] == 0)	equal = true;
			for (int index = 1; index < S.length(); index++){
				if (T.charAt(0) == S.charAt(index)){
					dynamicMatrix[index][0] = dynamicMatrix[index - 1][0];
				}
				else dynamicMatrix[index][0] = dynamicMatrix[index - 1][0] + 1;
			}
			equal = false;
			if (dynamicMatrix[0][0] == 0)	equal = true;
			for (int index = 1; index < T.length(); index++){
				if (T.charAt(index) == S.charAt(0)) dynamicMatrix[0][index] = dynamicMatrix[0][index - 1];
				else dynamicMatrix[0][index] = dynamicMatrix[0][index - 1] + 1;
			}
			// S[x] = T[y]	f(x, y) = f(x - 1, y - 1)
			// S[x] != T[y]		f(x, y) = min(f(x - 1, y - 1), f(x - 1, y), f(x, y - 1)) + 1
			for (int indexS = 1; indexS < S.length(); indexS++){
				for (int indexT = 1; indexT < T.length(); indexT++){
					if (T.charAt(indexT) == S.charAt(indexS))	dynamicMatrix[indexS][indexT] = dynamicMatrix[indexS - 1][indexT - 1];
					else {
						dynamicMatrix[indexS][indexT] = 1 + Math.min(dynamicMatrix[indexS - 1][indexT],
								Math.min(dynamicMatrix[indexS][indexT - 1], dynamicMatrix[indexS - 1][indexT - 1]));
					}
					
				}
			}
			return dynamicMatrix[S.length() - 1][T.length() - 1];
		}
	}
	public static void main(String[] args){
		System.out.println(new EditDistance().minDistance("ab", "aaaa"));
	}
}

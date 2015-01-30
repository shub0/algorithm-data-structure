/**
 * 
 * WordLadder.java
 * Mar 23, 2013
 */
import java.util.ArrayList;


/**
 * @author huangsp
 *
 */

public class WordLadder{
	int[][] edges;
	public void buildGraph(ArrayList<String> dictionary){
		edges = new int[dictionary.size()][dictionary.size()];
		for (int src = 0; src < dictionary.size(); src ++){
			for (int dest = 0; dest < dictionary.size(); dest++){
				//edges[src][dest] = (new EditDistance().minDistance(dictionary.get(src), dictionary.get(dest)) == 1) ? 1 : 0;
				edges[src][dest] = check(dictionary.get(src), dictionary.get(dest)) ? 1 : 0;
				edges[dest][src] = edges[src][dest];
			}
		}
	}
	private boolean check(String src, String dest){
		if (src.length() < dest.length())	return check(dest, src);
		else{
			if (src.length() - dest.length() > 1)	return false;
			else{
				boolean connected = true;
				if (src.length() > dest.length()) connected = false;
				for (int index = 0; index < dest.length(); index ++){
					if (src.charAt(index) == dest.charAt(index))	continue;
					if (!connected)	return false;
					else connected = false;
				}
				return true;
			}
		}
	}
	public ArrayList<String> search(ArrayList<String> dictionary, String src, String dest){
		dictionary.add(0, src);
		dictionary.add(dest);
		buildGraph(dictionary);
		ArrayList<Integer> path = Dijkstra(0, dictionary.size() - 1);
		ArrayList<String> ladder = new ArrayList<String>();
		for (int current : path){
			ladder.add(dictionary.get(current));
		}
		return ladder;
	}
	private ArrayList<Integer> Dijkstra(int src, int dest){
		int size = edges.length;
		int[] estimate = new int[size];
		int[] pi = new int[size];
		int[][] matrix = edges;
		boolean[] inSet = new boolean[size];
		for (int index = 0; index < size; index ++){
			pi[index] = -1;
			estimate[index] = Integer.MAX_VALUE;
		}
		estimate[src] = 0;
		int sizeOfQ = size;
		while (sizeOfQ > 0){
			// Extract minimum from queue
			int current = extractMin(inSet, estimate);
			if (current == -1)   break;
			sizeOfQ --;
			// remove current node from candidate
			inSet[current] = true;
			// Iterator all neighbor of current node 
			int nextVertex = 0;
			while (nextVertex < size){
				if (edges[current][nextVertex] != 0){
					relax(estimate, current, nextVertex, matrix, pi);
				}
				nextVertex ++;
			}
		}		
		// Get shortest path and print
		ArrayList<Integer> path = new ArrayList<Integer>();
		int current = dest;
		while(current != src){
			path.add(0,current);
			current = pi[current];
		}
		path.add(0, src);
		System.out.println(estimate[dest]);
		return path;	
	}
	private int extractMin(boolean[] inSet, int[] estimate){
		int min = Integer.MAX_VALUE, minIndex = -1;
		for (int index = 0; index < estimate.length; index ++){
			if (!inSet[index]){
				if (estimate[index] < min){
					min = estimate[index];
					minIndex = index;
				}
			}
		}
		return minIndex;
	}
	private void relax(int[] estimate, int source, int dest, int[][] matrix, int[] pi){
		if (estimate[dest] > estimate[source] + matrix[source][dest]){
			estimate[dest] = estimate[source] + matrix[source][dest];
			pi[dest] = source;
		}		
	}
	public static void main(String[] args){
		ArrayList<String> dictionary = new ArrayList<String>();
		dictionary.add("hot");
		dictionary.add("dot");
		dictionary.add("lot");
		dictionary.add("dog");
		dictionary.add("log");
		WordLadder myTest = new WordLadder();
		System.out.println(myTest.search(dictionary, "hit","cog"));
	}
}


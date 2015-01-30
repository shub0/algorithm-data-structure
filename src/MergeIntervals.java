/**
 * 
 * MergeIntervals.java
 * Nov 28, 2012
 */

/**
 * @author huangsp
 *
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class MergeIntervals {
	private class comp implements Comparator<Interval>{
		public int compare(Interval o1, Interval o2) {
			// TODO Auto-generated method stub
			return o1.end - o2.end;
		}	
	}
	public ArrayList<Interval> merge(ArrayList<Interval> intervals) {		
		if (intervals.size() == 0) return new ArrayList<Interval>();
		else if (intervals.size() == 1) return intervals;
		else{
			Collections.sort(intervals,new comp());
			ArrayList<Interval> mergeList = new ArrayList<Interval>();
			mergeList.add(intervals.get(0));
			int start = intervals.get(0).start;
			int end = intervals.get(0).end;
			for (int index = 1; index < intervals.size(); index ++ ){
				// overlapping
				Interval currentInterval = intervals.get(index);
				if (end >= currentInterval.start){
					while (mergeList.size () > 0 && mergeList.get(mergeList.size() - 1).end >= currentInterval.start){
						Interval lastInterval = mergeList.remove(mergeList.size() - 1);
						start = Math.min(currentInterval.start, lastInterval.start);
						end = Math.max(end, currentInterval.end);	
					}
					mergeList.add(new Interval(start, end));
					// no overlapping
				}else{
					mergeList.add(currentInterval);
					end = currentInterval.end;
				}
			}
			return mergeList;
		}
	}
	public static void main(String[] args){
		ArrayList<Interval> intervals = new ArrayList<Interval>();
		intervals.add(new Interval(2,3));
		intervals.add(new Interval(2,2));
		intervals.add(new Interval(3,3));
		intervals.add(new Interval(1,3));
		intervals.add(new Interval(5,7));
		intervals.add(new Interval(5,7));
		
		System.out.println(new MergeIntervals().merge(intervals));
	}
}

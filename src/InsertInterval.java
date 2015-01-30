/**
 * 
 * InsertInterval.java
 * Nov 26, 2012
 */

/**
 * @author huangsp
 *
 */
import java.util.*;
class Interval{
	int start;
	int end;
	public Interval(int s, int e){
		start = s;
		end = e;
	}
	public String toString(){
		return "[" + start + ", " + end + "]";
	}
}
public class InsertInterval{
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<Interval> newIntervals = new ArrayList<Interval>();
        if (intervals.size() == 0){
        	newIntervals.add(newInterval);
        }else{
        	int size = intervals.size();
        	int index = 0;
        	boolean flag = false;
        	for (index = 0; index < size; index++){
        		Interval current = intervals.get(index);
        		// no overlapping with current interval
        		if (current.end < newInterval.start){
        			newIntervals.add(current);
        			continue;
        		}
        		// no overlapping with current interval
        		if (current.start > newInterval.end){
        			if (!flag){
        				newIntervals.add(newInterval);
        			}
        			flag = true;
        			newIntervals.add(current);
        			continue;
        		}
        		// overlapping, update newInterval start and end pos
        		if (current.start < newInterval.start){
        			newInterval.start = current.start;
        		}
        		if (current.end > newInterval.end){
        			newInterval.end = current.end;
        			newIntervals.add(newInterval);
        			flag = true;
        		}
        	}
        	if (!flag)
        		newIntervals.add(newInterval);
        }
        return newIntervals;
    }
}

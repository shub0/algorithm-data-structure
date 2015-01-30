/**
 * 
 * LargestRectangle.java
 * Nov 27, 2012
 */
import java.util.Stack;
/**
 * @author huangsp
 *
 */
public class LargestRectangle {
	public int largestRectangleArea(int[] height) {
        // Start typing your Java solution below
        // DO NOT write main() function
		int len = height.length;
        if (len == 0)   return 0;
        else{
            Stack<Integer> h = new Stack<Integer>();
            Stack<Integer> indices = new Stack<Integer>();
            int maxArea = height[0];
            for (int index = 0; index < len; index ++){
                if (h.isEmpty() || height[index] >= h.peek()){
                    h.push(height[index]);
                    indices.push(index);
                }else if (height[index] < h.peek()){
                    int lastIndex = 0;
                    while(!h.isEmpty() && height[index] < h.peek()){
                        lastIndex = indices.pop();
                        int tmpArea = h.pop() * (index - lastIndex);
                        maxArea = Math.max(maxArea, tmpArea);
                    }
                    h.push(height[index]);
                    indices.push(lastIndex);
                }
            }
            while ( !h.isEmpty()){
                int lastIndex = indices.pop();
                int tmpArea = h.pop() * (len - lastIndex);
                maxArea = Math.max(maxArea, tmpArea);
            }
            return maxArea;
        }
    }
	public static void main(String[] args){
		int[] height = {1,2,3,4,5,6,5};
		System.out.println(new LargestRectangle().largestRectangleArea(height));
	}
}

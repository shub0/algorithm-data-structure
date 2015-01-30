/**
 * 
 * BuyStock.java
 * Nov 26, 2012
 */

/**
 * @author Shubo Liu
 *	Time and space complexity is O(n)
 */
public class BuyStock {
	// limit two transitions 
	public int maxProfit3(int[] prices){
		int len = prices.length;
		if (len < 2) 	return 0;
		else{
			int[] Profit = new int[len];
			int profit = 0;
			// assume buy at the beginning of period
			int buyPrice = prices[0];
			for (int index = 0; index < len; index++){
				if (prices[index] > buyPrice){
					// if sell stock at index time
					// make a comparison
					profit = Math.max(profit, prices[index] - buyPrice);
				}else{
					buyPrice = prices[index];
				}
				Profit[index] += profit;
			}
			// assume sell at the end of period
			int sellPrice = prices[len - 1];
			profit = 0;
			Profit[len - 1] += profit;
			for (int index = len - 2; index > -1; index --){
				if (prices[index] < sellPrice){
					// buy stock at index time
					profit = Math.max(profit, sellPrice - prices[index]);
				}else{
					sellPrice = prices[index];
				}
				Profit[index] += profit;
			}
			int maxProfit = Profit[0];
			for (int index = 1; index < len; index++){
				if (Profit[index] > maxProfit)
					maxProfit = Profit[index];
			}
			return maxProfit;
		}
	}
	public int maxProfit2(int[] prices){
		boolean share = false;
		int buyPrice = prices[0];
		int profit = 0;
		for(int index = 0; index < prices.length - 1; index ++){
			if (prices[index] < prices[index + 1]){
				if (!share){
					buyPrice = prices[index];
					share = true;
				}
			}else{
				if (share){
					profit += (prices[index] - buyPrice);
					share = false;
				}
			}
		}
		if (share)	profit += (prices[prices.length - 1] - buyPrice);
		return profit;
	}
	// limit one transition
	public int maxProfit(int[] prices){
		int buyPrice = prices[0];
		int profit = 0;
		for (int index = 0; index < prices.length; index ++){
			if (prices[index] < buyPrice)	buyPrice = prices[index];
			else{
				profit = Math.max(profit, prices[index] - buyPrice);
			}
		}
		return profit;
	}
	public static void main(String[] args){
		int[] prices = {5,4,3,6,8,10,9,15};
		BuyStock myTest = new BuyStock();
		System.out.println(myTest.maxProfit2(prices));
	}
}

import java.util.*;

public class Lab8 {
    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;

        coinChange(coins, amount);
    }

    public static int coinChange(int[] coins, int amount) {
        int[] combo = new int[amount + 1];
        Arrays.fill(combo, 0);

        combo[0] = 1;

        for (int i = 0; i < coins.length; i++) {
            for (int j = 0; j < combo.length; j++) {
                if (coins[i] <= j) {
                    combo[j] += combo[j - coins[i]];
                }
            }
        }

        System.out.println(combo[amount]);
        return combo[amount];
    }
}

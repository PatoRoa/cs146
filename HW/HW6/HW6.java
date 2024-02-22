import java.util.*;

public class HW6 {
    public static void main (String[] args) {
        int[] list = {-5, 0, 5, -10, 10, 0};

        System.out.println(threeSum(list));
    }
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;

        List<List<Integer>> triplets = new ArrayList<>();

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int sum = nums[i] + nums[j] + nums[k];

                    ArrayList<Integer> tempList = new ArrayList<>();
                    tempList.add(nums[i]);
                    tempList.add(nums[j]);
                    tempList.add(nums[k]);

                    if (sum == 0) {
                        if (!triplets.contains(tempList)) {
                            triplets.add(tempList);
                        }
                    }
                }
            }
        }
        return triplets;
    }
}

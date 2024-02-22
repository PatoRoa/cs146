import java.util.ArrayList;
import java.util.Collections;

public class HW6 {
    public static void main (String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(-5);
        list.add(0);
        list.add(5);
        list.add(-10);
        list.add(10);
        list.add(0);

        threeSum(list);

    }
    public static ArrayList<ArrayList<Integer>> threeSum(ArrayList<Integer> nums) {
        Collections.sort(nums);
        int n = nums.size();

        ArrayList<ArrayList<Integer>> triplets = new ArrayList<>();

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int sum = nums.get(i) + nums.get(j) + nums.get(k);

                    ArrayList<Integer> tempList = new ArrayList<>();
                    tempList.add(nums.get(i));
                    tempList.add(nums.get(j));
                    tempList.add(nums.get(k));

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

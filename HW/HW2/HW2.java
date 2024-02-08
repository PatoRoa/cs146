import java.util.ArrayList;

public class HW2 {
    public static void main (String[] args) {
        int badVersion = 9;
        int n = 10;
        ArrayList<Integer> versions = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            versions.add(i);
        }

        int result = checkFirstBadVersion(versions, 0, versions.size() - 1, badVersion);

        if (result != -1) {
            System.out.println("The first bad version is ");
            System.out.println(result);
        }
        else {
            System.out.println("There are no bad versions");
        }
    }
    public static int checkFirstBadVersion (ArrayList<Integer> versions, int low, int high, int badVersion) {
        // Base case
        if (high >= low) {
            int mid = Math.floorDiv(high + low,2);

            // If the bad version is in the middle
            // original if (versions.get(mid) == badVersion)
            if isBadVersion(versions.get(mid)) {
                return mid;
            }

            // If the bad version is in the left subarray
            else if (versions.get(mid) > badVersion) {
                return checkFirstBadVersion(versions, low, mid - 1, badVersion);
            }

            else {
                return checkFirstBadVersion(versions, mid + 1, high, badVersion);
            }
        }

        else {
            // If there are no bad versions
            return -1;
        }
    }
}

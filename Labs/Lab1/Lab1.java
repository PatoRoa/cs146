import java.util.*;

public class Lab1 {
    public static void main (String[] args) {
        int[] nums = {1, 3, 5, 7, 9};
        int target = 6;

        termIndices(nums, target);
    }
    public static void termIndices (int[] numbers, int sum) {
        for (int i = 0; i <= numbers.length - 1; i++) {
            if (checkContains(sum -numbers[i], numbers)) {
                if (checkIndex(numbers, numbers[i]) == checkIndex(numbers, sum - numbers[i])) {
                    System.out.println("Term indices cannot be repeated");
                    return;
                }
                else {
                    System.out.println("Indices: ");
                    System.out.println(i);
                    System.out.println(checkIndex(numbers, sum - numbers[i]));
                    return;
                }
            }
            else {
                System.out.println("Not enough terms that can add up to the target");
                return;
            }
        }
    }

    public static boolean checkContains(int term, int[] numbers) {
        boolean contains = false;
        for (int j : numbers) {
            if (j == term) {
                contains = true;
            }
        }
        return contains;
    }

    public static int checkIndex(int[] numbers, int term) {
        if (numbers == null) {
            return -1;
        }

        int length = numbers.length;
        int i = 0;

        while (i < length) {
            if (numbers[i] == term) {
                return i;
            }
            else {
                i += 1;
            }
        }
        return -1;
    }
}

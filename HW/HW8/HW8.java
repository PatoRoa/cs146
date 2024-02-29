public class HW8 {
    public static void main (String[] args) {
        String string = "abccccdd";
        longestPalindrome(string);
    }

    public static int longestPalindrome(String s) {
        int[] count = new int[128];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i)]++;
        }

        int result = 0;
        for (int i : count) {
            result += i - (i & 1);

            if (result % 2 == 0 && i % 2 == 1) {
                result++;
            }
        }

        System.out.println(result);
        return result;
    }
}

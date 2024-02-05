public class HW1 {
    public static void main(String[] args) {
        String s = "malayalam";
        checkPalindrome(s);
    }
    public static void checkPalindrome(String string) {
        char[] arrayS = string.toCharArray();

        char[] arrayT = new char[string.length()];
        int j = 0;
        for (int i = string.length() - 1; i >= 0; i--) {
            arrayT[j] = arrayS[i];
            j++;
        }

        for (int k = 0; k < string.length() - 1; k++) {
            if (arrayS[k] == arrayT[k]) {
                continue;
            }
            else {
                System.out.println(string + " is not a palindrome.");
                return;
            }
        }
        System.out.println(string + " is a plaindrome.");
        return;
    }
}
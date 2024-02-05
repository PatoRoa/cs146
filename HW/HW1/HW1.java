import java.util.ArrayList;

public class HW1 {
    public static void main(String[] args) {
        String s = "Malay alam";
        checkPalindrome(s);
    }
    public static void checkPalindrome(String string) {
        char[] tempArray = string.toCharArray();
        ArrayList<Character> array = new ArrayList<Character>();

        for (int i = 0; i <= tempArray.length - 1; i++) {
            if (Character.isLetterOrDigit(tempArray[i])) {
                array.add(Character.toLowerCase(tempArray[i]));
            }
        }

        ArrayList<Character> arrayT = new ArrayList<Character>();

        int j = 0;
        for (int i = array.size() - 1; i >= 0; i--) {
            arrayT.add(array.get(i));
            j++;
        }

        if (array.equals(arrayT)) {
            System.out.println(string + " is a palindrome.");
            return;
        }
        else {
            System.out.println(string + " is not a palindrome.");
        }
    }
}

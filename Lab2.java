// Given two strings, s and t, return true if t is an anagram of s

public class Lab2 {
    public static void main (String[] args) {
        String s = "bart";
        String t = "brat";
        checkAnagram(s, t);
    }
    public static void checkAnagram(String string1, String string2) {
        char[] arr1 = string1.toCharArray();
        char[] arr2 = string2.toCharArray();

        if (string1.length() == string2.length()) {
            for (int i = 0; i <= arr1.length - 1; i++) {

                int counter = 0;

                for (int j = 0; j <= arr2.length - 1; j++) {

                    if (arr1[i] == arr2[j]) {

                        counter++;

                        if (counter == 2) {
                            System.out.println("t is not an anagram of s, repeated letters.");
                            return;
                        }
                    }
                }

                if (counter == 0) {
                    System.out.println("t is not an anagram of s, missing or incorrect letters.");
                    return;
                }
            }
            System.out.println("t is an anagram of s.");
            return;
        }
        else {
            System.out.println("s and t are not the same size.");
            return;
        }
    }
}
import java.util.ArrayList;

public class fibonacci {
    public static void main(String[] args) {
        System.out.println(fibonacci(10));
    }
    public static Integer fibonacci(Integer n) {
        ArrayList<Integer> f = new ArrayList<>();
        f.add(0);
        f.add(1);

        for (int i = 2; i <= n + 1; i++) {
            f.add(f.get(i - 1) + f.get(i - 2));
        }
        return f.get(n);
    }
}

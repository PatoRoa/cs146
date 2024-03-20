import java.util.*;

public class HW11 {
    public static void main(String[] args) {
        int[][] image = {  {1,1,1}, {1,1,0}, {1,0,1}  };
        int sr = 1;
        int sc = 1;

        floodFill(image, sr, sc, 2);
    }

    public static int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int old_color = image[sr][sc];

        flood(image, sr, sc, color, old_color);

        System.out.println(Arrays.deepToString(image));
        return image;
    }

    public static void flood(int[][] image, int sr, int sc, int color, int old_color) {
        if (sr < 0 || sr >= image.length) {
            return;
        }
        if (sc < 0 || sc >= image[0].length){
            return;
        }
        if (image[sr][sc] == color || image[sr][sc] != old_color) {
            return;
        }

        image[sr][sc] = color;

        flood(image, sr - 1, sc, color, old_color);
        flood(image, sr + 1, sc, color, old_color);
        flood(image, sr, sc + 1, color, old_color);
        flood(image, sr, sc - 1, color, old_color);
    }
}

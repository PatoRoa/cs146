import java.util.*;

public class Lab6 {
    public static void main(String[] args) {
        int numCourses = 2;
        int[][] prerequisites = { {1, 0} };

        canFinish(numCourses, prerequisites);
    }

    public static boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] adj = new List[numCourses];
        int[] indegree = new int[numCourses];
        List<Integer> result = new ArrayList<>();

        for (int[] i : prerequisites) {
            int class_take = i[0];
            int class_need = i[1];

            if (adj[class_need] == null) {
                adj[class_need] = new ArrayList<>();
            }

            adj[class_need].add(class_take);
            indegree[class_take]++;
        }

        Queue<Integer> que = new LinkedList<>();
        for (int j = 0; j < numCourses; j++) {
            if (indegree[j] == 0) {
                que.add(j);
            }
        }

        while (!que.isEmpty()) {
            int current = que.poll();
            result.add(current);

            if (adj[current] != null) {
                for (int k : adj[current]) {
                    indegree[k]--;

                    if (indegree[k] == 0) {
                        que.add(k);
                    }
                }
            }
        }

        System.out.println(result.size() == numCourses);
        return result.size() == numCourses;
    }
}

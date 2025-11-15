import java.util.*;

public class Main {
    static class Node {
        int y, x;

        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        int[][] starts = new int[k][2];
        for (int i = 0; i < k; i++) {
            starts[i][0] = sc.nextInt();
            starts[i][1] = sc.nextInt();
        }
        // Please write your code here.
        int answer = 0;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        boolean[][] visited = new boolean[n][n];
        ArrayDeque<Node> dq = new ArrayDeque<>();

        for(int i = 0; i < k; i++) {
            int y = starts[i][0] - 1;
            int x = starts[i][1] - 1;
            Node start = new Node(y, x);
            visited[y][x] = true;
            dq.add(new Node(y, x));
        }

        while(!dq.isEmpty()) {
            Node current = dq.poll();

            for(int[] d: directions) {
                int my = current.y + d[0];
                int mx = current.x + d[1];

                if(0 <= my && my < n && 0 <= mx && mx < n && grid[my][mx] == 0 && !visited[my][mx]) {
                    visited[my][mx] = true;
                    dq.add(new Node(my, mx));
                }
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(visited[i][j]) {
                    answer++;
                }
            }
        }

        System.out.println(answer);
    }
}
import java.util.*;

public class Main {
    static int n, m;
    static int[][] grid;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        grid = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.
        search();
    }

    static class Node {
        int y, x;

        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static void search() {
        ArrayDeque<Node> dq = new ArrayDeque<Node>(Arrays.asList(new Node(0, 0)));
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while(!dq.isEmpty()) {
            Node current = dq.poll();

            for(int i = 0; i < 4; i++) {
                int my = current.y + directions[i][0];
                int mx = current.x + directions[i][1];

                if(0 <= my && my < n && 0 <= mx && mx < m && grid[my][mx] == 1 && !visited[my][mx]) {
                    visited[my][mx] = true;
                    dq.add(new Node(my, mx));
                }
            }
        }

        System.out.println(visited[n-1][m-1] == true ? 1 : 0);
    }
}
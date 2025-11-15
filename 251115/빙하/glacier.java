import java.util.*;

public class Main {
    static int n, m;
    static int[][] grid;
    static int time = 0;
    static int ice = 0;
    static class Node {
        int y, x;

        Node(int y, int x) {
            this.y=y;
            this.x=x;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        grid = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == 1) {
                    ice++;
                }
            }
        }

        int melted_ice = 0;
        while(ice > 0) {
            melted_ice = melt();
            ice -= melted_ice;
            time++;
        }

        System.out.println(time + " " + melted_ice);
    }

    static int melt() {
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        ArrayDeque<Node> dq = new ArrayDeque<>();
        dq.add(new Node(0, 0));
        ArrayList<Node> check = new ArrayList<>();

        while(!dq.isEmpty()) {
            Node current = dq.poll();

            for(int[] d: directions) {
                int my = current.y + d[0];
                int mx = current.x + d[1];

                if(0 <= my && my < n && 0 <= mx && mx < m && !visited[my][mx]) {
                    Node data = new Node(my, mx);
                    visited[my][mx] = true;

                    if(grid[my][mx] == 0) {
                        dq.add(data);
                    } else {
                        check.add(data);
                    }
                }
            }
        }

        for(Node i: check) {
            grid[i.y][i.x] = 0;
        }

        return check.size();
    }
}
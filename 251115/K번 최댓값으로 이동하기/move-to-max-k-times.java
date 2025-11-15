import java.util.*;

public class Main {
    static int n, k;
    static int[][] grid;
    static int r, c;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static Answer answer;
    static class Node {
        int y, x;
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static class Answer extends Node {
        int value;

        Answer(int y, int x, int value) {
            super(y, x);
            this.value = value;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        r = sc.nextInt() - 1;
        c = sc.nextInt() - 1;
        // Please write your code here.
        answer = new Answer(-1, -1, -1);
        for(int i = 0; i < k; i++) {
            if(search()) {
                r = answer.y;
                c = answer.x;
            } else {
                break;
            }
        }
        System.out.println((answer.y + 1) + " " + (answer.x + 1));
    }

    static boolean search() {
        boolean[][] visited = new boolean[n][n];
        ArrayDeque<Node> dq = new ArrayDeque<Node>();
        dq.add(new Node(r, c));
        int value = grid[r][c];
        answer.value = -1;

        while(!dq.isEmpty()) {
            Node current = dq.poll();

            for(int[] d: directions) {
                int my = current.y + d[0];
                int mx = current.x + d[1];
                if(0 <= my && my < n && 0 <= mx && mx < n && grid[my][mx] < value && !visited[my][mx]) {
                    visited[my][mx] = true;
                    dq.add(new Node(my, mx));
                    if(answer.value < grid[my][mx] || (answer.value == grid[my][mx] && answer.y > my) || (answer.value == grid[my][mx] && answer.y == my && answer.x > mx)) {
                        answer = new Answer(my, mx, grid[my][mx]);
                    }
                }
            }
            if(answer.value == -1) {
                return false;
            }
        }

        return true;
    }
}
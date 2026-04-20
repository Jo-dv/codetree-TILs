import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static Node[] arr;
    static int n;
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;

    public static class Node {
        int x, y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void search(int prev, int nxt, int cnt, int distance) {
        if(nxt == n-1) {
            if(cnt == n-1) {
                answer = Math.min(answer, distance);
            }
            return;
        }

        for(int i = nxt + 1; i < n; i++) {
            int new_distance = Math.abs(arr[nxt].x - arr[i].x) + Math.abs(arr[nxt].y - arr[i].y);
            search(nxt, i, cnt + 1, distance + new_distance);
        }
    }

    public static void main(String[] args) throws IOException {
        // Please write your code here.
        n = Integer.parseInt(br.readLine());
        arr = new Node[n];
        visited = new boolean[n];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            Node node = new Node(x, y);
            arr[i] = node;
        }

        visited[0] = true;
        visited[n-1] = true;
        for(int i = 1; i < n; i++) {
            int initial_dist = Math.abs(arr[0].x - arr[i].x) + Math.abs(arr[0].y - arr[i].y);
            search(0, i, 2, initial_dist);
        }

        System.out.println(answer);
    }
}
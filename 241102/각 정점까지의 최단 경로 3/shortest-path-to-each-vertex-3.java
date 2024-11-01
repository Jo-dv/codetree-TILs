import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m;
    static int s, e, c;
    static List<Node>[] graph;

    static class Node {
        int end, cost;

        public Node(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        for(int i = 0; i <= n; i++)
            graph[i] = new ArrayList<>();

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            graph[s].add(new Node(e, c));
        }

        dijkstra();
    }

    static void dijkstra() {
        int[] cost = new int[n + 1];
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
        Arrays.fill(cost, Integer.MAX_VALUE);
        cost[1] = 0;
        pq.add(new Node(1, 0));

        while(!pq.isEmpty()) {
            Node current = pq.poll();

            if(cost[current.end] < current.cost)
                continue;

            for(Node next: graph[current.end]) {
                if(current.cost + next.cost < cost[next.end]) {
                    cost[next.end] = current.cost + next.cost;
                    pq.add(new Node(next.end, current.cost + next.cost));
                }
            }
        }

        for(int i = 2; i <= n; i++)
            System.out.println(cost[i] == Integer.MAX_VALUE ? -1 : cost[i]);
    }
}
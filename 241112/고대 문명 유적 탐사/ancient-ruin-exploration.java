import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int k, m;
    static int[][] relic;
    static ArrayDeque<Integer> board = new ArrayDeque<>();
    static int socre;
    static StringBuilder answer = new StringBuilder();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        relic = new int[5][5];
        for(int i = 0; i < 5; i ++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 5; j++)
                relic[i][j] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++)
            board.add(Integer.parseInt(st.nextToken()));

        solve();
    }

    static int[][] rotate(int y, int x, int cnt) {
        int[][] rotated_relic = new int[5][5];
        for(int i = 0; i < 5; i++)
            rotated_relic[i] = relic[i].clone();

        int temp = -1;
        for(int i = 0; i < cnt; i++) {
        	temp = rotated_relic[y][x + 2];
            rotated_relic[y][x + 2] = rotated_relic[y][x];
            rotated_relic[y][x] = rotated_relic[y + 2][x];
            rotated_relic[y + 2][x] = rotated_relic[y + 2][x + 2];
            rotated_relic[y + 2][x + 2] = temp;
            temp = rotated_relic[y][x + 1];
            rotated_relic[y][x + 1] = rotated_relic[y + 1][x];
            rotated_relic[y + 1][x] = rotated_relic[y + 2][x + 1];
            rotated_relic[y + 2][x + 1] = rotated_relic[y + 1][x + 2];
            rotated_relic[y + 1][x + 2] = temp;
        }

        return rotated_relic;
    }

    static void fill_relic(int[][] rest_relic) {
        for(int x = 0; x < 5; x++)
            for(int y = 4; y > -1; y--)
                if(rest_relic[y][x] == 0)
                    rest_relic[y][x] = board.pollFirst();
    }

    static int find_relic(int[][] rotated_relic) {
        int score = 0;
        boolean[][] visited = new boolean[5][5];
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for(int i = 0; i < 5; i++)
            for(int j = 0; j < 5; j++) {
                if(!visited[i][j]) {
                	ArrayDeque<int[]> found = new ArrayDeque<>();
                    ArrayDeque<int[]> dq = new ArrayDeque<>();
                    found.add(new int[] {i, j});
                    dq.add(new int[] {i, j});
                    visited[i][j] = true;

                    while(!dq.isEmpty()) {
                        int[] current = dq.pollFirst();
                        int y = current[0], x = current[1];
                        for(int[] d: directions) {
                            int my = y + d[0], mx = x + d[1];
                            if(0 <= my && my < 5 && 0 <= mx && mx < 5 && !visited[my][mx] && rotated_relic[y][x] == rotated_relic[my][mx]) {
                                visited[my][mx] = true;
                                dq.add(new int[] {my, mx});
                                found.add(new int[] {my, mx});
                            }
                        }
                    }
                    if(found.size() >= 3) {
                        score += found.size();
                        while(!found.isEmpty()) {
                        	int[] current = found.pollFirst();
                            int y = current[0], x = current[1];
                            rotated_relic[y][x] = 0; 
                        }
                    }
                }
            }

        
        return score;
    }

    static void solve() {
        for(int trial = 1; trial <= k; trial++) {
            int max_score = 0;
            int[][] found = null;
            int[][] rotated_relic = null;
            for(int cnt = 1; cnt <= 3; cnt++) {  //  돌리는 횟수를 최소화해야 하므로 단계적으로 실행
                for(int y = 0; y < 3; y++)
                    for(int x = 0; x < 3; x++) {
                        rotated_relic = rotate(y, x, cnt);
                        int current_score = find_relic(rotated_relic);
                        if(current_score > max_score) {
                            max_score = current_score;
                            found = rotated_relic; // 최대값으로 갱신되는 유물 구조를 찾은 경우
                        }
                    }
            }

            if(found == null)  // 유물의 갱신이 일어나지 않았다면 모든 턴 종료
                break;

            while(true) {
                fill_relic(found);
                int rest_score = find_relic(found);
                if(rest_score == 0)
                    break;
                max_score += rest_score;
                
            }
            for(int i = 0; i < 5; i++)
                relic[i] = found[i].clone();
            answer.append(max_score).append(" ");
        }
        System.out.println(answer);
    }
}
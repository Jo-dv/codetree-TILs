import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int r, c;
    static String[][] board;

    public static void main(String[] args) throws IOException {
        // Please write your code here.
        st = new StringTokenizer(br.readLine());
        r = Integer.valueOf(st.nextToken());
        c = Integer.valueOf(st.nextToken());
        board = new String[r][c];
        int answer = 0;

        for(int i = 0; i < r; i++) {
            board[i] = br.readLine().split(" ");
            // System.out.println(Arrays.toString(board[i]));
        }
        Deque<String> s = new ArrayDeque<>();
        s.add("0,0,"+board[0][0]+",0");

        while(!s.isEmpty()) {
            String[] info = s.poll().split(",");
            int y = Integer.valueOf(info[0]);
            int x = Integer.valueOf(info[1]);
            String current = info[2];
            int step = Integer.valueOf(info[3]);

            if(y == r-1 && x == c-1 && step == 3) {
                answer++;
            }

            for(int i = y+1; i < r; i++) {
                for(int j = x+1; j < c; j++) {
                    if(!current.equals(board[i][j])) {
                        s.add(i+","+j+","+board[i][j]+","+(step+1));
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
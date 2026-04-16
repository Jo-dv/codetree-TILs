import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        // Please write your code here.
        int n = Integer.valueOf(br.readLine());
        int[][] grid = new int[n][n];
        int answer = 0;

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                grid[i][j] = Integer.valueOf(st.nextToken());
            }

            for(int j = 0; j < n-3 + 1; j++) {
                int temp = 0;
                for(int k = j; k < j + 3; k++) {
                    temp += grid[i][k];
                   
                }
                answer = Math.max(answer, temp);
            }
        }

        System.out.println(answer);
    }
}
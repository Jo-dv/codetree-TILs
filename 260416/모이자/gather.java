import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        // Please write your code here.
        int n = Integer.valueOf(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.valueOf(st.nextToken());
        }

        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++) {
            int temp = 0;
            int center = i;
            for(int j = i+1; j < n; j++) {
                temp += ((j - i) * arr[j]);
            }
            for(int j = i-1; j > -1; j--) {
                temp += ((i - j) * arr[j]);
            }

            answer = Math.min(answer, temp);
        }
        System.out.println(answer);
    }
}
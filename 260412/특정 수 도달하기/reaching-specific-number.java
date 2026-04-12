import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int sum = 0;
    static boolean flag = false;
    static double cnt = 0;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(st.nextToken());

            if (n >= 250) {
                flag = true;
                break;
            }

            sum += n;
            cnt++;
        }

        double avg;

        if (flag) {
            avg = sum / cnt;
        } else {
            avg = sum / 10.0;
        }

        avg = Math.round(avg * 10) / 10.0;
        sb.append(sum).append(" ").append(avg);
        System.out.println(sb);
    }
}
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int max_len = Integer.MIN_VALUE;
    static int min_len = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        for(int i = 0; i < 3; i++) {
            String data = br.readLine();
            max_len = Integer.max(max_len, data.length());
            min_len = Integer.min(min_len, data.length());
        }

        System.out.println(max_len - min_len);
    }
}
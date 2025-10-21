import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static String data1;
    static String data2;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        data1 = st.nextToken();
        data2 = st.nextToken();

        if (data1.length() > data2.length()) {
            System.out.println(data1 + " " + data1.length());
        } else if (data1.length() < data2.length()) {
            System.out.println(data2 + " " + data2.length());
        } else {
            System.out.println("same");
        }
    }
}
import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static String[] arr;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        arr = new String[n];
        for(int i = 0; i < n; i++)
            arr[i] = br.readLine();

        Arrays.sort(arr, (o1, o2) -> (o2 + o1).compareTo(o1 + o2));
        for(String i: arr)
            sb.append(i);

        System.out.println(sb);
        
    }
}
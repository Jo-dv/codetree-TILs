import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static String input;

    public static void main(String[] args) throws IOException {
        int size = 0;
        for(int i = 0; i < 2; i++) {
            input = br.readLine();
            size += input.length();
        }

        System.out.println(size);
    }
}
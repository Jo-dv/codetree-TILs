import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static boolean isValid(int i, int j, int k) {
        return i <= j && j <= k;
    }
    public static void main(String[] args) throws IOException {
        // Please write your code here.
        int n = Integer.valueOf(br.readLine());
        String[] input = br.readLine().split(" ");
        int answer = 0;

        for(int i = 0; i < input.length; i++) {
            for(int j = i+1; j < input.length; j++) {
                for(int k = j+1; k < input.length; k++) {
                    if(isValid(Integer.valueOf(input[i]), Integer.valueOf(input[j]), Integer.valueOf(input[k]))) {
                        answer++;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
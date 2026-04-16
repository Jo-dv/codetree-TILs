import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        // Please write your code here.
        String input = br.readLine();
        int answer = 0;

        for(int i = 0; i < input.length(); i++) {
            if(input.charAt(i) == '(') {
                for(int j = i; j < input.length(); j++) {
                    if(input.charAt(j) == ')') {
                        answer++;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
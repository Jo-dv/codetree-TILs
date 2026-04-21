import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int n = s.length();

        int[] right = new int[n];
        int count = 0;

        // 오른쪽에서 "))" 개수 누적
        for (int i = n - 2; i >= 0; i--) {
            if (s.charAt(i) == ')' && s.charAt(i + 1) == ')') {
                count++;
            }
            right[i] = count;
        }

        int answer = 0;

        // 왼쪽에서 "((" 찾기
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == '(' && s.charAt(i + 1) == '(') {
                answer += right[i + 2];
            }
        }

        System.out.println(answer);
    }
}
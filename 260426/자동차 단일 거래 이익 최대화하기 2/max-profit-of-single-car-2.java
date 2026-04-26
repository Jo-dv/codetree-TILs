import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] prices = new int[n];
        for(int i = 0; i < n; i++)
            prices[i] = sc.nextInt();
        // Please write your code here.
        int answer = 0;

        for(int i = 0; i < n - 1; i++) {
            int temp = prices[i];
            for(int j = i + 1; j < n; j++) {
                if(temp < prices[j]) {
                    answer = Math.max(answer, prices[j] - temp);
                }
            }
        }

        System.out.println(answer);
    }
}
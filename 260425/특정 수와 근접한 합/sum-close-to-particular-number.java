import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // Please write your code here.
        int answer = Integer.MAX_VALUE;

        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                int temp = 0;
                for(int k = 0; k < n; k++) {
                    if(k == i || k == j) {
                        continue;
                    }
                    temp += arr[k];
                }

                answer = Math.min(answer, Math.abs(temp - s));
            }
        }

        System.out.println(answer);
    }
}
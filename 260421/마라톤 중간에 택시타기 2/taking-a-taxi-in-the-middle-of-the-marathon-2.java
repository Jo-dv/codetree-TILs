import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        // Please write your code here.
        int answer = Integer.MAX_VALUE;
        for(int i=1; i < n-1; i++) {
            int prev = 0;
            int distance = 0;
            for(int j = 1; j < n; j++) {
                if(i == j) {
                    continue;
                }
                distance += Math.abs(x[prev] - x[j]) + Math.abs(y[prev] - y[j]);
                prev = j;
            }

            answer = Math.min(answer, distance);
        }

        System.out.println(answer);
    }
}
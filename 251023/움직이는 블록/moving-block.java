import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] blocks = new int[n];
        int average = 0;
        int answer = 0;
        for (int i = 0; i < n; i++) {
            blocks[i] = sc.nextInt();
            average += blocks[i];
        }
        // Please write your code here.
        average /= n;

        while(true) {
            int cnt = 0;
            int max_num = 0;
            int max_idx = -1;
            for(int i = 0; i < n; i++) {
                if(blocks[i] == average) {
                    cnt++;
                }
                if(max_num < blocks[i]) {
                    max_num = blocks[i];
                    max_idx = i;
                }
            }
            if(cnt == n) {
                System.out.println(answer);
                break;
            }

            for(int i = 0; i < n; i++) {
                if(blocks[i] < average) {
                    int diff = Integer.min(average - blocks[i], blocks[max_idx] - average);
                    blocks[max_idx] -= diff;
                    blocks[i] += diff;
                    answer += diff;
                    break;
                }
            }
        }
    }
}
import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        // Please write your code here.
        String bin = br.readLine();
        String[] bin_arr = new String[bin.length()];
        int answer = 0;
        for(int i = 0; i < bin.length(); i++) {
            bin_arr[i] = String.valueOf(bin.charAt(i));
        }

        boolean flag = false;
        for(int i = 0; i < bin.length(); i++) {
            if(bin_arr[i].equals("0")) {
                bin_arr[i] = "1";
                flag = true;
                break;
            }
        }

        int temp = 0;
        for(int i = 0; i < bin.length(); i++) {
            temp += Integer.valueOf(bin_arr[i]) * Math.pow(2, bin.length()-(i+1));
        }

        if(!flag) {
            temp -= 1;
        }

        System.out.println(temp);
    }
}
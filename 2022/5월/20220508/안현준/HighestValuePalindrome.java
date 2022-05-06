import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'highestValuePalindrome' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. INTEGER n
     *  3. INTEGER k
     */

    public static String highestValuePalindrome(String s, int n, int k) {
    // Write your code here
        int cnt = 0;
        char[] cs = s.toCharArray();
        char[] temp = cs.clone();
        boolean[] check = new boolean[n];

        for (int i = 0; i < n / 2; i++) {
            if (cs[i] == cs[n - 1 - i])
                continue;

            if (cnt >= k) {
                return "-1";
            }

            if (cs[i] > cs[n - 1 - i]) {
                temp[i] = cs[i];
                temp[n - 1 - i] = cs[i];
                check[n - 1 - i] = true;
            } else if (cs[i] < cs[n - 1 - i]) {
                temp[i] = cs[n - 1 - i];
                temp[n - 1 - i] = cs[n - 1 - i];
                check[i] = true;
            }
            cnt++;
        }
        for (int i = 0; i < (n+1) / 2; i++) {
            if(k-cnt > 1) {
                if (temp[i] != '9') {
                    temp[i]='9';
                    temp[n-1-i]='9';

                    if(!check[i]){
                        cnt++;
                        check[i]=true;
                    }
                    if(!check[n-1-i]){
                        cnt++;
                        check[n-1-i]=true;
                    }
                }
            }
            else if (k-cnt==1){
                if (temp[i] != '9') {
                    if(check[i] || check[n-1-i] || ((i==n-1-i) && !check[i])){
                        temp[i]='9';
                        temp[n-1-i]='9';

                        if(!check[i]){
                            cnt++;
                            check[i]=true;
                        }
                        if(!check[n-1-i]){
                            cnt++;
                            check[n-1-i]=true;
                        }
                    }
                }
            }
            else{
                break;
            }
        }
        return String.valueOf(temp);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int k = Integer.parseInt(firstMultipleInput[1]);

        String s = bufferedReader.readLine();

        String result = Result.highestValuePalindrome(s, n, k);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

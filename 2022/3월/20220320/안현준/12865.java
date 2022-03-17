import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N + 1][2];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N + 1][K + 1];
        for (int i = 1; i <= N; i++) {
            int w = arr[i][0];
            int v = arr[i][1];
            for (int j = 0; j <= K; j++) {
                if (j - w >= 0)
                    dp[i][j] = dp[i - 1][j - w] + v;
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);
            }
        }
        System.out.println(dp[N][K]);
    }
}

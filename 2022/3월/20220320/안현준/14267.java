import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

class Main {

    static ArrayList<Integer>[] superior;
    static int[] good;
    static int[] answer;

    static void dfs(int root) {
        answer[root] += good[root];
        if (superior[root] == null)
            return;
        for (int node : superior[root]) {
            answer[node] += answer[root];
            dfs(node);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        superior = new ArrayList[n + 1];
        good = new int[n + 1];
        answer = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        st.nextToken();
        for (int i = 2; i <= n; i++) {
            int s = Integer.parseInt(st.nextToken());
            if (superior[s] == null)
                superior[s] = new ArrayList<>();
            superior[s].add(i);
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            good[p] += w;
        }

        dfs(1);
        for (int i = 1; i <= n; i++) {
            bw.write(answer[i] + " ");
        }
        bw.close();
    }
}
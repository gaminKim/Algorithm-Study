import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static int[] parent;

    static boolean union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa != pb) {
            parent[pb] = pa;
            return true;
        }
        return false;
    }

    static int find(int a) {
        if (parent[a] == a)
            return a;

        return parent[a] = find(parent[a]);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<int[]> list = new ArrayList<>();
        parent = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            list.add(new int[]{v, a, b});
        }

        list.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        int answer = 0;
        int cnt = 0;
        for (int[] k : list) {
            if (union(k[1], k[2])) {
                answer += k[0];
                cnt++;
            }
            if (cnt == N - 2)
                break;
        }
        System.out.println(answer);
    }
}

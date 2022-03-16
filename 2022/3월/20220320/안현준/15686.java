import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static ArrayList<int[]> chicken;
    static ArrayList<int[]> house;
    static ArrayList<int[]> select;
    static int[][] arr;
    static int N;
    static int M;
    static int answer = 100000;

    static int calcDis() {
        int sum = 0;
        for (int[] h : house) {
            int dist = 1000000;
            for (int[] pos : select) {
                dist = Math.min(dist, Math.abs(pos[0] - h[0]) + Math.abs(pos[1] - h[1]));
            }
            sum += dist;
        }
        return sum;
    }

    static void dfs(int idx, int cnt) {
        if (cnt == M) {
            answer = Math.min(answer, calcDis());
            return;
        }
        if (idx == chicken.size()) {
            return;
        }

        int x = chicken.get(idx)[0];
        int y = chicken.get(idx)[1];

        select.add(new int[]{x, y});
        dfs(idx + 1, cnt + 1);
        select.remove(select.size() - 1);
        dfs(idx + 1, cnt);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        chicken = new ArrayList<>();
        house = new ArrayList<>();
        select = new ArrayList<>();
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 2)
                    chicken.add(new int[]{i, j});
                if (arr[i][j] == 1)
                    house.add(new int[]{i, j});
            }
        }

        dfs(0, 0);
        System.out.println(answer);
    }
}

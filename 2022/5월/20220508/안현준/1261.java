import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;

class Main {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int N, M;

    static boolean isRange(int x, int y) {
        return x > 0 && y > 0 && x <= N && y <= M;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");

        int[][] arr = new int[101][101];
        int[][] visit = new int[101][101];

        M = Integer.parseInt(s[0]);
        N = Integer.parseInt(s[1]);

        for (int i = 1; i <= N; i++) {
            String k = br.readLine();
            for (int j = 1; j <= M; j++) {
                arr[i][j] = k.charAt(j - 1) - '0';
            }
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        pq.offer(new int[]{0, 1, 1});
        visit[1][1] = 1;
        while (!pq.isEmpty()) {
            int[] f = pq.poll();
            int x = f[1];
            int y = f[2];
            int cnt = f[0];

            if (f[1] == N && f[2] == M) {
                System.out.println(cnt);
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (isRange(nx, ny) && visit[nx][ny] == 0) {
                    if (arr[nx][ny] == 1)
                        pq.offer(new int[]{cnt + 1, nx, ny});
                    else
                        pq.offer(new int[]{cnt, nx, ny});
                    visit[nx][ny] = 1;
                }
            }
        }
    }
}
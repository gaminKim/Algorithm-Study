import java.io.*;
import java.util.*;

class Main {
    static int N, M, K;
    static int[][] arr, sticker;
    static int R, C;

    static boolean putSticker(int x, int y) {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (sticker[i][j] == 1 && arr[x + i][y + j] == 1)
                    return false;
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (sticker[i][j] == 1)
                    arr[x + i][y + j] = 1;
            }
        }
        return true;
    }

    static void rotateSticker() {
        int t = R;
        R = C;
        C = t;

        int[][] temp = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                temp[i][j] = sticker[C - j - 1][i];
            }
        }
        sticker = temp;
    }

    static void printArr() {
        System.out.println("print Arr!");
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                System.out.print(sticker[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        for (int x = 0; x < K; x++) {
            st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            sticker = new int[R][C];
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    sticker[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            int dir = 0;
            put:
            while (dir < 4) {
                for (int i = 0; i <= N - R; i++) {
                    for (int j = 0; j <= M - C; j++) {
                        if (putSticker(i, j))
                            break put;
                    }
                }

                rotateSticker();
                dir++;
            }
        }

        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 1)
                    answer++;
            }
        }
        System.out.println(answer);
    }
}
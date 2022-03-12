import java.io.*;

class Main {

    static char[][] star = {
            {' ', ' ', '*', ' ', ' '},
            {' ', '*', ' ', '*', ' '},
            {'*', '*', '*', '*', '*'}};
    static char[][] arr;

    static void func(int len, int r, int c) {
        if (len == 3) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 5; j++) {
                    arr[r + i][c + j] = star[i][j];
                }
            }
            return;
        }
        func(len / 2, r, c + len / 2);
        func(len / 2, r + len / 2, c);
        func(len / 2, r + len / 2, c + len);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        arr = new char[N][2 * N - 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N * 2 - 1; j++) {
                arr[i][j] = ' ';
            }
        }

        func(N, 0, 0);
        for (int i = 0; i < N; i++) {
            bw.write(arr[i]);
            bw.write('\n');
        }
        bw.close();
    }
}
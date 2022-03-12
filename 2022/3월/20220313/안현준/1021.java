import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            list.add(i);
        }

        st = new StringTokenizer(br.readLine());
        int answer = 0;
        for (int i = 0; i < m; i++) {
            int now = Integer.parseInt(st.nextToken());
            boolean isFront = false;

            int cnt = 0;
            for (int l : list) {
                if (l == now) {
                    isFront = true;
                    break;
                }
                cnt++;
                if (cnt > list.size() / 2)
                    break;
            }
            if (isFront) {
                while (list.peekFirst() != now) {
                    list.addLast(list.pollFirst());
                    answer++;
                }
            } else {
                while (list.peekFirst() != now) {
                    list.addFirst(list.pollLast());
                    answer++;
                }
            }
            list.pollFirst();
        }
        System.out.println(answer);
    }
}
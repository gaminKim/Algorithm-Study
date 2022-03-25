import java.io.*;
import java.util.*;

class Main {

    static int[] dist;
    static ArrayList<int[]>[] list;
    static int start, end, cost;
    static int[] pre;

    static void dijkstra() {
        dist[start] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.offer(new int[]{0, start});
        pq.offer(new int[]{3, start});

        while (!pq.isEmpty()) {
            int node = pq.peek()[1];
            int w = pq.peek()[0];
            pq.poll();

            if (dist[node] < w)
                continue;
            for (int[] next : list[node]) {
                int n0 = next[0];
                int n1 = next[1];

                if (dist[n0] > w + n1) {
                    dist[n0] = w + n1;
                    pre[n0] = node;
                    pq.offer(new int[]{dist[n0], n0});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        list = new ArrayList[n + 1];
        dist = new int[n + 1];
        pre = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            list[i] = new ArrayList<>();
            dist[i] = 1000000000;
        }

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            cost = Integer.parseInt(st.nextToken());

            list[start].add(new int[]{end, cost});
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        dijkstra();
        System.out.println(dist[end]);

        Stack<Integer> s = new Stack<>();
        s.push(end);
        while (s.peek() != start) {
            end = pre[end];
            s.push(end);
        }

        System.out.println(s.size());
        StringBuilder answer = new StringBuilder();
        while (!s.isEmpty()) {
            answer.append(s.pop());
            answer.append(" ");
        }
        System.out.println(answer);
    }
}
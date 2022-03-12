import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());

            if(num==0){
                if(pq.isEmpty()) {
                    bw.write(Integer.toString(0));
                }
                else {
                    bw.write(Integer.toString(pq.poll()));
                }
                bw.write("\n");
            }
            else{
                pq.offer(num);
            }
        }
        bw.close();
    }
}
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        int x = Integer.parseInt(s[0]);
        int y = Integer.parseInt(s[1]);

        double a = 0;
        double b = 0;

        double d = Math.sqrt(x * x + y * y);
        a = x / d;
        b = y / d;
        System.out.println(String.format("%.12f  %.12f", a, b));
    }
}
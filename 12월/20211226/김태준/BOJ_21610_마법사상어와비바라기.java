package com.company.algorithm_solving.study.week4;

import java.util.*;

public class test2 {
    // 마법사 상어와 비바라기

    static int n;
    static int m;
    static int A[ ][ ];
    static int dx[ ] = {0,-1,-1,-1,0,1,1,1};
    static int dy[ ] = {-1,-1,0,1,1,1,0,-1};
    static Move moves[ ];
    static Map<String, Boolean> cloudPosMap = new HashMap<>();
    static Queue<Point> nowQ = new LinkedList<>();
    static Queue<Point> nextQ = new LinkedList<>();

    public static void main(String args[ ]) {
        processInputData();
        doProcess();
        processOutputData();
    }

    public static void processInputData( ) {
        Scanner in=new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();

        A = new int[n][n];

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                A[i][j] = in.nextInt();
            }
        }

        moves = new Move[m];
        for(int i=0; i<m; i++) {
            int direction = in.nextInt() - 1;
            int moveDistance = in.nextInt();
            moves[i] = new Move(direction, moveDistance);
        }

        //최고 구름위치 세팅
        nowQ.add(new Point(n-1, 0));
        nowQ.add(new Point(n-1, 1));
        nowQ.add(new Point(n-2, 0));
        nowQ.add(new Point(n-2, 1));
    }

    public static void doProcess( ) {

        for(int i=0; i<moves.length; i++) {
            moveAndIncreaseWater(moves[i]);
            doMagic();
            makeCloud();
        }
    }

    // 1.구름을 움직인다.
    // 2.구름이 있는 칸에 있는 바구니의 물의양이 1증가
    // 3. 구름이 사라진다. -> visit을 -1로 변경
    public static void moveAndIncreaseWater(Move move) {

        while(!nowQ.isEmpty()) {

            Point p = nowQ.poll();
            int xp = p.x;
            int yp = p.y;

            for(int j=0; j<move.moveDistance; j++) {
                int xp2 = xp + dx[move.direction];
                int yp2 = yp + dy[move.direction];

                if(xp2 < 0) xp2 = n-1;
                if(yp2 < 0) yp2 = n-1;
                if(n-1 < xp2) xp2 = 0;
                if(n-1 < yp2) yp2 = 0;

                xp = xp2;
                yp = yp2;
            }
            nextQ.add(new Point(xp, yp));
            cloudPosMap.put(xp + ":" + yp, true);
            A[xp][yp] += 1;
        }
    }

    // 4. 물복사버그 마법을 시전한다.
    public static void doMagic( ) {

        while(!nextQ.isEmpty()) {

            Point p = nextQ.poll();
            int xp = p.x;
            int yp = p.y;

            int waterBacketCount = 0;
            for(int i=0; i<8; i++) {

                if(i == 0 || i == 2 || i == 4 || i == 6) continue;
                int xp2 = xp + dx[i];
                int yp2 = yp + dy[i];

                if(xp2 < 0 || n-1 < xp2) continue;
                if(yp2 < 0 || n-1 < yp2) continue;

                if(A[xp2][yp2] > 0) waterBacketCount++;
            }

            A[xp][yp] += waterBacketCount;
        }
    }

    // 5. 물의 양이 2이상인 칸에 구름을 만든다.
    public static void makeCloud( ) {

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {

                boolean isPrevCloud = cloudPosMap.containsKey(i+":"+j);
                if(isPrevCloud) continue;  // 전 단계에 구름이였던 곳은 제외

                if(A[i][j] >= 2) {
                    A[i][j] -= 2;
                    nowQ.add(new Point(i, j));
                }
            }
        }

        cloudPosMap.clear();
    }

    public static void processOutputData( ) {

        int res = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                res += A[i][j];
            }
        }

        System.out.println(res);
    }

    public static class Move {
        int direction;
        int moveDistance;

        public Move(int direction, int moveDistance) {
            this.direction = direction;
            this.moveDistance = moveDistance;
        }
    }

    public static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}


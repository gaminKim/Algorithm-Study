package com.company.algorithm_solving.study.week5;

import com.company.algorithm_solving.study.week4.test2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * 플로이드 워셜 알고리즘
 * n개의 노드에서 n개의 노드로 가능 최소비용(최단거리)를 구할때 사용 (1->n 일때 edge 양수이면 다익스트라, 음수이면 벨만포드)
  즉, 플로이드는 다익스트라 n번 돌린거라고 보면된다..? (1->1, 1->2 ...1->n 최소비용이므로..?)
 * 시간복잡도 : o(n^3)
 * 설명 : i -> j로 가는게 작은 비용인가? i -> k -> j로 가는게 작은 비용인가?
 *           for (int k = 1; k <= n; k++) { // 거쳐가는 도시
 *             for (int i = 1; i <= n; i++) { // 출발 도시
 *                 for (int j = 1; j <= n; j++) { // 도착 도시
 *
 *                     if (i == j || k == i || k == j) continue;
 *                     if(moveCost[i][k] == 0 || moveCost[k][j] == 0) continue; // 갈 수 없는길
 *                     moveCost[i][j] = (moveCost[i][j] == 0) ? moveCost[i][k] + moveCost[k][j] : Math.min(moveCost[i][j], moveCost[i][k] + moveCost[k][j]); // i->j와 i->k->j 최소값 선택
 *                 }
 *             }
 *         }
 */
public class test1 {

    static int n;
    static int m;
    static int moveCost[ ][ ]; // start->end로 가는 최소 cost

    public static void main(String args[]) {
        processInputData();
        doProcess();
        processOutputData();
    }

    public static void processInputData() {
        Scanner in = new Scanner(System.in);
        n = in.nextInt(); // 도시 수
        m = in.nextInt(); // 버스 수

        // 초기화
        moveCost = new int[n+1][n+1];
        for(int i=1; i<=n; i++) {
            Arrays.fill(moveCost[i], 0);
        }

        for (int i = 0; i < m; i++) {
            int startCity = in.nextInt();
            int endCity = in.nextInt();
            int cost = in.nextInt();

            //같은 경로가 여러번 들어올 수 있음(최소값 선택)
            moveCost[startCity][endCity] = (moveCost[startCity][endCity] == 0) ? cost : Math.min(moveCost[startCity][endCity], cost);
        }
    }

    public static void doProcess () {

        for (int k = 1; k <= n; k++) { // 거쳐가는 도시
            for (int i = 1; i <= n; i++) { // 출발 도시
                for (int j = 1; j <= n; j++) { // 도착 도시

                    if (i == j || k == i || k == j) continue;
                    if(moveCost[i][k] == 0 || moveCost[k][j] == 0) continue; // 갈 수 없는길
                    moveCost[i][j] = (moveCost[i][j] == 0) ? moveCost[i][k] + moveCost[k][j] : Math.min(moveCost[i][j], moveCost[i][k] + moveCost[k][j]);
                }
            }
        }
    }

    public static void processOutputData () {

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                System.out.print(moveCost[i][j] + " ");
            }
            System.out.println();
        }
    }
}


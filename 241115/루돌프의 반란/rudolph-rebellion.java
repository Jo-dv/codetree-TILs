import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m, p, c, d;
    static int ry, rx;
    static int [][] map;  // 디버깅
    static Santa[] santas;
    static boolean[] alive;
    static int[] stun;
    static int[] scores;

    static class Santa {
        int y, x, num;
        double distance;

        public Santa(int y, int x) {
            this.y = y;
            this.x = x;
        }

        public Santa(int y, int x, int num) {
            this.y = y;
            this.x = x;
            this.num = num;
        }

        public Santa(int y, int x, int num, double distance) {
            this.y = y;
            this.x = x;
            this.num = num;
            this.distance = distance;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        ry = Integer.parseInt(st.nextToken());
        rx = Integer.parseInt(st.nextToken());
        santas = new Santa[p + 1];  // sy, sx
        for(int i = 1; i <= p; i++) {
            st = new StringTokenizer(br.readLine());
            int sNum, sy, sx;
            sNum = Integer.parseInt(st.nextToken());
            sy = Integer.parseInt(st.nextToken());
            sx = Integer.parseInt(st.nextToken());
            santas[sNum] = new Santa(sy, sx);
        }

        map = new int[n + 2][n + 2];
        alive = new boolean[p + 1];
        Arrays.fill(alive, true);
        stun = new int[p + 1];
        scores = new int[p + 1];

        solve();
    }

    static void initMap() {  //  디버깅, 산타 및 루돌프 위치 표기
        for(int i = 1; i <= p; i++) {
            Santa s = santas[i];
            map[s.y][s.x] = i;
        }
        map[ry][rx] = -1;
    }

    static void moveRudolph(int turn) {
        Santa santa = findSanta();
        int dy = 0, dx = 0;

        if(ry < santa.y)
            dy = 1;
        else if(ry > santa.y)
            dy = -1;

        if(rx < santa.x)
            dx = 1;
        else if(rx > santa.x)
            dx = -1;


        map[ry][rx] = 0;
        map[ry + dy][rx + dx] = -1;
        ry += dy;
        rx += dx;
        if(ry == santa.y && rx == santa.x) {
            pushSanta(santa, dy, dx, c);
            scores[santa.num] += c;
            stun[santa.num] = turn + 2;
        }
    }

    static Santa findSanta() {
        ArrayList<Santa> distances = new ArrayList<>();
        double minDistance = 2 * n * n;

        for(int i = 1; i <= p; i++) {
            if(!alive[i])
                continue;
            double distance = Math.pow((ry - santas[i].y), 2) + Math.pow((rx - santas[i].x), 2);
            if(distance <= minDistance) { // 동일한 거리가 있을 수도 있음
                minDistance = distance;
                distances.add(new Santa(santas[i].y, santas[i].x, i, distance));
            }
        }

        Collections.sort(distances, 
        Comparator.comparingDouble((Santa o) -> o.distance)
        .thenComparingInt((o) -> -o.y)
        .thenComparingInt((o) -> -o.x));
        return distances.get(0);
    }

    static void moveSanta(int turn) {
        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

        for(int i = 1; i <= p; i++) {
            if(!alive[i] || stun[i] > turn)
                continue;
            double minDistance = Math.pow((ry - santas[i].y), 2) + Math.pow((rx - santas[i].x), 2);
            int santa = 0, my = 0, mx = 0, dy = 0, dx = 0;
            for(int[] d: directions) {
                my = santas[i].y + d[0];
                mx = santas[i].x + d[1];
                double distance = Math.pow((ry - my), 2) + Math.pow((rx - mx), 2);
                if(1 <= my && my <= n && 1 <= mx && mx <= n && map[my][mx] <= 0 && distance < minDistance) {
                    minDistance = distance;
                    santa = i;
                    dy = d[0];
                    dx = d[1];
                }
            }

            if(santa != 0) {
                my = santas[santa].y + dy;
                mx = santas[santa].x + dx;
                map[santas[santa].y][santas[santa].x] = 0;
                if(map[my][mx] == 0) {
                    map[my][mx] = santa;
                    santas[santa] = new Santa(my, mx);
                } else {
                    pushSanta(new Santa(my, mx, santa), -dy, -dx, d);
                    scores[santa] += d;
                    stun[santa] = turn + 2;
                }
            }
        }
    }

    static void pushSanta(Santa santa, int dy, int dx, int power) {
        ArrayDeque<Santa> dq = new ArrayDeque<>();
        dq.add(santa);

        while(!dq.isEmpty()) {
            Santa current = dq.pollFirst();
            int my = current.y + (dy * power), mx = current.x + (dx * power);
            if(1 <= my && my <= n && 1 <= mx && mx <= n) {
                if(map[my][mx] != 0) {  // 다른 산타가 있는 경우
                	power = 1;  // 한 칸씩 밀어야 함
                    dq.add(new Santa(my, mx, map[my][mx]));
                }
	            map[my][mx] = current.num;
	            santas[current.num] = new Santa(my, mx);  //  산타 위치 정보 갱신
            }
            else {
                alive[current.num] = false;
                return;
            }
        }
    }

    static void solve() {
        initMap();

        for(int turn = 1; turn <= m; turn++) {
            int aliveSanta = p;
            Game:
            for(int i = 1; i <= p; i++) {
                aliveSanta -= alive[i] ? 1 : 0;
                if(aliveSanta == 0)
                    break Game;
            }
            moveRudolph(turn);
            moveSanta(turn);
            for(int i = 1; i <= p; i++) {
                if(alive[i] == true)
                	scores[i] += 1;
            }
        }
        for(int i = 1; i <= p; i++)
        	System.out.print(scores[i] + " ");
    }
}
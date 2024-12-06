import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] map = new int[4][4];
    static int m, t, r, c, answer = 0;
    static Pos packman;
    static HashMap<Integer, ArrayList<Monster>> monsters = new HashMap<>();
    static ArrayList<Monster> eggs = new ArrayList<>();
    static Queue<Corpse> corpses = new LinkedList<>();
    static int[][] grave = new int[4][4];
    static int[][] monDir = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
    static int[][] packDir = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    static List<int[][]> packmanRoutes = new ArrayList<>();

    static class Pos {
        int y, x;

        Pos(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static class Monster extends Pos {
        int d;

        Monster(int y, int x, int d) {
            super(y, x);
            this.d = d;
        }
    }

    static class Corpse extends Pos {
        int expireTurn;

        Corpse(int y, int x, int expireTurn) {
            super(y, x);
            this.expireTurn = expireTurn;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken()) - 1;
        c = Integer.parseInt(st.nextToken()) - 1;

        packman = new Pos(r, c);

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                monsters.put(i * 4 + j, new ArrayList<>());
            }
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int mr = Integer.parseInt(st.nextToken()) - 1;
            int mc = Integer.parseInt(st.nextToken()) - 1;
            int md = Integer.parseInt(st.nextToken()) - 1;
            monsters.get(mr * 4 + mc).add(new Monster(mr, mc, md));
            map[mr][mc]++;
        }

        generatePackmanRoutes(new int[3][2], 0);

        for (int turn = 1; turn <= t; turn++) {
            copyEggs();
            moveMonsters();
            movePackman(turn);
            removeExpiredCorpses(turn);
            hatchEggs();
        }

        for (int i = 0; i < 16; i++) {
            answer += monsters.get(i).size();
        }

        System.out.println(answer);
    }

    static boolean isValid(int y, int x) {
        return 0 <= y && y < 4 && 0 <= x && x < 4;
    }

    static void copyEggs() {
        for (int i = 0; i < 16; i++) {
            for (Monster monster : monsters.get(i)) {
                eggs.add(new Monster(monster.y, monster.x, monster.d));
            }
        }
    }

    static void moveMonsters() {
        ArrayList<Monster> nextMonsters = new ArrayList<>();

        for (int i = 0; i < 16; i++) {
            ArrayList<Monster> currentList = monsters.get(i);
            for (Monster monster : currentList) {
                boolean moved = false;
                for (int j = 0; j < 8; j++) {
                    int nd = (monster.d + j) % 8;
                    int ny = monster.y + monDir[nd][0];
                    int nx = monster.x + monDir[nd][1];
                    if (isValid(ny, nx) && grave[ny][nx] == 0 && (packman.y != ny || packman.x != nx)) {
                        monster.y = ny;
                        monster.x = nx;
                        monster.d = nd;
                        nextMonsters.add(monster);
                        moved = true;
                        break;
                    }
                }
                if (!moved) nextMonsters.add(monster);
            }
            currentList.clear();
        }

        for (Monster monster : nextMonsters) {
            monsters.get(monster.y * 4 + monster.x).add(monster);
        }
    }

    static void movePackman(int turn) {
        int maxCatch = 0;
        int[][] bestRoute = null;

        for (int[][] route : packmanRoutes) {
            HashSet<Integer> visited = new HashSet<>();
            int count = 0;
            int y = packman.y, x = packman.x;

            for (int[] move : route) {
                y += move[0];
                x += move[1];
                if (isValid(y, x) && visited.add(y * 4 + x)) {
                    count += monsters.get(y * 4 + x).size();
                }
            }

            if (count > maxCatch) {
                maxCatch = count;
                bestRoute = route;
            }
        }

        if (bestRoute != null) {
            for (int[] move : bestRoute) {
                packman.y += move[0];
                packman.x += move[1];
                int idx = packman.y * 4 + packman.x;
                ArrayList<Monster> caught = monsters.get(idx);
                if (caught != null && !caught.isEmpty()) {
                    map[packman.y][packman.x] = 0;
                    for (Monster monster : caught) {
                        corpses.add(new Corpse(monster.y, monster.x, turn + 2));
                        grave[monster.y][monster.x]++;
                    }
                    caught.clear();
                }
            }
        }
    }

    static void removeExpiredCorpses(int turn) {
        while (!corpses.isEmpty() && corpses.peek().expireTurn <= turn) {
            Corpse corpse = corpses.poll();
            grave[corpse.y][corpse.x]--;
        }
    }

    static void hatchEggs() {
        for (Monster egg : eggs) {
            monsters.get(egg.y * 4 + egg.x).add(egg);
        }
        eggs.clear();
    }

    static void generatePackmanRoutes(int[][] route, int depth) {
        if (depth == 3) {
            packmanRoutes.add(route.clone());
            return;
        }
        for (int[] dir : packDir) {
            route[depth] = dir;
            generatePackmanRoutes(route, depth + 1);
        }
    }
}

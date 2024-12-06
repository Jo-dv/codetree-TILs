import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] map = new int[4][4];
	static int m, t;
	static int r, c;
	static int mr, mc, md;
	static Pos packman;
	static HashMap<Integer, ArrayList<Monster>> monsters = new HashMap<>();
	static List<Monster> eggs = new LinkedList<>();
	static List<Corpse> corpses = new ArrayList<>();
	static int[][] grave = new int[4][4];
	static int[][] mon_dir = { { -1, 0 }, { -1, -1 }, { 0, -1 }, { 1, -1 }, { 1, 0 }, { 1, 1 }, { 0, 1 }, { -1, 1 } };
	static int[][] dir = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 } };
	static ArrayList<int[][]> pack_dir = new ArrayList<>();
	static int answer = 0;

	static class Pos {
		int y, x;

		Pos(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}

	static class Monster extends Pos {
		int d;

		public Monster(int y, int x, int d) {
			super(y, x);
			this.d = d;
		}
	}

	static class Corpse extends Pos {
		int t;

		public Corpse(int y, int x, int t) {
			super(y, x);
			this.t = t;
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
			mr = Integer.parseInt(st.nextToken()) - 1;
			mc = Integer.parseInt(st.nextToken()) - 1;
			md = Integer.parseInt(st.nextToken()) - 1;
			monsters.get(mr * 4 + mc).add(new Monster(mr, mc, md));
			map[mr][mc]++;
		}

		solve();
	}

	static boolean is_valid(int y, int x) {
		return 0 <= y && y < 4 && 0 <= x && x < 4;
	}

	static void produce_egg() {
		for (int i = 0; i < 16; i++) {
			for (Monster monster : monsters.get(i)) {
				eggs.add(new Monster(monster.y, monster.x, monster.d)); // 몬스터 객체 그대로 넣으면 메모리 복사됨
			}
		}
	}

	static void move_monster() {
		ArrayList<Monster> wait_list = new ArrayList<>();

		for (int i = 0; i < 16; i++) {
			int size = monsters.get(i).size() - 1;
			for (int j = size; j >= 0; j--) {
				Monster monster = monsters.get(i).get(j);
				for (int l = 0; l < 8; l++) { // 방향
					int md = (monster.d + l) % 8;
					int my = monster.y + mon_dir[md][0];
					int mx = monster.x + mon_dir[md][1];
					if (is_valid(my, mx) && grave[my][mx] == 0 && !(packman.y == my && packman.x == mx)) {
						map[monster.y][monster.x]--;
						monsters.get(i).remove(j);
						monster.y = my;
						monster.x = mx;
						monster.d = md;
						wait_list.add(monster);
						break;
					}
				}
			}

		}

		for (Monster monster : wait_list) {
			monsters.get(monster.y * 4 + monster.x).add(monster);
			map[monster.y][monster.x]++;
		}
	}

	static void move_packman(int turn) {
		int max_cnt = 0; // 잡은 몬스터의 수
		int[][] final_pos = null; // 최종 위치

		for (int[][] route : pack_dir) {
			HashSet<Integer> visited = new HashSet<>();
			int y = packman.y, x = packman.x;
			int cnt = 0;
			boolean flag = true;

			for (int[] step : route) {
				y += step[0];
				x += step[1];
				if (!is_valid(y, x)) {
					flag = false;
					break;
				}
				if (!visited.contains(y * 4 + x)) {
					visited.add(y * 4 + x);
					cnt += monsters.get(y * 4 + x).size();
				}
			}

			if (flag && max_cnt < cnt) {
				max_cnt = cnt;
				final_pos = route;
			}
		}

		for (int[] pos : final_pos) {
			packman.y += pos[0];
			packman.x += pos[1];
			ArrayList<Monster> caught = monsters.get(packman.y * 4 + packman.x);
			if (!caught.isEmpty()) {
				map[packman.y][packman.x] = 0;
				for (Monster monster : caught) {
					corpses.add(new Corpse(monster.y, monster.x, turn + 2));
					grave[monster.y][monster.x]++;
				}
				caught.clear();
			}
		}
	}

	static void remove_corpse(int turn) {
		int size = corpses.size() - 1;
		for (int i = size; i >= 0; i--) {
			Corpse corpse = corpses.get(i);
			if (corpse.t <= turn) {
				corpses.remove(i);
				grave[corpse.y][corpse.x]--;
			}
		}
	}

	static void hatch_egg() {
		int size = eggs.size() - 1;
		for (int i = size; i >= 0; i--) {
			Monster monster = eggs.remove(i);
			monsters.get(monster.y * 4 + monster.x).add(monster);
			map[monster.y][monster.x]++;
		}
	}

	static void find_dir(int depth, int[][] route) {
		if (depth == 3) {
			pack_dir.add(route.clone());
			return;
		}
		for (int i = 0; i < 4; i++) {
			route[depth] = dir[i];
			find_dir(depth + 1, route);
		}
	}

	static void solve() {
		find_dir(0, new int[3][2]);

		for (int turn = 1; turn <= t; turn++) {
			produce_egg();
			move_monster();
			move_packman(turn);
			remove_corpse(turn);
			hatch_egg();
		}

		for (int i = 0; i < 16; i++) {
			answer += monsters.get(i).size();
		}

		System.out.println(answer);
	}
}

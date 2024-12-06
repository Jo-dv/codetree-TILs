import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] map = new int[4][4];
	static int m, t;
	static int r, c;
	static int mr, mc, md;
	static Pos packman;
	static HashMap<String, ArrayList<Monster>> monsters = new HashMap<>();
	static ArrayList<Monster> eggs = new ArrayList<>();
	static ArrayList<Corpse> corpses = new ArrayList<>();
	static int[][] grave = new int[4][4];
	static int[][] mon_dir = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
	static int[][] dir = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
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
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				monsters.put(i + ", " + j, new ArrayList<>());
			}
		}
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			mr = Integer.parseInt(st.nextToken()) - 1;
			mc = Integer.parseInt(st.nextToken()) - 1;
			md = Integer.parseInt(st.nextToken()) - 1;
			monsters.get(mr + ", " + mc).add(new Monster(mr, mc, md));
		}
		
		solve();
	}
	
	static boolean is_valid(int y, int x) {
		return 0 <= y && y < 4 && 0 <= x && x < 4;
	}
	
	static void produce_egg() {
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				for(Monster monster: monsters.get(i + ", " + j)) {
					eggs.add(new Monster(monster.y, monster.x, monster.d));  // 몬스터 객체 그대로 넣으면 메모리 복사됨
					map[i][j] += 1;
				}
			}
		}
	}
	
	static void move_monster() {
		ArrayList<Monster> wait_list = new ArrayList<>();
		
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int size = monsters.get(i + ", " + j).size() - 1;
				for(int k = size; k >= 0; k--) {
					for(int l = 0; l < 8; l++) {  // 방향
						Monster monster = monsters.get(i + ", " + j).get(k);
						int my = monster.y + mon_dir[monster.d][0];
						int mx = monster.x + mon_dir[monster.d][1];
						if(is_valid(my, mx) && grave[my][mx] == 0 && !(packman.y == my && packman.x == mx)) {
							map[monster.y][monster.x] -= 1;
							monsters.get(i + ", " + j).remove(k);
							monster.y = my;
							monster.x = mx;
							wait_list.add(monster);
							break;
						} else {
							monster.d = (monster.d + 1 + 8) % 8;  // 반시계라서 왼쪽인 줄 알았는데 아니었음
						}
					}
				}
			}
		}
		
		for(Monster monster: wait_list) {
			monsters.get(monster.y + ", " + monster.x).add(monster);
			map[monster.y][monster.x] += 1;
		}
	}
	
	static void move_packman(int turn) {
		int cnt = 0;  // 잡은 몬스터의 수
		int[][] final_pos = new int[3][2];  // 최종 위치
		
		for (int[][] d : pack_dir) {
		    int my1 = packman.y + d[0][0];
		    int mx1 = packman.x + d[0][1];
		    int my2 = my1 + d[1][0];
		    int mx2 = mx1 + d[1][1];
		    int my3 = my2 + d[2][0];
		    int mx3 = mx2 + d[2][1];

		    if (is_valid(my1, mx1) && is_valid(my2, mx2) && is_valid(my3, mx3)) {
		        if ((my1 != my2 || mx1 != mx2) && (my1 != my3 || mx1 != mx3) && (my2 != my3 || mx2 != mx3)) {
		            if (map[my1][mx1] + map[my2][mx2] + map[my3][mx3] > cnt) {
		                cnt = map[my1][mx1] + map[my2][mx2] + map[my3][mx3];
		                final_pos[0] = new int[]{my1, mx1};
		                final_pos[1] = new int[]{my2, mx2};
		                final_pos[2] = new int[]{my3, mx3};
		            }
		        }
		    }
		}
		
		for(int[] pos: final_pos) {	
			int y = pos[0], x = pos[1];
			if(map[y][x] > 0) {
				int size = monsters.get(y + ", " + x).size();
				monsters.get(y + ", " + x).clear();
				map[y][x] = 0;
				for(int i = 0; i < size; i++) {
					corpses.add(new Corpse(y, x, turn + 2));
					grave[y][x] += 1;
				}
			}
		}
		packman.y = final_pos[2][0];
		packman.x = final_pos[2][1];
	}
	
	static void remove_corpse(int turn) {
		int size = corpses.size() - 1;
		for(int i = size; i >= 0; i--) {
			Corpse corpse = corpses.get(i);
			if(corpse.t <= turn) {
				corpses.remove(i);
				grave[corpse.y][corpse.x] -= 1;
			}
		}
	}
	
	static void hatch_egg() {
		int size = eggs.size() - 1;
		for(int i = size; i >= 0; i--) {
			Monster monster = eggs.remove(i);
			monsters.get(monster.y + ", " + monster.x).add(monster);
		}
	}
	
	static void find_dir(int depth, int[][] route) {
		if(depth == 3) {
			pack_dir.add(route.clone());
			return;
		}
		for(int i = 0; i < 4; i++) {
			route[depth] = dir[i];
			find_dir(depth + 1, route);
		}
	}
	
	static void solve() {
		find_dir(0, new int[3][2]);
			
		for(int turn = 1; turn <= t; turn++) {
			produce_egg();
			move_monster();
			move_packman(turn);
			remove_corpse(turn);
			hatch_egg();
		}
		
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				answer += monsters.get(i + ", " + j).size();
			}
		}
		
		System.out.println(answer);
	}
}

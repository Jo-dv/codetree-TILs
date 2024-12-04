import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, h, k;
	static int[][] map;
	static int y, x;
	static int d;
	static int[][] directions = {{-1 , 0}, {0, 1}, {1, 0}, {0, -1}};  // 상 우 하 좌
	static Tagger tagger;
	static HashSet<String> trees = new HashSet<>();
	static ArrayList<Player> runners = new ArrayList<>();
	static int answer = 0;
	
	static class Player {
		int y, x, d;
		
		Player(int y, int x, int d) {
			this.y = y;
			this.x = x;
			this.d = d;
		}
	}
	
	static class Tagger extends Player {
		int max_distance, distance, cnt, val;

		public Tagger(int y, int x, int d, int max_distance, int distance, int cnt, int val) {
			super(y, x, d);
			this.max_distance = max_distance;
			this.distance = distance;
			this.cnt = cnt;
			this.val = val;
		}

		@Override
		public String toString() {
			return "Tagger [y=" + y + ", x=" + x + ", d=" + d + ", max_distance=" + max_distance + ", distance=" + distance + ", cnt=" + cnt
					+ ", val=" + val + "]";
		}
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		map = new int[n][n];
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			y = Integer.parseInt(st.nextToken()) - 1;
			x = Integer.parseInt(st.nextToken()) - 1;
			d = Integer.parseInt(st.nextToken()) - 1;
			runners.add(new Player(y, x, d == 0 ? 1 : 2));
			map[y][x] = i + 1;
		}
		
		for(int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			y = Integer.parseInt(st.nextToken()) - 1;
			x = Integer.parseInt(st.nextToken()) - 1;
			trees.add(y + ", " + x);
		}
		tagger = new Tagger(n / 2, n / 2, 0, 1, 0, 0, 1);

		
		solve();
	}
	
	static void move_tagger() {
		tagger.distance++;
		tagger.y += directions[tagger.d][0];
		tagger.x += directions[tagger.d][1];
		
		if(tagger.y == 0 && tagger.x == 0) {
			tagger.d = 2;
			tagger.max_distance = n;
			tagger.distance = 1;
			tagger.cnt = 1;
			tagger.val = -1;
		} else if(tagger.y == n / 2 && tagger.x == n / 2) {
			tagger.d = 0;
			tagger.max_distance = 1;
			tagger.distance = 0;
			tagger.cnt = 0;
			tagger.val = 1;
		} else {
			if(tagger.distance == tagger.max_distance) {
				int val = tagger.val;
				tagger.distance = 0;
				tagger.d = (tagger.d + (tagger.d + val >= 0 ? 0 : n - 1) + val) % 4;
				tagger.cnt++;
				if(tagger.cnt == 2) {
					tagger.max_distance += val;
					tagger.cnt = 0;
				}
			}
		}
	}
	
	static void move_runner() {
		for(Player runner: runners) {
			if(!valid_run(runner)) {
				continue;
			}

			int d = runner.d;
			int my = runner.y + directions[d][0];
			int mx = runner.x + directions[d][1];
			if(0 <= my && my < n && 0 <= mx && mx < n) {
				if(my != tagger.y || mx != tagger.x) {
					runner.y = my;
					runner.x = mx;
				}
			} else {
				d = d == 0 ? 2 : d == 2 ? 0 : d == 1 ? 3 : 1;
				my = runner.y + directions[d][0];
				mx = runner.x + directions[d][1];
				if(my != tagger.y || mx != tagger.x) {
					runner.y = my;
					runner.x = mx;
					runner.d = d;
				}
			}
		}
	}
	
	static boolean valid_run(Player runner) {
		if(Math.abs(runner.x - tagger.x) + Math.abs(runner.y - tagger.y) <= 3) {
			return true;
		}
		return false;
	}
	
	static void catch_runner(int turn) {
		int catched = 0;
		int size = runners.size() - 1;
		int[] d = directions[tagger.d];
		
		for(int i = size; i > -1; i--) {
			Player runner = runners.get(i);
			for(int distance = 0; distance < 3; distance++) {
				if(tagger.y + d[0] * distance == runner.y && tagger.x + d[1] * distance == runner.x) {
					if(!trees.contains(runner.y + ", " + runner.x)) {
						runners.remove(i);
						catched++;
					}
				}
			}
		}
		
		answer += (catched * turn);
	}

	static void solve() {
		for(int turn = 1; turn <= k; turn++) {
			move_runner();
			move_tagger();
			catch_runner(turn);
		}
		
		System.out.println(answer);
	}
}

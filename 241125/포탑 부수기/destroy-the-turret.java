import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, k;
	static int[][] towers;
	static int[][] recent;
	static boolean[][] participants;
	static int answer = 0;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		towers = new int[n][m];
		recent = new int[n][m];
		participants = new boolean[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				towers[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		solve();
	}
	
	static class Tower {
		int row, col, atk, recent;

		public Tower(int row, int col, int atk, int recent) {
			this.row = row;
			this.col = col;
			this.atk = atk;
			this.recent = recent;
		}
	}

	static int[] find_attacker() {
		int max_atk = 5000;
		ArrayList<Tower> attackers = new ArrayList<>();

		for (int row = 0; row < n; row++) {
			for (int col = 0; col < m; col++) {
				if (0 != towers[row][col] && towers[row][col] <= max_atk) {
					max_atk = towers[row][col];
					attackers.add(new Tower(row, col, towers[row][col], recent[row][col]));
				}
			}
		}
		Collections.sort(attackers, Comparator
				.comparingInt((Tower o) -> o.atk)
				.thenComparingInt((o) -> -o.recent)
				.thenComparingInt((o) -> -(o.row + o.col))
				.thenComparingInt((o) -> -o.col)
				);
		Tower attacker = attackers.get(0);

		return new int[] { attacker.row, attacker.col };
	}

	static int[] find_target() {
		int min_atk = 0;
		ArrayList<Tower> targeters = new ArrayList<>();

		for (int row = 0; row < n; row++) {
			for (int col = 0; col < m; col++) {
				if (0 != towers[row][col] && towers[row][col] >= min_atk) {
					min_atk = towers[row][col];
					targeters.add(new Tower(row, col, towers[row][col], recent[row][col]));
				}
			}
		}
		Collections.sort(targeters, Comparator
				.comparingInt((Tower o) -> -o.atk)
				.thenComparingInt((o) -> o.recent)
				.thenComparingInt((o) -> o.row + o.col)
				.thenComparingInt((o) -> o.col)
				);
		Tower target = targeters.get(0);

		return new int[] { target.row, target.col };
	}

	static void attack(int[] attacker, int[] target, int turn) {
		participants[attacker[0]][attacker[1]] = true;
		participants[target[0]][target[1]] = true;
		towers[attacker[0]][attacker[1]] += (n + m);
		recent[attacker[0]][attacker[1]] = turn;
		if (!laser(attacker, target)) {
			bomb(attacker, target);
		}
	}

	static boolean laser(int[] attacker, int[] target) {
		int atk = towers[attacker[0]][attacker[1]];
		int[][][] visited = new int[n][m][2];
		visited[attacker[0]][attacker[1]] = attacker;
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(attacker);

		while (!q.isEmpty()) {
			int[] current = q.poll();
			if (current[0] == target[0] && current[1] == target[1]) {
				towers[current[0]][current[1]] = Math.max(0, towers[current[0]][current[1]] - atk);
				while (true) {
					current = visited[current[0]][current[1]];

					if (current[0] == attacker[0] && current[1] == attacker[1]) {
						return true;
					}
					participants[current[0]][current[1]] = true;
					towers[current[0]][current[1]] = Math.max(0, towers[current[0]][current[1]] - (atk / 2));
				}
			}

			for (int[] d : new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } }) {
				int my = (current[0] + d[0] + n) % n;
				int mx = (current[1] + d[1] + m) % m;
				if (towers[my][mx] > 0 && visited[my][mx][0] == 0 && visited[my][mx][1] == 0) {
					q.add(new int[] { my, mx });
					visited[my][mx] = new int[] { current[0], current[1] };
				}
			}
		}

		return false;
	}

	static void bomb(int[] attacker, int[] target) {
		int atk = towers[attacker[0]][attacker[1]];
		towers[target[0]][target[1]] = Math.max(0, towers[target[0]][target[1]] - atk);
		for (int[] d : new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } }) {
			int my = (target[0] + d[0] + n) % n;
			int mx = (target[1] + d[1] + m) % m;

			if (towers[my][mx] != 0 && !(attacker[0] == my && attacker[1] == mx)) {
				towers[my][mx] = Math.max(0, towers[my][mx] - (atk / 2));
				participants[my][mx] = true;
			}
		}
	}

	static void recover() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!participants[i][j] && towers[i][j] != 0) {
					towers[i][j] += 1;
				}
			}
		}
		participants = new boolean[n][m];
	}
	
	static boolean check_terminate() {
		int rest_tower = n * m;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(towers[i][j] == 0) {
					rest_tower -= 1;
				}
			}
		}
		return rest_tower <= 1 ? true : false;
	}

	static void solve() {
		int[] attacker, target;

		for (int turn = 1; turn <= k; turn++) {
			attacker = find_attacker();
			target = find_target();
			attack(attacker, target, turn);
			if(check_terminate())
				break;
			recover();
		}
		for(int[] i: towers)
			answer = Math.max(answer, Arrays.stream(i).max().getAsInt());
		
		System.out.println(answer);
	}
}

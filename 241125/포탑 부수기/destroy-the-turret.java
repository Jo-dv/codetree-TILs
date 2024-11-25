import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, k;
	static int[][] towers;
	static int[][] recent;
	static boolean[][] participants;
	static int survivor = n * m;
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

	static int[] find_attacker(int turn) {
		int max_atk = 5001;
		int attacker_y = 0, attacker_x = 0;
		int recently_turn = 0;

		for (int col = n - 1; col >= 0; col--) {
			for (int row = m - 1; row >= 0; row--) {
				if (0 < towers[col][row] && towers[col][row] <= max_atk && recently_turn <= recent[col][row]) {
					max_atk = towers[col][row];
					recently_turn = recent[col][row];
					attacker_y = col;
					attacker_x = row;
				}
			}
		}

		towers[attacker_y][attacker_x] += (n + m);
		recent[attacker_y][attacker_x] = turn;
		return new int[] { attacker_y, attacker_x };
	}

	static int[] find_target(int turn) {
		int min_atk = 1;
		int target_y = 0, target_x = 0;
		int recently_turn = turn;

		for (int col = 0; col < n; col++) {
			for (int row = 0; row < m; row++) {
				if (towers[col][row] >= min_atk && recently_turn >= recent[col][row]) {
					min_atk = towers[col][row];
					recently_turn = recent[col][row];
					target_y = col;
					target_x = row;
				}
			}
		}

		return new int[] { target_y, target_x };
	}

	static void attack(int[] attacker, int[] target) {
		participants[attacker[0]][attacker[1]] = true;
		participants[target[0]][target[1]] = true;
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

		for (int[] d : new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 }, { -1, -1 }, { -1, 1 }, { 1, -1 },
				{ 1, 1 } }) {
			int my = (target[0] + d[0] + n) % n;
			int mx = (target[1] + d[1] + m) % m;
			if (towers[my][mx] != 0 && attacker[0] != my && attacker[1] != mx) {
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

	static void solve() {
		int[] attacker, target;

		for (int turn = 1; turn <= k; turn++) {
//			if(survivor == 1)
//				break;
			attacker = find_attacker(turn);
			target = find_target(turn);
			attack(attacker, target);
			recover();
		}
		
		for(int[] i: towers)
			answer = Math.max(answer, Arrays.stream(i).max().getAsInt());
		
		System.out.println(answer);
	}
}

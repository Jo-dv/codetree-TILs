import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, k;
	static int[][] map;
	static HashMap<String, PriorityQueue<Integer>> guns;
	static Player[] players;
	static int y, x, d, s;
	static int[][] directions = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

	static class Player {
		int y, x, d, s, gun, score;

		public Player(int y, int x, int d, int s, int gun, int score) {
			this.y = y;
			this.x = x;
			this.d = d;
			this.s = s;
			this.gun = gun;
			this.score = score;
		}

		@Override
		public String toString() {
			return "Player [y=" + y + ", x=" + x + ", d=" + d + ", s=" + s + ", gun=" + gun + ", score=" + score + "]";
		}
		
		
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		map = new int[n][n];
		guns = new HashMap<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				String key = i + ", " + j;
				map[i][j] = Integer.parseInt(st.nextToken());
				guns.put(key, new PriorityQueue<>((o1, o2) -> o2 - o1));
				guns.get(key).add(map[i][j]);
			}
		}
		players = new Player[m];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			y = Integer.parseInt(st.nextToken()) - 1;
			x = Integer.parseInt(st.nextToken()) - 1;
			d = Integer.parseInt(st.nextToken());
			s = Integer.parseInt(st.nextToken());
			players[i] = new Player(y, x, d, s, 0, 0);
		}
		
		solve();
	}
	
	static void move_loser(Player loser) {
		for(int i = 0; i < 4; i++) {
			int[] d = directions[loser.d];
			boolean flag = false;
			int my = loser.y + d[0];
			int mx = loser.x + d[1];
			boolean range = my < 0 || my >= n || mx < 0 || mx >= n;
			if(range) {
				loser.d = (loser.d + 1) % 4;
				continue;
			}
			for(Player player: players) {
				if(my == player.y && mx == player.x) {
					loser.d = (loser.d + 1) % 4;
					flag = true;
					break;
				}
			}
			if(flag) {
				continue;
			}
			loser.y = my;
			loser.x = mx;
			if(guns.get(loser.y + ", " + loser.x).peek() > 0) {
				int put_gun = loser.gun;
				loser.gun = guns.get(loser.y + ", " + loser.x).poll();
				if(put_gun > 0) {
					guns.get(loser.y + ", " + loser.x).add(put_gun);
				}
			}
			break;
		}
	}
	
	static void fight_player(Player player, Player enemy) {
		int player_atk = player.s + player.gun;
		int enemy_atk = enemy.s + enemy.gun;
		if(player_atk > enemy_atk) {
			player.score += Math.abs(player_atk - enemy_atk);
			if(enemy.gun > 0) {
				guns.get(enemy.y + ", " + enemy.x).add(enemy.gun);
				enemy.gun = 0;
			}
			get_gun(player);
			move_loser(enemy);
		} else if(player_atk == enemy_atk) {
			if(player.s > enemy.s) {
				player.score += Math.abs(player_atk - enemy_atk);
				if(enemy.gun > 0) {
					guns.get(enemy.y + ", " + enemy.x).add(enemy.gun);
					enemy.gun = 0;
				}
				get_gun(player);
				move_loser(enemy);
			} else if(player.s < enemy.s) {
				enemy.score += Math.abs(player_atk - enemy_atk);
				if(player.gun > 0) {
					guns.get(player.y + ", " + player.x).add(player.gun);
					player.gun = 0;
				}
				get_gun(enemy);
				move_loser(player);
			}
		} else {
			enemy.score += Math.abs(player_atk - enemy_atk);
			if(player.gun > 0) {
				guns.get(player.y + ", " + player.x).add(player.gun);
				player.gun = 0;
			}
			get_gun(enemy);
			move_loser(player);
		}
	}
	
	static void get_gun(Player player) {
		int put_gun = player.gun;
		String pos = player.y + ", " + player.x;
		if(!guns.get(pos).isEmpty() && guns.get(pos).peek() > put_gun) {
			player.gun = guns.get(pos).poll();
			guns.get(pos).add(put_gun);
		}
	}

	static void move_player() {
		for (int player = 0; player < m; player++) {
			boolean fight = false;
			int[] d = directions[players[player].d];
			int my = players[player].y + d[0];
			int mx = players[player].x + d[1];
			if (my < 0 || my >= n || mx < 0 || mx >= n) {
				my = players[player].y - d[0];
				mx = players[player].x - d[1];
				players[player].d = (players[player].d + 2) % 4;
			}
			players[player].y = my;
			players[player].x = mx;
			for(int enemy = 0; enemy < m; enemy++) {
				if(player == enemy) {
					continue;
				}
				if(players[player].y == players[enemy].y && players[player].x == players[enemy].x) {
					fight_player(players[player], players[enemy]);
					fight = true;
					break;
				}
			}
			if(!fight) {
				get_gun(players[player]);
			}
		}
	}

	static void solve() {
		for (int turn = 1; turn <= k; turn++) {
			move_player();
		}
		StringBuilder sb = new StringBuilder();
		for(Player player: players)
			sb.append(player.score).append(" ");
		System.out.println(sb);
	}
}

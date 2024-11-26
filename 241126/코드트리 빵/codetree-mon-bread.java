import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int[][] map;
	static int y, x;
	static boolean[] arrive;
	static Pos[] people;
	static Pos[] stores;
	static int time = 0;
	static int[][] directions = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
	
	static class Pos {
		int y, x;
		
		public Pos(int y, int x) {
			this.y = y;
			this.x = x;
		}

		@Override
		public String toString() {
			return "Pos [y=" + y + ", x=" + x + "]";
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][n];
		arrive = new boolean[m + 1];
		people = new Pos[m + 1];
		stores = new Pos[m + 1];
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for(int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			y = Integer.parseInt(st.nextToken()) - 1;
			x = Integer.parseInt(st.nextToken()) - 1;
			stores[i] = new Pos(y, x);
			people[i] = new Pos(-1, -1);
		}
		
		solve();
	}
	
	static int[][] connect_road(int i) {
		Pos store = stores[i];  // 해당 편의점을 기점으로 가장 가까운 편의점 탐색
		int[][] visited = new int[n][n];
		visited[store.y][store.x] = 1;
		ArrayDeque<Pos> dq = new ArrayDeque<>();
		dq.add(store);
		
		while(!dq.isEmpty()) {
			Pos current = dq.poll();
			for(int[] d: directions) {
				int my = current.y + d[0], mx = current.x + d[1];
				if(0 <= my && my < n && 0 <= mx && mx < n && visited[my][mx] == 0 && map[my][mx] != -1) {
					visited[my][mx] = visited[current.y][current.x] + 1;
					dq.add(new Pos(my, mx));
				}
			}
		}
		
		return visited;
	}
	
	static void find_base(int i) {
		int[][] road = connect_road(i);
		Pos man = people[i];  // 이 사람의 베이스켐프를 지정할 것
		int distance = Integer.MAX_VALUE;

		for(int y = 0; y < n; y++) {
			for(int x = 0; x < n; x++) {
				if(map[y][x] == 1 && distance > road[y][x]) {
					distance = road[y][x];
					man.y = y;
					man.x = x;
				}
			}
		}
		
		map[man.y][man.x] = -1;  // 이동 불가의 의미
	}
	
	static void go_store(int i) {
		int[][] road = connect_road(i);
		Pos man = people[i];  // 이 사람의 베이스켐프를 지정할 것
		int distance = Integer.MAX_VALUE;
		int final_y = -1, final_x = -1;
		
		for(int[] d: directions) {
			int my = man.y + d[0], mx = man.x + d[1];
			if(0 <= my && my < n && 0 <= mx && mx < n && map[my][mx] != -1 && distance > road[my][mx]) {
				distance = road[my][mx];
				final_y = my;
				final_x = mx;
			}
		}
		
		man.y = final_y;
		man.x = final_x;
	}
	
	static void update_info() {
		for(int i = 1; i <= m; i++) {
			Pos man = people[i];
			Pos store = stores[i];
			if(man.y == store.y && man.x == store.x) {
				arrive[i] = true;
				map[store.y][store.x] = -1;
			}
		}
	}
	
	static boolean check_terminate() {
		for(int i = 1; i <= m; i++) {
			if(!arrive[i]) {
				return false;
			}
		}
		return true;
	}
	
	static void solve() {
		while(true) {
			time += 1;
			for(int i = 1; i <= m; i++) {
				if(arrive[i] || people[i].y == -1 && people[i].x == -1) {  // 편의점에 도착했거나, 아직 베이스켐프가 아니라면
					continue;
				}
				go_store(i);
			}
			update_info();  // 모든 사람들의 이동이 끝났을 때, 편의점을 막을지 말지 확인해야 함
			if(check_terminate()) {  // 이 시점에서 종료유무 체크해야 함
				break;
			}
			if(time <= m) {
				// 사람들을 베이스캠프로
				find_base(time);
			}
		}
		
		System.out.println(time);
	}
}

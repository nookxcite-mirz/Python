# 지료구조
# --------------------------------------------------------------------
# Topic3 : 그래프
# --------------------------------------------------------------------

#--------------------------------------------------------------------
# Chapter1 : 그래프란?
#   - 그래픽는 행열 및 연결 리스트로 모두 구현이 가능한다.
#--------------------------------------------------------------------
"""
	- 연결 관계를 나타낼때 사용됨
		: 위치 데이터 (지하철 노선도, 네비게이션)
		: 사회 연결망 (친구 관계)

	- 노드와 엣지로 구성됨 (엣지는 연결선이며, 엣지가 있는경우 인접으로 정의함)
	- 노드와 노드가 엣지들로 연결 되어 있을때 거치는 엣지들 집합을 경로라고 정의함
	- 최단경로(가장 짧은 경로), 사이클(한바퀴 돌수 있음), 차수(엣지 수)

	- 엣지가 쌍방향일 경우 [무방향 그래프]
	- 엣지가 단방향일 경우 [방향 그래프] - 출력차수, 입력차수로 분리됨.
	- 엣지에 가중치가 있는 경우 [가중치 그래프]
"""

# 그래프 노드 만들어보기
class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []  # 인접 리스트

    def add_connection(self, other_station):
        """지하철 역 노드 사이 엣지 저장하기"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


    def __str__(self):
        """지하철 노드 문자열 메소드. 지하철 역 이름과 연결된 역들을 모두 출력해준다"""
        res_str = f"{self.station_name}: "  # 리턴할 문자열

        # 리턴할 문자열에 인접한 역 이름들 저장
        for station in self.adjacent_stations:
            res_str += f"{station.station_name} "

        return res_str


def create_station_nodes(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, 'rt', encoding='UTF8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)     # 새로운 인스턴스를 생성하고
                    stations[station_name] = current_station        # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다

    return stations


stations1 = create_station_nodes("./study_DataStructure3_stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (채점을 위해 역 이름 순서대로 출력)
# for station in sorted(stations1.keys()):
#    print(stations1[station].station_name)

# 입접 행열
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]
adjacency_matrix[0][1] = adjacency_matrix[1][0] = 1
adjacency_matrix[0][2] = adjacency_matrix[2][0] = 1
adjacency_matrix[1][5] = adjacency_matrix[5][1] = 1
adjacency_matrix[1][3] = adjacency_matrix[3][1] = 1
adjacency_matrix[2][5] = adjacency_matrix[5][2] = 1
adjacency_matrix[3][5] = adjacency_matrix[5][3] = 1
adjacency_matrix[3][4] = adjacency_matrix[4][3] = 1
adjacency_matrix[4][5] = adjacency_matrix[5][4] = 1
#print(adjacency_matrix)


# 인접 리스트로 구현
def create_subway_graph(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, 'rt', encoding='UTF8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            prevStation = None
            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다
                else:
                    current_station = stations[station_name]

                if prevStation is not None:
                    current_station.add_connection(prevStation)
                prevStation = current_station

    return stations

stations1 = create_subway_graph("./study_DataStructure3_stations.txt")  # stations.txt 파일로 그래프를 만든다

# stations에 저장한 역 인접 역들 출력 (채점을 위해 역 이름 순서대로 출력)
for station in sorted(stations1.keys()):
        print(stations1[station])


#--------------------------------------------------------------------
# Chapter2 : 그래프 탐색
#   - 하나의 시작점 노드에 연결된 모든 노드를 찾는것.
#   - 연결되어 있는검 찾거나, 최단거리를 검색하는 기능.
#--------------------------------------------------------------------

"""
Breadth First Search (BFS) : 알고리즘
    - 너비 우선 검색
"""

"""
Depth First Search (DFS) : 알고리즘
    - 깊이 우선 검색
"""

#--------------------------------------------------------------------
# Chapter3 : 최단 경로 알고리즘
#--------------------------------------------------------------------



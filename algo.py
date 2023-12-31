# SOURCE CODE FINAL PROJECT 
# KELOMPOK 15 KKA(C)
# Nama: 1. Fairuuz Azmi Firas - 5025221057
#       2. Ivan Fairuz Adinata - 5025221167
#       3. Gilang Kista Ramadhan - 502522173

# Import library yang dibutuhkan
import heapq
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

# Definisikan kelas Graph
class Graph:
    def __init__(self):
        # Konstruktor kelas dan atribut-atributnya
        self.graph = defaultdict(list)
        self.static_heuristic = {}
        self.edge_costs = {}
        
    # Metode untuk menambahkan edge ke dalam graf
    def add_edge(self, from_node, to_node, cost):
        # Menambahkan edge dari from_node ke to_node dengan cost tertentu
        self.graph.setdefault(from_node, []).append(to_node)
        self.edge_costs[(from_node, to_node)] = cost

    # Metode untuk menambahkan heuristic statis untuk suatu node
    def add_static_heuristic(self, node, heuristic_value):
        # Menambahkan heuristic statis untuk suatu node pada graf
        self.static_heuristic[node] = heuristic_value

    # Metode implementasi algoritma A* search untuk mencari jalur terpendek untuk suatu node pada graf
    def a_star_search(self, start, finish):
        # Implementasi algoritma A* search
        visited = set()
        priority_queue = [(0, start)]
        g_values = {node: float('inf') for node in self.graph.keys()}
        g_values[start] = 0
        path = {}

        while priority_queue:
            _, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == finish:
                result_path = [current_node]
                while current_node != start:
                    current_node = path[current_node]
                    result_path.append(current_node)
                result_path.reverse()
                return result_path

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    tentative_g_value = g_values[current_node] + self.edge_costs.get((current_node, neighbor), float('inf'))
                    if tentative_g_value < g_values.get(neighbor, float('inf')):
                        g_values[neighbor] = tentative_g_value
                        h_value = self.static_heuristic.get(neighbor, 0)
                        f_value = tentative_g_value + h_value
                        heapq.heappush(priority_queue, (f_value, neighbor))
                        path[neighbor] = current_node

        return None

# Inisialisasi objek Graph
g = Graph()

# Definisi jalur utara pada graf
# JALUR UTARA
g.add_edge('SURABAYA PASAR TURI', 'LAMONGAN', 38)
g.add_edge('LAMONGAN', 'BOJONEGORO', 62)
g.add_edge('BOJONEGORO', 'CEPU', 36)
g.add_edge('CEPU', 'NGROMBO', 80)
g.add_edge('NGROMBO', 'SEMARANG TAWANG', 49)
g.add_edge('SEMARANG TAWANG', 'PEKALONGAN',	89)
g.add_edge('PEKALONGAN', 'TEGAL', 60)
g.add_edge('TEGAL',	'CIREBON', 71)
g.add_edge('CIREBON', 'JATIBARANG', 40)
g.add_edge('JATIBARANG', 'CIKAMPEK', 98)
g.add_edge('CIKAMPEK', 'KARAWANG', 22)

g.add_edge('LAMONGAN', 'SURABAYA PASAR TURI', 38)
g.add_edge('BOJONEGORO', 'LAMONGAN', 62)
g.add_edge('CEPU', 'BOJONEGORO', 36)
g.add_edge('NGROMBO', 'CEPU', 80)
g.add_edge('SEMARANG TAWANG', 'NGROMBO', 49)
g.add_edge('PEKALONGAN', 'SEMARANG TAWANG', 89)
g.add_edge('TEGAL', 'PEKALONGAN', 60)
g.add_edge('CIREBON', 'TEGAL',	71)
g.add_edge('JATIBARANG', 'CIREBON', 40)
g.add_edge('CIKAMPEK', 'JATIBARANG', 98)
g.add_edge('KARAWANG', 'CIKAMPEK', 22)

# Definisi jalur tengah pada graf
# JALUR TENGAH
g.add_edge('SURABAYA GUBENG', 'SEPANJANG', 45)
g.add_edge('SEPANJANG',	'MOJOKERTO', 45)
g.add_edge('MOJOKERTO',	'JOMBANG', 23)
g.add_edge('JOMBANG', 'KERTOSONO', 38)
g.add_edge('KERTOSONO',	'MADIUN', 68)
g.add_edge('MADIUN', 'WALIKUKUN', 43)
g.add_edge('WALIKUKUN',	'SRAGEN', 23)
g.add_edge('SRAGEN', 'SOLO BALAPAN', 30)
g.add_edge('SOLO BALAPAN', 'GUNDIH', 41)
g.add_edge('GUNDIH', 'SEMARANG TAWANG',	66)
g.add_edge('SEMARANG TAWANG', 'PEKALONGAN',	89)
g.add_edge('PEKALONGAN', 'TEGAL', 60)
g.add_edge('TEGAL',	'CIREBON', 71)
g.add_edge('CIREBON', 'JATIBARANG', 40)
g.add_edge('JATIBARANG', 'CIKAMPEK', 98)
g.add_edge('CIKAMPEK', 'KARAWANG', 22)

g.add_edge('SEPANJANG', 'SURABAYA GUBENG', 45)
g.add_edge('MOJOKERTO', 'SEPANJANG', 45)
g.add_edge('MOJOKERTO',	'JOMBANG', 23)
g.add_edge('KERTOSONO', 'JOMBANG', 38)
g.add_edge('MADIUN', 'KERTOSONO', 68)
g.add_edge('WALIKUKUN', 'MADIUN', 43)
g.add_edge('SRAGEN', 'WALIKUKUN', 23)
g.add_edge('SOLO BALAPAN', 'SRAGEN', 30)
g.add_edge('GUNDIH', 'SOLO BALAPAN', 41)
g.add_edge('SEMARANG TAWANG', 'GUNDIH', 66)
g.add_edge('PEKALONGAN', 'SEMARANG TAWANG', 89)
g.add_edge('TEGAL', 'PEKALONGAN', 60)
g.add_edge('CIREBON', 'TEGAL',	71)
g.add_edge('JATIBARANG', 'CIREBON', 40)
g.add_edge('CIKAMPEK', 'JATIBARANG', 98)
g.add_edge('KARAWANG', 'CIKAMPEK', 22)

# Definisi jalur selatan pada graf
# JALUR SELATAN
g.add_edge('SURABAYA GUBENG', 'SEPANJANG', 45)
g.add_edge('SEPANJANG',	'MOJOKERTO', 23)
g.add_edge('MOJOKERTO',	'JOMBANG', 38)
g.add_edge('JOMBANG', 'KERTOSONO', 68)
g.add_edge('KERTOSONO',	'MADIUN', 43)
g.add_edge('MADIUN', 'WALIKUKUN', 23)
g.add_edge('WALIKUKUN',	'SRAGEN', 23)
g.add_edge('SRAGEN', 'SOLO BALAPAN', 30)
g.add_edge('SOLO BALAPAN', 'TUGU', 56)
g.add_edge('TUGU', 'KEDUNDANG', 29)
g.add_edge('KEDUNDANG', 'KUTOARJO', 36)
g.add_edge('KUTOARJO', 'KEBUMEN', 28)
g.add_edge('KEBUMEN', 'KROYA', 47)
g.add_edge('KROYA', 'TASIKMALAYA', 130)
g.add_edge('TASIKMALAYA', 'CIPEUNDEUY', 33)
g.add_edge('CIPEUNDEUY', 'NAGREG', 43)
g.add_edge('NAGREG', 'PADALARANG', 45)

g.add_edge('SEPANJANG', 'SURABAYA GUBENG', 45)
g.add_edge('MOJOKERTO', 'SEPANJANG', 23)
g.add_edge('JOMBANG', 'MOJOKERTO', 38)
g.add_edge('KERTOSONO', 'JOMBANG', 68)
g.add_edge('MADIUN', 'KERTOSONO', 43)
g.add_edge('WALIKUKUN', 'MADIUN', 23)
g.add_edge('SRAGEN', 'WALIKUKUN', 23)
g.add_edge('SOLO BALAPAN', 'SRAGEN', 30)
g.add_edge('TUGU', 'SOLO BALAPAN', 56)
g.add_edge('KEDUNDANG', 'TUGU', 29)
g.add_edge('KUTOARJO', 'KEDUNDANG', 36)
g.add_edge('KEBUMEN', 'KUTOARJO', 28)
g.add_edge('KROYA', 'KEBUMEN', 47)
g.add_edge('TASIKMALAYA', 'KROYA', 130)
g.add_edge('CIPEUNDEUY', 'TASIKMALAYA', 33)
g.add_edge('NAGREG', 'CIPEUNDEUY', 43)
g.add_edge('PADALARANG', 'NAGREG', 45)

# Definisi jalur tambahan pada graf
# JALUR TAMBAHAN
g.add_edge('HALIM',	'PASAR SENEN',	9)
g.add_edge('PADALARANG', 'TEGALUAR', 28)
g.add_edge('SURABAYA PASAR TURI', 'SURABAYA GUBENG', 5)

g.add_edge('PASAR SENEN', 'HALIM', 9)
g.add_edge('TEGALUAR', 'PADALARANG', 28)
g.add_edge('SURABAYA GUBENG', 'SURABAYA PASAR TURI', 5)

# Definisi heuristic statis untuk stasiun pada graf
# HEURISTIK STASIUN 
g.add_static_heuristic('SURABAYA PASAR TURI', 35)
g.add_static_heuristic('LAMONGAN', 60)
g.add_static_heuristic('BOJONEGORO', 50)
g.add_static_heuristic('CEPU', 60)
g.add_static_heuristic('NGROMBO', 70)
g.add_static_heuristic('SEMARANG TAWANG', 35)
g.add_static_heuristic('PEKALONGAN', 55)
g.add_static_heuristic('TEGAL', 45)
g.add_static_heuristic('CIREBON', 45)
g.add_static_heuristic('JATIBARANG', 60)
g.add_static_heuristic('CIKAMPEK', 65)
g.add_static_heuristic('KARAWANG', 45)
                       
g.add_static_heuristic('SURABAYA GUBENG', 35)
g.add_static_heuristic('SEPANJANG', 70)
g.add_static_heuristic('MOJOKERTO', 70)
g.add_static_heuristic('JOMBANG', 70)
g.add_static_heuristic('KERTOSONO', 50)
g.add_static_heuristic('MADIUN', 40)
g.add_static_heuristic('WALIKUKUN', 70)
g.add_static_heuristic('SRAGEN', 70)
g.add_static_heuristic('SOLO BALAPAN', 35)
g.add_static_heuristic('GUNDIH', 55)
g.add_static_heuristic('SEMARANG TAWANG', 35)
g.add_static_heuristic('PEKALONGAN', 55)
g.add_static_heuristic('TEGAL', 45)
g.add_static_heuristic('CIREBON', 45)
g.add_static_heuristic('JATIBARANG', 60)
g.add_static_heuristic('CIKAMPEK', 65)
g.add_static_heuristic('KARAWANG', 45)
                       
g.add_static_heuristic('SURABAYA GUBENG', 35)
g.add_static_heuristic('SEPANJANG', 70)
g.add_static_heuristic('MOJOKERTO', 70)
g.add_static_heuristic('JOMBANG', 70)
g.add_static_heuristic('KERTOSONO', 50)
g.add_static_heuristic('MADIUN', 40)
g.add_static_heuristic('WALIKUKUN', 70)
g.add_static_heuristic('SRAGEN', 70)
g.add_static_heuristic('SOLO BALAPAN', 35)
g.add_static_heuristic('TUGU', 35)
g.add_static_heuristic('KEDUNDANG', 80)
g.add_static_heuristic('KUTOARJO', 45)
g.add_static_heuristic('KEBUMEN', 60)
g.add_static_heuristic('KROYA', 55)
g.add_static_heuristic('TASIKMALAYA', 60)
g.add_static_heuristic('CIPEUNDEUY', 70)
g.add_static_heuristic('NAGREG', 80)
g.add_static_heuristic('PADALARANG', 50)

g.add_static_heuristic('HALIM', 35)
g.add_static_heuristic('PASAR SENEN', 35)
g.add_static_heuristic('PADALARANG', 50)
g.add_static_heuristic('TEGALUAR', 45)

# Tentukan stasiun awal dan akhir untuk hasil yang statis
start_node = 'PADALARANG'
finish_node = 'SURABAYA PASAR TURI'

# Lakukan A* search dan tampilkan hasilnya
result = g.a_star_search(start_node, finish_node)

if result:
    print(f"Jalur dari {start_node} ke {finish_node}: {' -> '.join(result)}")
else:
    print(f"Tidak ada jalur dari {start_node} ke {finish_node}")


#########################################

G = nx.DiGraph()

for node, neighbors in g.graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor, weight=g.edge_costs.get((node, neighbor, 0)))

pos = nx.random_layout(G)
# pos = nx.circular_layout(G)

node_labels = {node: f"{node}\nH: {g.static_heuristic.get(node, 0)}" for node in G.nodes}
edge_labels = {(node, neighbor): g.edge_costs.get((node, neighbor), 0) for node, neighbor in G.edges}

plt.figure(figsize=(10, 5))
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=700, node_color="skyblue", font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Tampilkan gambar
plt.show()
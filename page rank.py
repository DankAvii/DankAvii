Practical 8
pip install scikit-learn
pip install numpy
Aim: Link Analysis and PageRank
∙ Implement the PageRank algorithm to rank web pages based on link
analysis.
∙ Apply the PageRank algorithm to a small web graph and analyze the
results.
 
def pagerank(graph, damping_factor=0.85, epsilon=1.0e-8, max_iterations=100):
 
    num_nodes = len(graph)
 
    pagerank_scores = {node: 1.0 / num_nodes for node in graph}
 
    for _ in range(max_iterations):
 
        new_pagerank_scores = {}
        max_diff = 0
 
        for node in graph:
 
            new_pagerank = (1 - damping_factor) / num_nodes
 
            for referring_page, links in graph.items():
                if node in links:
                    num_outlinks = len(links)
                    new_pagerank += damping_factor * pagerank_scores[referring_page] / num_outlinks
 
            new_pagerank_scores[node] = new_pagerank
 
            diff = abs(new_pagerank - pagerank_scores[node])
            max_diff = max(max_diff, diff)
 
        pagerank_scores = new_pagerank_scores
 
        if max_diff < epsilon:
            break
 
    return pagerank_scores
 
 
# Example Web Graph
web_graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A']
}
 
pagerank_scores = pagerank(web_graph)
 
# Sort pages by rank
sorted_scores = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
 
print("PageRank Scores:")
 
for node, score in sorted_scores:
    print(node, ":", score)
 

 

ABC]cfd48df85c36814e673a8292f8651aac.png
def pagerank(graph, d=0.85, iterations=20):
 
    n = len(graph)
    rank = {page: 1/n for page in graph}
 
    for _ in range(iterations):
        new_rank = {}
 
        for page in graph:
            new_rank_value = (1-d)/n
 
            for node in graph:
                if page in graph[node]:
                    new_rank_value += d * rank[node] / len(graph[node])
 
            new_rank[page] = new_rank_value
 
        rank = new_rank
 
    return rank
 
 
# Web graph
web_graph = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"]
}
 
# Calculate PageRank
result = pagerank(web_graph)
 
print("PageRank Results:")
for page, score in result.items():
    print(page, ":", score)
 

98c8b157d294107bef23b600a2510675.png
def pagerank(graph, d=0.85, iterations=20):
 
    N = len(graph)
 
    # Initial rank
    rank = {page: 1/N for page in graph}
 
    for _ in range(iterations):
 
        new_rank = {}
 
        for page in graph:
            new_rank_value = (1 - d) / N
 
            for node in graph:
                if page in graph[node]:
                    new_rank_value += d * rank[node] / len(graph[node])
 
            new_rank[page] = new_rank_value
 
        rank = new_rank
 
    return rank
 
 
# Web graph
web_graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["A", "D"],
    "D": ["B"]
}
 
# Calculate PageRank
result = pagerank(web_graph)
 
print("PageRank Scores:")
for page, score in result.items():
    print(page, ":", round(score,4))

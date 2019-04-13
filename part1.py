
def compute_number_connections(graph, actor):

    movies = graph.get_neighbors(actor)

    actor_set = set()

    for movie in movies:

        actors = graph.get_neighbors(movie)

        actor_set.update(actors)


    return len(actor_set) - 1

def filter_pred(graph, pred):

    nodes = graph.get_nodes()
    arr = []
    for id in nodes:
        data = nodes[id]

        if pred(data):
            arr.append(data)

    return arr

def get_actors(graph):

    # nodes = graph.get_nodes()
    # arr = []
    # for id in nodes:
    #     data = nodes[id]
    #
    #     if data['json_class'] == 'Actor':
    #         arr.append(data)

    return filter_pred(graph, lambda data: data['json_class'] == 'Actor' )


def get_top_k_hub_actors(graph, k):

    arr = []

    for data in get_actors(graph):
        num_connections = compute_number_connections(graph, data['name'])
        arr.append((data, num_connections))

    arr.sort(key=lambda x:x[1], reverse=True)

    return arr[:k]


def compute_age_group_gross(graph):

    actors = get_actors(graph)

    # ages = []
    #
    # gross = []
    #
    grossCounts = [0] * 10

    for actor in actors:

        grossCounts[actor['age'] // 10] += actor['total_gross']

        # ages.append(actor['age'])
        #
        # gross.append(actor['total_gross'])

    return grossCounts


    # for age in ages

def plot_age_group_gross(graph):

    import matplotlib.pyplot as plt

    grossCounts = compute_age_group_gross(graph)

    x = list(range(10))

    plt.bar(x,  grossCounts)

    groups = ('0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99')

    # plot_age_group_gross(graph)

    plt.xticks(x, groups)

    plt.ylabel('Total Gross')

    plt.xlabel("Age Group")

    plt.title("Gross for different age group")

    maxi = 0

    for i in range(len(grossCounts)):

        if grossCounts[i] > grossCounts[maxi]:
            maxi = i


    print("Age group %s generates the most amount of money" % groups[maxi] )


    plt.show()


if __name__ == '__main__':

    from load_graph import load_graph

    graph = load_graph('data.json')

    top3 = get_top_k_hub_actors(graph, 3)

    top3 = [(x['name'], n) for x,n in top3]

    print("Top 3 hub actors")

    print(top3)

    plot_age_group_gross(graph)














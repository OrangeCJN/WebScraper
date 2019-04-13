

from unittest import TestCase

from part1 import compute_number_connections, compute_age_group_gross

from part1 import get_top_k_hub_actors

from load_graph import load_graph

import unittest

class TestGraph1(TestCase):

    def setUp(self):

        self.graph = load_graph('data.json')


    def test_comppute_number_connections(self):

        n = compute_number_connections(self.graph, 'Bruce Willis')

        self.assertEqual(n, 230)

        n = compute_number_connections(self.graph, 'Faye Dunaway')

        self.assertEqual(n, 12)

    def test_get_top_k_hub_actors(self):

        top3 = get_top_k_hub_actors(self.graph, 3)

        top3 = [(x['name'], n) for x,n in top3]

        self.assertEqual([('Bruce Willis', 230), ('Mickey Rourke', 28), ('Samuel L. Jackson', 23)], top3)


    def test_compute_age_group_gross(self):

        group_gross = compute_age_group_gross(self.graph)

        self.assertEqual([0, 0, 21767523, 2216132, 178214618, 1027863196, 1005773688, 1001143377, 1150162485, 16770084], group_gross)


if __name__ == "__main__":
    unittest.main()






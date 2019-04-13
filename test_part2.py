import unittest
import requests

class TestFlaskApi(unittest.TestCase):


    def test_get_actors(self):
        response = requests.get('http://127.0.0.1:5000/actors?name="Alan"&age=69')
        res = response.json()['actors'][0]
        self.assertEqual('Alan Rickman', res['name'])
        self.assertEqual(69, res['age'])

    def test_get_movies(self):
        response = requests.get('http://localhost:5000/movies?name="die_hard"|year=2010')
        res = response.json()['movies']

        for movie in res:
            self.assertTrue("die hard" in movie['name'].lower() or movie['year'] == 2010)


    def test_get_actor(self):
        response = requests.get('http://localhost:5000/actors/Bruce_Dern')
        res = response.json()
        self.assertEqual("Bruce Dern", res['name'])


    def test_get_movie(self):
        response = requests.get('http://localhost:5000/movies/Die_Hard_with_a_Vengeance')
        res = response.json()
        self.assertEqual("Die Hard with a Vengeance", res['name'])

    def test_put_actor(self):

        response = requests.put('http://localhost:5000/actors/bruce', json={"age": 20})
        res = response.json()

        self.assertEqual(res['age'], 20)

    def test_put_movie(self):

        response = requests.put('http://localhost:5000/movies/die_hard', json={"year": 1999})
        res = response.json()

        self.assertEqual(res['year'], 1999)


    def test_post_movie(self):

        response = requests.post('http://localhost:5000/movies', json={"name": "billy"})
        res = response.json()

        # print(res)

        self.assertTrue(res['name'],'billy')


    def test_post_actor(self):

        response = requests.post('http://localhost:5000/actors', json={"name": "me", "age": 10})
        res = response.json()

        # print(res)

        self.assertTrue(res['name'],'me')


    def test_deleete_actor1(self):

        response = requests.delete('http://localhost:5000/actors/xxx***')
        res = response.json()

        #print(res)

        self.assertTrue('error' in res)

    def test_deleete_actor2(self):

        response = requests.delete('http://localhost:5000/actors/Jeremy_Piven')
        res = response.json()

        self.assertTrue('error' not in res)

        self.assertEqual("Jeremy Piven", res['name'])


    def test_deleete_movie(self):

        response = requests.delete('http://localhost:5000/movies/The_Bye_Bye_Man')
        res = response.json()

        self.assertTrue('error' not in res)

        self.assertEqual("The Bye Bye Man", res['name'])










if __name__ == "__main__":
    unittest.main()
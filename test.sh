



curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/movies?name=die_hard

curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/actors?age=69

curl -i -H "Content-Type: application/json" -X PUT -d '{"age": 20}' http://localhost:5000/actors/bruce

curl -i -H "Content-Type: application/json" -X PUT -d '{"year": 2001}' http://localhost:5000/movies/die_hard

curl -i -H "Content-Type: application/json" -X POST -d '{"name": "billy"}' http://localhost:5000/movies

curl -i -H "Content-Type: application/json" -X POST -d '{"name": "me", "age": 10}' http://localhost:5000/actors

curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/actors/bruce

curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/actors/bruce

curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/movies/die_hard

curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/movies/die_hard
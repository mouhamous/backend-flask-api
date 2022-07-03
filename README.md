# Flask api user account management

## run a container for development or testing
```
docker-compose up 
```

## test endpoints using curl

### test server
```
curl localhost:5000
```

### authenticate user and get token
```
curl -X POST -d '{"username":"test", "password":"p@ssw0rd"}' localhost:5000/auth -H "Content-Type: application/json"
```

### update user email (require valid token)
``` 
curl -X PUT 'localhost:5000/users/1' -H 'Authorization: JWT $TOKEN' -H 'Content-Type: application/json' -d '{"email": "mynewemail@mail.tld"}'
 ```






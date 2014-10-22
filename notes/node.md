# node.js notes

## Express

### use express generator to generate apps:mo
```javascript
npm install -g express-generator
```

### express how to change port to 80?

```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3000
```

or 

```bash
sudo node app.js
```

### next() function

next refers to a function. The next command instructs Express to try processing the next route matching the current request.



## backbone.js


```
var Todo = Backbone.Model.extend({
  defaults: {
    title: '',
    completed: false
  },
   initialize: function(){
    console.log('This model has been initialized.');
    this.on('change:title', function(){
        console.log('- Values for this model have changed.');
    });
  },
   setTitle: function(newTitle){
    this.set({ title: newTitle });
  }
});

var myTodo = new Todo();
console.log(JSON.stringify(myTodo));
var todo2 = new Todo({
  title: 'Check the attributes of both model instances in the console.',
  completed: true
});
console.log(JSON.stringify(todo2));
console.log(todo2.get('completed'));
var todo2Attributes = todo2.toJSON();
console.log(todo2Attributes);
todo2.set("title", "Title attribute set through Model.set().");
```
## require.js
https://www.youtube.com/watch?v=eRqsZqLyYaU

## mongoDB


###　how to run node app using forever
[reference](http://blog.nodejitsu.com/keep-a-nodejs-server-up-with-forever/)

## References
[node-express-mongo quick start](http://cwbuecheler.com/web/tutorials/2013/node-express-mongo/)
[node-express-mongoose-demo](https://github.com/madhums/node-express-mongoose-demo/)
[notepad demo](https://github.com/alexyoung/nodepad/blob/master/app.js)
[async loading](https://github.com/mjhea0/node-express-ajax-craigslist)
[node and socket.io](http://www.plhwin.com/2014/05/28/nodejs-socketio/)
[node in production](http://blog.carbonfive.com/2014/06/02/node-js-in-production/)


## sails

#### how to create project
```javascript
sails new testProject
```
#### how to start server
```javascript
sails lift
```
#### how to generate REST api;
```
sails generate api user
```
#### how to check data using the ```localDiskDb``` ?

```bash
 find ./ -name "*.db"
.//.tmp/localDiskDb.db
vim .//.tmp/localDiskDb.db //then you can see the data inside it
```

#### sails reference
[ref](http://sailsjs.org/#/documentation/reference/)

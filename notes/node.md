# node.js notes

## Express

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
#GO


#### set up a web production server on ubuntu
```
sudo apt-get install curl git mercurial make binutils bison gcc
```



[ref](http://evanbyrne.com/blog/go-production-server-ubuntu-nginx)
[ref](https://github.com/moovweb/gvm)


### vim syntax highlight for go
```
sudo apt-get install vim-gocomplete gocode vim-syntax-go
vim-addon-manager install go-syntax
vim-addon-manager install gocode
```

### Install go on ubuntu
http://evanbyrne.com/blog/go-production-server-ubuntu-nginx

http://railskey.wordpress.com/2014/05/31/install-gogolang-on-ubuntu/



## BeeGo framework

#### how to return json data for the request
```
type User struct {
        Name string
        Age int
}

func (this *UserController) Get() {
        u := User{"chenbo",28}
        this.Data["json"] = &u
        this.ServeJson()
}
```
## swift language

### Basics

#### variables
```swift
var a = 1 //variable
let b = 2 //constant
```

#### ; and ,
```swift
var a = 0, b = 1, c = 2
var a = 0; var b = 1; var c = 2 
```

#### data types
```swift
//type safety
//Basic data types: Int, Double(小数点后15位), Float(小数点后6位), String
//String 不能用单引号', 只能用双引号"
//Bool: true or false (different with objective-c, YES/NO)
let decimalInt:Int = 17 //10进制
let binaryint:Int = 0b10001 //2进制
let octalInt:Int = 0o21  //8进制
let hexadecimalInt:Int = 0x11 //16进制

var myname:String = "airbob"
//方便的定义大数字位置
let bignum = 1_000_000  //print 1,000,000
let bignum_a = 1_0000_0000 //print 1,0000,0000

let numb:Int = Int(1.2) //强制类型转换
Int.max  //64位机器会显示64位最大值 
Int.max + 1 //报错
Int.min - 1 //报错

//String mutability:
let String   //it is same as objective-c NSString
var String  //it is same as objective-c NSMutableString

//init empty string
var emptyString = "" //method 1
var emptyString2 = String() //method 2
emptyString.isEmpty //check whether it is empty string
//使用for-in 遍历字符串
for character in str
{
  println(character)  //data type is Character
}

var a:Character = "!"
var b:String = "abc"
a = b //报错, data type error
//字符串长度
var str = "你好,play ground \U00001F496"
countElements(str)
var str2:NSString = str
str2.length  //objective-c method, it will count wrongly sometimes



```

#### if flow
```swift
//if 后condition可以不用括号, 但{}不可缺少
let trueVal = true
if trueVal
{
  println("it is true")
}
//Int 不可以直接做Bool来用
```

### tuples
```swift
//(,,,)   定义原型,objective-c 没有,python有
let registrationResult = (true, "username","female")
let (isRegisterSuccess, username, gender) = registrationResult  //access method 1 
registrationResult.0  //access method 2

//tuples 2
let registrationResult = (isRegisterSuccess:true, username:"username",gender:"female")
registrationResult.username //access method 2

//使用下划线(_)忽略部分数值
let loginResult = (true, "airbob")
let (isLoginSuccess, _) = loginResult
if isLoginSuccess 
{
  println("login success")
}
```

### optional variable
```swift
var imOptionalVar:Int?
imOptionalVar = 12

let userInput = "18"
var age = userInput.toInt() //it returns an optional variable
if age 
{
  println("your age is \(age)")   // \()打印变量
  println("your age is" + String(age)) //报错,age is optional, can not be invoked as this
  println("your age is" + String(age!)) //correct, optional variable 解包
  age   //
  age!  //解包成整型
}
else 
{
  println("user input is invalid")
}
//optional binding
if let userAge = userInput.toInt()
{
  println("your age is \(userAge)")   
}
else {
  println("user input is invalid")
}

var a:Int! //确保会有数值
```

### operators 
```swift
//assign operator
var a = 2 , b = 3 
if a = b {  //这里会报错, = operator 没有return type
}
//conditional operator
let statusBarHeight = 20 
let basicViewHeight = 568
var inFullScreenMode = true
var viewHeight = basicViewHeight + (isFullScreenMode? 0 : statusBarHeight)
//Range operator
a...b //[a,b] closed range
a..b //[a,b) half closed

for index in 1...10
{
  index  //constant by default
  }
```

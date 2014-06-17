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

let decimalInt:Int = 17 //10进制
let binaryint:Int = 0b10001 //2进制
let octalInt:Int = 0o21  //8进制
let hexadecimalInt:Int = 0x11 //16进制

var myname:String = "airbob"
//方便的定义大数字位置
let bignum = 1_000_000  //print 1,000,000
let bignum_a = 1_0000_0000 //print 1,0000,0000

let numb:Int = Int(1.2) //强制类型转换
```

package ex
import Array._

class Outer{
  class Inner{
        private def f(){println("f")}
        class InnerMost{
          f() // true
        }
  }
//  (new Inner).f()
}

// func and method
// val 语句可以定义函数，def 语句定义方法。
class Calculator{
  def add3(x: Int) = x + 3
  val func = (x: Int) => x + 3 // Lambda
}

// 在scala中没有静态方法和静态字段，
// 所以在scala中可以用object来实现这些功能，直接用对象名调用的方法都是采用这种实现方式。
// Adder.addInt
object Adder{
  def addInt( a:Int, b:Int ) : Int = {
    var sum:Int = 0
    sum = a + b
    return sum
  }
}

// 闭包是一个函数， 返回值依赖于声明在函数外部的一个或多个变量。

object Closure{
  var factor = 3 // 自由变量
  val multiplier = (i:Int) => i * factor
}

object example extends App {
      var myStr:String = "Hi"
      myStr += " IU"
      myStr.concat(" ")
      println(myStr.length())
      var myInt, herInt = 100
      var myTuple = (100,"Hi")
      // List, Set, Map, Option, Tuple
      val myOpt:Option[Int] = Some(5)  // 这种类型的值可能为 None
      val myMap = Map("one" -> 1, "two" -> 2, "three" -> 3)
      println(myMap.get("one"))  // Some(1)
      def showMap(x: Option[String]) = x match {
        case Some(s) => s
        case None => "?"
      }
      val myList = List(1, 2, 3, 4, 5, 6)
      var z = new Array[String](3)
      var x = Array("test", "1")   // ???
      var y = concat(x, z)
      var myMatrix = ofDim[Int](3,3)
      // 创建矩阵
      for (i <- 0 to 2) {
        for ( j <- 0 to 2) {
          myMatrix(i)(j) = j
        }
      }
      // 打印二维阵列
      for (i <- 0 to 2) {
        for ( j <- 0 to 2) {
          print(" " + myMatrix(i)(j))
        }
        println()
      }

      if(myInt>99){
        println(herInt)
      }else{
        println(myStr)
      }
      // for 循环, filter
      var a = 0
      for( a <- 1 to 10
           if a != 3; if a < 8){
        println( "Value of a: " + a)
        // 1-->10
        // (a <- 1 until 10)  1-->9
      }
      var mySet = for{ a <- myList if a != 3; if a < 8
      } yield a

      println(mySet)
      // format
      printf("multiplier(1) -> %d", Closure.multiplier(1))
}

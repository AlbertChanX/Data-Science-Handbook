package ex

class Point(xc: Int, yc: Int) {
  var x: Int = xc
  var y: Int = yc

  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
    println ("x 的坐标点: " + x)
    println ("y 的坐标点: " + y)
  }
}
/*
extends
1、重写一个非抽象方法必须使用override修饰符。
2、只有主构造函数才可以往基类的构造函数里写参数。
3、在子类中重写超类的抽象方法时，你不需要使用override关键字。
*/

class Location(xc: Int, yc: Int,
               val zc :Int) extends Point(xc, yc){
  override var x = xc
  override var y = yc
  var z: Int = zc

  def move(dx: Int, dy: Int, dz: Int) {
    x = x + dx
    y = y + dy
    z = z + dz
    println ("x 的坐标点 : " + x);
    println ("y 的坐标点 : " + y);
    println ("z 的坐标点 : " + z);
  }
}

object Test {
  def main(args: Array[String]) {
    //val pt = new Point(10, 20);

    // 移到一个新的位置
    // pt.move(10, 10);
    val loc = new Location(10, 20, 15);

    // 移到一个新的位置
    loc.move(10, 10, 5);
  }
}
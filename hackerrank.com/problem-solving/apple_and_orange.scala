//www.hackerrank.com/challenges/apple-and-orange/problem

import java.util.Scanner
import scala.io.StdIn._

object Solution {

  def countApplesAndOranges2(s: Int, t: Int, a: Int, b: Int,
      apples: Array[Int], oranges: Array[Int]): Unit = {
        println(apples.count(x => x + a >= s && x + a <= t))
        println(oranges.count(x => x + b >= s && x + b <= t))
  }

  def countApplesAndOranges(s: Int, t: Int, a: Int, b: Int,
      apples: Array[Int], oranges: Array[Int]): Unit = {
        println(apples.map(a + _).count(x => x >= s && x <= t).size)
        println(oranges.map(b + _).count(x => x >= s && x <= t))
  }

  def main(args: Array[String]) {
    val sc = new Scanner(System.in)
    val s = sc.nextInt()
    val t = sc.nextInt()
    val a = sc.nextInt()
    val b = sc.nextInt()
    val m = sc.nextInt()
    val n = sc.nextInt()
    val apples = (0 until m).map(_ => sc.nextInt()).toArray
    val oranges = (0 until n).map(_ => sc.nextInt()).toArray
    countApplesAndOranges(s, t, a, b, apples, oranges)

  }
}
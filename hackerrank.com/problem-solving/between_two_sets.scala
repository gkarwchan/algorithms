// https://www.hackerrank.com/challenges/between-two-sets/problem

import scala.io.StdIn._

object Solution {

// *******************************************************************
  def gcd(a: Int, b: Int): Int = {
    if (b == 0) a else gcd(b, a%b)
  }

  def lcm(a: Int, b: Int): Int = {
    ((a * b) / gcd(a, b)).toInt
  }

  def getTotalX(a: Array[Int], b: Array[Int]): Int = {
      val lcm_a = a.reduce((x, y) => lcm(x, y))
      val gcd_b = b.reduce((x, y) => gcd(x, y))
      (1 until (gcd_b / lcm_a).toInt + 1)
        .map(x => if (gcd_b % (lcm_a * x) == 0) 1 else 0).sum
  }
  
// ******************************************************************

  def getTotalX2(a: Array[Int], b: Array[Int]): Int = {
      (a.last to b.head).map(i => a.forall(x => i % x == 0) && b.forall(x => x % i == 0)).count(_ == true)
  }

// *******************************************************************
  def main(args: Array[String]) {
    val nm = readLine.split(" ").map(_.trim.toInt)
    val a = readLine.split(" ").map(_.trim.toInt)
    val b = readLine.split(" ").map(_.trim.toInt)
    println(getTotalX(a, b))
  }
}
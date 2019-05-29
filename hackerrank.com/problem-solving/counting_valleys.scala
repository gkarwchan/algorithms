https://www.hackerrank.com/challenges/counting-valleys/problem

import scala.io.StdIn._

object Solution {
  
  def countingValleys(n: Int, s: String): Int = {
    val a = s.split("").map(x => if (x == "U") 1 else -1)
    a.scanLeft(0)(_ + _).sliding(2).map(x => if (x(0) == -1 && x(1) == 0) 1 else 0).sum
  }


  def main(args: Array[String]) {
    val n = readInt
    val s = readLine
    println(countingValleys(n,s))
  }
}
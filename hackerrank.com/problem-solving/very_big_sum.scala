// https://www.hackerrank.com/challenges/a-very-big-sum/problem

import scala.io.StdIn._

object Solution {
  def main(args: Array[String]) {
    val n = readInt
    val a = readLine.split(" ").take(n).map(_.trim.toLong)
    println(a.sum)
  }
}
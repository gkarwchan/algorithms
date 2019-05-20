// https://www.hackerrank.com/challenges/kangaroo/problem

import scala.io.StdIn._

object Solution {

  def kangaroo(x1: Int, v1: Int, x2: Int, v2: Int): String = {
        if (v2 >= v1) return "NO"
        val rem = (x2 - x1) % (v1 - v2)
        return if (rem == 0) "YES" else "NO"
  }

  def main(args: Array[String]) {
    val ar = readLine.split(" ").map(_.trim.toInt)
    println(kangaroo(ar(0),ar(1), ar(2), ar(3)))
  }
}
// https://www.hackerrank.com/challenges/diagonal-difference/problem

import scala.io.StdIn._

object Solution {
  def main(args: Array[String]) {
    val n = readInt
    var ax1, ax2 = 0
    for (i <- 0 until n) {
      val values = readLine.split(" ").map(_.trim.toInt)
      ax1 += values(i)
      ax2 += values(n - i - 1)
    }

    println(Math.abs(ax1 - ax2))
  }
}

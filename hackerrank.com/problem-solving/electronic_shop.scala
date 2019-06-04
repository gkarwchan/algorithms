// https://www.hackerrank.com/challenges/electronics-shop/problem

import scala.io.StdIn._

object Solution {
  
  def getMoneySpent(keyboards: Array[Int], drives: Array[Int], b: Int): Int = {
    val prices = for (k <- keyboards; d <- drives) yield k + d
    val filtered = prices.filter(_ <= b)
    if (filtered.isEmpty) -1 else filtered.max
  }


  def main(args: Array[String]) {
    // val n = readInt
    val bnm = readLine.split(" ").map(_.trim.toInt)
    val keyboards = readLine.split(" ").map(_.trim.toInt)
    val drives = readLine.split(" ").map(_.trim.toInt)
    println(getMoneySpent(keyboards, drives, bnm(0)))
  }
}
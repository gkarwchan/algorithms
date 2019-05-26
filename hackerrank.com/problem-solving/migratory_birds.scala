// https://www.hackerrank.com/challenges/migratory-birds/problem

import scala.io.StdIn._


object Solution {
  

  def migratoryBirds(ar: Array[Int]): Int = {
    var c = Array.fill[Int](5)(0)
    for (i <- ar) {
      c(i-1) += 1
    }
    val max = c.reduce((a, b) => math.max(a, b))
    c.indexOf(max) + 1
  }

  def main(args: Array[String]) {
    val n = readLine.trim.toInt
    val ar = readLine.split(" ").map(_.trim.toInt)
    println(migratoryBirds(ar))
  }
}
// https://www.hackerrank.com/challenges/staircase/problem

import scala.io.StdIn._

object Solution {
  
  def staircase(n: Int): Unit = {
    for (i <- 1 to n) {
      println(("#" * i).padTo(n, ' ').reverse)
    }
  }
  
  def main(args: Array[String]) {

    val n = readInt
    staircase(n)
  }
}
// https://www.hackerrank.com/challenges/mini-max-sum/problem

import scala.io.StdIn._

object Solution {
  
  def miniMaxSum(arr: Array[Long]): Unit = {
    var ar = arr.sorted
    val min = ar.take(4).sum
    val max = ar.drop(1).sum
    println(min + " " + max)
  }
  
  def main(args: Array[String]) {

    val n = readLine.split(" ").map(_.trim.toLong)
    miniMaxSum(n)
  }
}
// https://www.hackerrank.com/challenges/sock-merchant/problem

import scala.io.StdIn._

object Solution {
  
  def sockMerchant(n: Int, ar: Array[Int]): Int = {
    return ar.distinct.map(i => ar.count(_ == i) / 2).sum
  }

  def sockMerchant1(n: Int, ar: Array[Int]): Int = {
    ar.groupBy(identity).mapValues(_.length / 2).values.sum
  }


  def main(args: Array[String]) {
    val n = readInt
    val ar = readLine.split(" ").map(_.trim.toInt)
    println(sockMerchant(n,ar))
  }
}
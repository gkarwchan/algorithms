// # https://www.hackerrank.com/challenges/birthday-cake-candles/problem


import scala.io.StdIn._

object Solution {

  def birthdayCakeCandles(ar: Array[Int]): Int = {
    val tallest = ar.max
    ar.count(x => x == tallest)
  }

  def birthdayCakeCandles2(ar: Array[Int]): Int = {
    ar.groupBy(identity).map(t => (t._1, t._2.length)).maxBy(_._1)._2
  }

  def birthdayCakeCandles3(ar: Array[Int]): Int = {
    ar.groupBy(identity).maxBy(_._1)._2.length
  }

  def birthdayCakeCandles4(ar: Array[Int]): Int = {
    val tallest = ar.reduceLeft(_ max _)
    ar.filter(_ == tallest).length
  }

  def main(args: Array[String]) {
    val n = readInt
    val ar = readLine.split(" ").map(_.trim.toInt)
    println(birthdayCakeCandles3(ar))
    
  }
}
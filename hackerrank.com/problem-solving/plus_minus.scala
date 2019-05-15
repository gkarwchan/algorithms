// https://www.hackerrank.com/challenges/plus-minus/problem

import scala.io.StdIn._

object Solution {

  def plusMinus(arr: Array[Int]) {
    val neg = arr.filter(_ < 0).length.toFloat
    val pos = arr.filter(_ > 0).length.toFloat
    val zer = arr.filter(_ == 0).length.toFloat

    println("%.6f".format(pos / arr.length))
    println("%.6f".format(neg / arr.length))
    println("%.6f".format(zer / arr.length))
  }

  def plusMinus1(arr: Array[Int]) {
    var pos: Double = 0
    var neg: Double = 0
    var zer: Double = 0

    for(i <- arr) {
      if (i < 0)
        neg += 1
      else if (i > 0)
        pos += 1
      else
        zer += 1
    }

    println("%.6f".format(pos / arr.length))
    println("%.6f".format(neg / arr.length))
    println("%.6f".format(zer / arr.length))
  }

  def main(args: Array[String]) {
    val n = readInt
    val values = readLine.split(" ").map(_.trim.toInt)
    plusMinus(values)
    
  }
}
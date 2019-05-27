// https://www.hackerrank.com/challenges/bon-appetit/problem

import scala.io.StdIn._

object Solution {
  
  def bonAppetit(bill: Array[Int], k: Int, b: Int) {
    val owning = b - (bill.sum - bill(k)) / 2
    println(if (owning == 0) "Bon Appetit" else owning)
  }


  def main(args: Array[String]) {
    val nk = readLine.split(" ").map(_.trim.toInt)
    val bill = readLine.split(" ").map(_.trim.toInt)
    val b = readInt
    bonAppetit(bill, nk(1), b)
  }
}
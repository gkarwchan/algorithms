// https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

import scala.io.StdIn._


object Solution {
  

  def divisibleSumPairs(n: Int, k: Int, ar: Array[Int]): Int = {
    var res: Array[Int] = Array.fill(k){0}
    for (i <- ar) {
      res(i%k) += 1
    }
    var acc = 0
    for (i <- 1 to Math.floor((k - 1) / 2).toInt) {
      acc += res(i) * res(k - i)
    }
    val selfItems = if (k % 2 == 0) Array(0, k / 2) else Array(0)
    for (i <- selfItems) {
      acc += res(i) * (res(i) - 1) / 2
    }
    acc
  }

  def main(args: Array[String]) {
    val nk = readLine.split(" ").map(_.trim.toInt)
    val ar = readLine.split(" ").map(_.trim.toInt)
    println(divisibleSumPairs(nk(0), nk(1), ar))
  }
}
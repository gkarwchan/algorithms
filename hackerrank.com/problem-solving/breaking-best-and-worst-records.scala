
// https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import scala.io.StdIn._

object Solution {
  
  def breakingRecords(scores: Array[Int]): Array[Int] = {
    var minBreak, maxBreak = 0
    var minScore, maxScore = scores(0)
    for (i <- scores) {
      if (i > maxScore) {
        maxScore = i
        maxBreak += 1
      } else if (i < minScore) {
        minScore = i
        minBreak  += 1
      }
    }
    return Array(maxBreak, minBreak)
  }
  

  def breakingRecords2(scores: Array[Int]): Array[Int] = {
    val rec = scores.tail.foldLeft((scores.head, 0, scores.head, 0)) {
      (r, score) =>
        if (score > r._1) (score, r._2 + 1, r._3, r._4)
        else if (score < r._3) (r._1, r._2, score, r._4 + 1)
        else r
    }
    Array(rec._2, rec._4)
  }

  def main(args: Array[String]) {
    val n = readInt
    val ar = readLine.split(" ").take(n).map(_.trim.toInt)
    val o = breakingRecords(ar)
    println(o.mkString(" "))
  }
}
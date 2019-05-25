// https://www.hackerrank.com/challenges/the-birthday-bar/problem
import scala.io.StdIn._

object Solution {
  
  def birthday(nums: Array[Int], d: Int, m: Int): Int = {
    var ways = 0
    for (i <- 0 to nums.size - m) {
      val value = nums.slice(i, i + m).sum
      ways += (if (value == d) 1 else 0)
    }
    ways
  }

  def birthday(nums: Array[Int], d: Int, m: Int): Int = {
    nums.sliding(m).map(_.sum).filter(_ == d).size
  }
  
  
  def main(args: Array[String]) {
    val n = readInt
    val ar = readLine.split(" ").take(n).map(_.trim.toInt)
    val dm = readLine.split(" ").map(_.trim.toInt)
    val o = birthday(ar, dm(0), dm(1))
    println(o)
  }
}
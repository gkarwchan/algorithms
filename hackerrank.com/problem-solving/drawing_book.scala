// https://www.hackerrank.com/challenges/drawing-book/problem
import scala.io.StdIn._

object Solution {
  
  def pageCount(n: Int, p: Int): Int = {
    math.min(p/2, n/2 - p/2)
  }


  def main(args: Array[String]) {
    val n = readInt
    val p = readInt

    println(pageCount(n,p))
  }
}
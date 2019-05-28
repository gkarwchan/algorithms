
// https://www.hackerrank.com/challenges/time-conversion/problem

import scala.io.StdIn._

object Solution {

  def timeConversion(s: String): String = {
    var hour = s.substring(0, 2).toInt
    val remain = s.drop(2).dropRight(2)
    if (s.endsWith("PM")) {
      if (hour != 12) {
        hour = hour + 12
      }
    } else {
      if (hour == 12) {
        hour = 0
      }
    }
    s"%02d$remain".format(hour)
  }

  def main(args: Array[String]) {
    val s = readLine
    
    println(timeConversion(s))
  }
}

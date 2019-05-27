// https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import scala.io.StdIn._

object Solution {
  

  def dayOfProgrammer(year: Int): String = {
    if (year == 1918) {
      return "26.09.1918"
    }
    if (year % 4 == 0 && ((year % 100 != 0) || year % 400 == 0 || year < 1918)) {
      return "12.09.%d".format(year)
    }
    return "13.09.%d".format(year)
  }

  def dayOfProgrammer1(year: Int): String = {
    val leapYearDate = s"12.09.$year"
    val nonLeapYearDate = s"13.09.$year"

    year match {
      case 1918 => "26.09.1918"
      case _ if year < 1918 => if (year % 4 == 0) leapYearDate else nonLeapYearDate
      case _ => if (year % 400 == 0 || (year % 4 == 0 && !(year % 100 == 0))) leapYearDate else nonLeapYearDate
    }
  }

  def main(args: Array[String]) {
    val year = readLine.trim.toInt
    println(dayOfProgrammer(year))
  }
}
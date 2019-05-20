// https://www.hackerrank.com/challenges/grading/problem
import scala.io.StdIn._

object Solution {

  def gradingStudents(grades: Array[Int]): Array[Int] = {
    grades.map(i => if (i < 38 || i % 5 < 3) i else i + 5 - i % 5)
  }

  def main(args: Array[String]) {
    val n = readInt
    val grades = for (i <- 0 until n) yield readInt
    val newGrades = gradingStudents(grades.toArray)
    println(newGrades.mkString("\n"))
  }
}
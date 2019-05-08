object Solution {

  def solve(meal_cost: Double, tip_percent: Int, tax_percent: Int) {
    var tip = meal_cost * tip_percent / 100
    var tax = meal_cost * tax_percent / 100
    var totalCost = meal_cost + tip + tax
    println(f"$totalCost%1.0f")
  }

  def main (args: Array[String]) {
    val stdin = scala.io.StdIn
    val meal_cost = scala.io.StdIn.readLine.trim.toDouble
    val tip_percent = scala.io.StdIn.readLine.trim.toInt
    val tax_percent = scala.io.StdIn.readLine.trim.toInt
    solve(meal_cost, tip_percent, tax_percent)

  }
}
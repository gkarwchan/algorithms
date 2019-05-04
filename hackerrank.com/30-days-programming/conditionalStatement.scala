object ConditionalStatement {

  def main (args: Array[String]) {
    val N = scala.io.StdIn.readLine.trim.toInt
    if (N % 2 != 0) {
      println("Weird")
    } else if ((N >= 2 && N < 5) || (N > 20)) {
      println("Not Weird")
    } else {
      println("Weird")
    }

  }
}

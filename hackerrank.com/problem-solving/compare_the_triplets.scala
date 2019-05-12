// https://www.hackerrank.com/challenges/compare-the-triplets/problem

object Solution extends App {
  val a = StdIn.readLine.split(" ").map(_.trim.toInt)
  val b = StdIn.readLine.split(" ").map(_.trim.toInt)

  val total = a.zip(b).fold((0,0)){ case (acc, pair) =>
    if(pair._1 > pair._2)
      (acc._1+1, acc._2)
    else if(pair._1 < pair._2)
      (acc._1, acc._2+1)
    else
      acc
  }
  println(s"${total._1} ${total._2}")
}
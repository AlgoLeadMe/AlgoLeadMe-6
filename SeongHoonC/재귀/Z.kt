import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

var count = 0

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, r, c) = br.readLine().split(" ").map { it.toInt() }
    program(n, 0, 0, r, c)
}

private fun program(n: Int, x: Int, y: Int, r: Int, c: Int) {
    val additionRange = 2.pow(n)
    if (r !in x until x + additionRange || c !in y until y + additionRange) {
        count += additionRange * additionRange
        return
    }
    if (n == 0) {
        if (x == r && y == c) {
            println(count)
            return
        }
        count++
        return
    }
    val additionIndex = 2.pow(n - 1)
    program(n - 1, x, y, r, c)
    program(n - 1, x, y + additionIndex, r, c)
    program(n - 1, x + additionIndex, y, r, c)
    program(n - 1, x + additionIndex, y + additionIndex, r, c)
}

private fun Int.pow(n: Int) = this.toDouble().pow(n).toInt()

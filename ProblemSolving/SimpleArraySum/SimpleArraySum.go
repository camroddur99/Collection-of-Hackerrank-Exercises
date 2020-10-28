package main
import "fmt"

func main(){
	var a, arr, sum int
	fmt.Scan(&a)
	for i := 0; i <= a - 1; i++{
		fmt.Scan(&arr)
		sum += arr
	}
	fmt.Println(sum)  
}
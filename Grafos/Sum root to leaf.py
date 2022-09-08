/**
 * Definition for a binary tree node.
 * type Nodo struct {
 *     Val int
 *     izquierda *Nodo
 *     derecha *Nodo
 * }
 */
 func sumNumbers(raiz *Nodo) int {
     if raiz==nil{return 0}
     numerosCaminos = make([]string, 0)
     dfs(raiz, "")
     total:=0
     for _, n:= range numerosCaminos{
         tmp, _ := strconv.Atoi(n)
         total += tmp
     }
     return total
 }
 var numerosCaminos []string
 func dfs(raiz *Nodo, str string) {
     if raiz.izquierda==nil && raiz.derecha==nil{
         numerosCaminos=append(numerosCaminos, str + strconv.Itoa(raiz.Val))return}
     if raiz.izquierda!=nil{
         dfs(raiz.izquierda, str + strconv.Itoa(raiz.Val))}
     if raiz.derecha!=nil{
         dfs(raiz.derecha, str + strconv.Itoa(raiz.Val))
     }
 }
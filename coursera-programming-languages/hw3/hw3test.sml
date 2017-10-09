(* Homework3 Simple Test*)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)
use "hw3.sml";

val test1 = only_capitals ["A","B","C"] = ["A","B","C"]
val test1_1 = only_capitals ["Abbbb","ccc","Dddd"] = ["Abbbb","Dddd"]

val test2 = longest_string1 ["A","bc","C"] = "bc"
val test2_1 = longest_string1 ["Ac","bc","C"] = "Ac"
val test2_2 = longest_string1 [] = ""

val test3 = longest_string2 ["A","bc","C"] = "bc"
val test3_1 = longest_string2 ["Ac","bc","C"] = "bc"
val test3_2 = longest_string2 [] = ""

val test4a = longest_string3 ["A","bc","C"] = "bc"
val test4a_1 = longest_string3 ["Ac","bc","C"] = "Ac"
val test4a_2 = longest_string3 [] = ""

val test4b = longest_string4 ["A","B","C"] = "C"
val test4b_1 = longest_string4 ["Ac","bc","C"] = "bc"
val test4b_2 = longest_string4 [] = ""

val test5 = longest_capitalized ["A","bc","C"] = "A"

val test6 = rev_string "abc" = "cba"
val test6_1 = rev_string "1234#" = "#4321"
val test6_2 = rev_string "" = ""

val test7 = first_answer (fn x => if x > 3 then SOME x else NONE) [1,2,3,4,5] = 4
val test7_1 = (first_answer (fn x => if x > 3 then SOME x else NONE) [1,2,3,2,1]; false) handle NoAnswer => true
val test7_2 = (first_answer (fn x => if x > 3 then SOME x else NONE) []; false) handle NoAnswer => true

val test8 = all_answers (fn x => if x = 1 then SOME [x] else NONE) [2,3,4,5,6,7] = NONE
val test8_1 = all_answers (fn x => if x = 1 then SOME [x] else NONE) [] = SOME []
val test8_2 = all_answers (fn x => if x > 1 then SOME [x] else NONE) [2,3,4,5,6,7] =SOME [2,3,4,5,6,7]
val test8_3 = all_answers (fn x => if x = 1 then SOME [x] else NONE) [1,1,1,1,1,7] = NONE

val test9a = count_wildcards Wildcard = 1

val test9a_1 = count_wildcards (TupleP [Wildcard, Variable "hello", TupleP [Wildcard,Wildcard]]) = 3

val test9b = count_wild_and_variable_lengths (Variable("a")) = 1
val test9b_1 = count_wild_and_variable_lengths (TupleP [Wildcard, ConstructorP("oh", Variable "hello") , TupleP [Wildcard,Wildcard]]) = 8

val test9c = count_some_var ("x", Variable("x")) = 1
val test9c_1 = count_some_var ("hello", TupleP [Wildcard, Variable "hello", TupleP [Wildcard,Variable "hello"]]) = 2

val test10 = check_pat (Variable("x")) = true
val test10_1 = check_pat (TupleP [Wildcard, Variable "hello", TupleP [Wildcard,Variable "hello"]]) = false
val test10_2 = check_pat (TupleP [Wildcard, Variable "hello", TupleP [Wildcard,Variable "world"]]) = true
val test10_3 = check_pat (TupleP [Wildcard, ConstructorP("oh", Variable "hello") , TupleP [Wildcard,Wildcard]]) = true

val test11 = match (Const(1), UnitP) = NONE
val test11_1 = match (Const(1), Wildcard) = SOME []
val test11_2 = match (Const(1), ConstP(1)) = SOME []

val test11_3 = match ((Tuple [Unit, Constructor("oh", Const(1)) , Tuple [Const(2),Const(3)]]),  
                    (TupleP [Wildcard, ConstructorP("oh", Variable "v1") , TupleP [Variable "v2",Variable "v3"]])) 
                    = SOME[("v1", Const(1)), ("v2", Const(2)),("v3", Const(3))]

val test11_4 = match ((Tuple [Unit, Constructor("ho", Const(1)) , Tuple [Const(2),Const(3)]]),  
                    (TupleP [Wildcard, ConstructorP("oh", Variable "v1") , TupleP [Variable "v2",Variable "v3"]])) 
                    = NONE
val test12 = first_match Unit [UnitP] = SOME []
val test12_1 = first_match Unit [Variable "hello", Variable "world"] = SOME [("hello", Unit)]

val test12_2 = first_match (Constructor("egg",Const 4)) [ConstP 4] = NONE
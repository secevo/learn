(* Homework2 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)
use "hw2.sml";

val test1 = all_except_option ("string", ["string"]) = SOME []
val test1_1 = all_except_option ("string", ["hello","string","world"]) = SOME (["hello","world"])
val test1_2 = all_except_option ("string", ["hello"]) = NONE
val test1_3 = all_except_option ("string", []) = NONE

val test2 = get_substitutions1 ([["foo"],["there"]], "foo") = []
val test2_1 = get_substitutions1 ([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],"Fred") = ["Fredrick","Freddie","F"]
val test2_2 = get_substitutions1 ([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]],"Jeff") = ["Jeffrey","Geoff","Jeffrey"]

val test3 = get_substitutions2 ([["foo"],["there"]], "foo") = []
val test3_1 = get_substitutions2 ([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],"Fred") = ["Fredrick","Freddie","F"]
val test3_2 = get_substitutions2 ([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]],"Jeff") = ["Jeffrey","Geoff","Jeffrey"]

val test4 = similar_names ([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], {first="Fred", middle="W", last="Smith"}) =
	    [{first="Fred", last="Smith", middle="W"}, {first="Fredrick", last="Smith", middle="W"},
	     {first="Freddie", last="Smith", middle="W"}, {first="F", last="Smith", middle="W"}]

val test5 = card_color (Clubs, Num 2) = Black
val test5_1 = card_color (Diamonds, Num 2) = Red
val test5_2 = card_color (Spades, King) = Black
val test5_3 = card_color (Hearts, Num 2) = Red
val test5_4 = card_color (Hearts, King) = Red

val test6 = card_value (Clubs, Num 2) = 2
val test6_1 = card_value (Clubs, Ace) = 11
val test6_2 = card_value (Clubs, Jack) = 10
val test6_3 = card_value (Clubs, Queen) = 10
val test6_4 = card_value (Clubs, King) = 10

val test7 = remove_card ([(Hearts, Ace)], (Hearts, Ace), IllegalMove) = []
val test7_1 = remove_card ([(Hearts, Ace),(Hearts, Ace)], (Hearts, Ace), IllegalMove) = [(Hearts, Ace)]
val test7_2 = remove_card ([], (Hearts, Ace), IllegalMove) = [] handle IllegalMove => true
val test7_3 = remove_card ([(Clubs, Num 2),(Hearts, Ace)], (Hearts, Ace), IllegalMove) = [(Clubs, Num 2)]
val test8 = all_same_color [(Hearts, Ace), (Hearts, Ace)] = true
val test8_1 = all_same_color [] = true
val test8_2 = all_same_color [(Hearts, Ace)] = true
val test8_3 = all_same_color [(Hearts, Ace),(Spades, Num 3),(Hearts, Num 4), (Hearts, Ace)] = false
val test8_4 = all_same_color [(Hearts, Ace),(Hearts, Num 3),(Hearts, Num 4), (Diamonds, Ace)] = true

val test9 = sum_cards [(Clubs, Num 2),(Clubs, Num 2)] = 4
val test9_1 = sum_cards [(Hearts, Num 2),(Clubs, Ace), (Spades, King)] = 23

val test10 = score ([(Hearts, Num 2),(Clubs, Num 4)],10) = 4
val test10_1 = score ([(Hearts, Num 2),(Clubs, Num 8)],10) = 0
val test10_2 = score ([(Hearts, Num 2),(Clubs, Ace)],10) = 9
val test10_3 = score ([(Hearts, Num 2),(Diamonds, Ace)],10) = 4
val test10_4 = score ([(Hearts, Num 2),(Diamonds, Num 3)],10) = 2
val test10_5 = score ([(Hearts, Num 2),(Diamonds, Num 3)],9) = 2
val test10_6 = score ([],9) = 4

val test11 = officiate ([(Hearts, Num 2),(Clubs, Num 4)],[Draw], 15) = 6

val test11_1 = officiate ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                        [Draw,Draw,Draw,Draw,Draw],
                        42)
             = 3

val test11_2 = ((officiate([(Clubs,Jack),(Spades,Num(8))],
                         [Draw,Discard(Hearts,Jack)],
                         42);
               false) 
              handle IllegalMove => true)

val test11_3 = officiate ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                        [Draw,Draw,Draw,Draw,Draw],
                        45)
             = 0

val test11_4 = officiate ([(Hearts, Num 2),(Clubs, Num 4)],[Draw, Draw], 15) = 9
val test11_5 = officiate ([(Hearts, Num 2),(Clubs, Num 4)],[Draw, Draw, Draw], 15) = 9

val test11_6 = officiate([(Clubs,Jack),(Spades,Num(8))],
                         [Draw,Discard(Clubs,Jack)],
                         42)
              = 21

val test11_7 = officiate ([(Hearts, Num 5),(Diamonds, Ace), (Clubs, Num 4)],[Draw, Draw, Draw], 7) = 13
val test11_8 = officiate ([(Clubs, Num 5),(Diamonds, Ace), (Clubs, Num 4)],[Draw, Draw, Draw], 7) = 27

(*val test12 = score_challenge ([(Hearts, Ace),(Clubs, Num 4)],5) = 0
val test12_1 = score_challenge ([(Hearts, Ace),(Clubs, Num 4)],15) = 0
val test12_2 = score_challenge ([(Hearts, Num 2),(Clubs, Ace)],10) = 9
val test12_3 = score_challenge ([(Hearts, Num 2),(Diamonds, Ace)],10) = 4
val test12_4 = score_challenge ([(Hearts, Ace),(Hearts, Ace),(Clubs, Num 4)],6) = 0
val test12_5 = score_challenge ([(Hearts, Ace),(Hearts, Ace),(Clubs, Num 4)],16) = 0
val test12_6 = score_challenge ([(Hearts, Ace),(Hearts, Ace),(Clubs, Num 4)],26) = 0
val test12_7 = score_challenge ([(Hearts, Ace),(Hearts, Ace),(Clubs, Num 4)],21) = 5
val test12_8 = score_challenge ([(Hearts, Ace),(Hearts, Ace),(Clubs, Num 4)],23) = 6*)
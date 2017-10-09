(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
fun all_except_option(str, strList) = 
    case strList of
            [] => NONE
        |    head :: tail => if same_string(head, str)
                                then SOME(tail)
                                else case all_except_option(str, tail)  of
                                    NONE =>  NONE
                                |   SOME strList' => SOME(head::strList')

fun get_substitutions1(lls, s) = 
    case lls of
        [] => []
    | head::tail => case all_except_option(s, head) of 
                        NONE => get_substitutions1(tail, s)
                    |   SOME strList => strList@get_substitutions1(tail, s)

fun get_substitutions2(lls, s) = 
    let fun f (lls, s, acc) = 
        case lls of
        [] => acc
        | head::tail => case all_except_option(s, head) of 
                        NONE => f(tail, s, acc)
                    |   SOME strList => f(tail, s, acc@strList)
    in
        f(lls, s, [])
    end

fun similar_names(lls, {first=x,middle=y,last=z}) =
    let fun build(ls) = 
        case ls of
            [] => []
        |   head::tail => {first=head,middle=y,last=z}::build(tail)
    in
        build(x::get_substitutions2(lls,x))
    end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color(a_card) = 
    case a_card of 
        (Clubs, _) => Black
    |   (Diamonds, _) => Red
    |   (Hearts, _) => Red
    |   (Spades, _) => Black

fun card_value(a_card) = 
    case a_card of 
       (_, Ace) => 11
    |   (_, Num num) => num
    |   (_, _) => 10

fun remove_card(cs, c, e) = 
    case cs of  
        [] => raise e
    |   head::tail => if head=c then tail else head::remove_card(tail,c,e)

fun all_same_color(cs) =
    case cs of 
        [] => true
    |   _::[] => true
    |   head::(nech::tail) => card_color(head)=card_color(nech) andalso all_same_color(nech::tail)

fun sum_cards(cs) = 
    let fun f(cs, acc) =
        case cs of 
            [] => acc
        |   head::tail => f(tail, card_value(head) + acc)
    in
        f(cs, 0)
    end

fun score(cs, goal) = 
    let 
        val difference  = sum_cards(cs) - goal
        val preliminary_score = if difference <=0 then ~difference else 3 * difference
    in 
        if all_same_color(cs) then preliminary_score div 2 else preliminary_score
    end

fun officiate(card_list, move_list, goal) =
    let fun f(card_list, held_list, move_list) =
        case (card_list, held_list, move_list) of
            (_,held_list,[]) => score(held_list, goal)
        |   (card_list, held_list, Discard c::tail) => f(card_list, remove_card(held_list, c, IllegalMove), tail)
        |   ([],held_list,Draw::tail) => score(held_list, goal)
        |   (cs_head::cs_tail, held_list, Draw::tail) => 
                if sum_cards(cs_head::held_list) > goal
                then score(cs_head::held_list, goal)
                else f(cs_tail, cs_head::held_list, tail)
    in
        f(card_list, [], move_list)
    end
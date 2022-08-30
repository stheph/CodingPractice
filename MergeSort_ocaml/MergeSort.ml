let rec merge l1 l2 =
  begin
    match l1, l2 with
    | [], [] -> []
    | l, [] -> l
    | [], l -> l
    | x::xs, y::ys ->
      if x < y
      then x::(merge xs (y::ys))
      else y::(merge (x::xs) ys)
  end

let rec split l =
  begin
    match l with
    | [] -> ([], [])
    | [x] -> ([x], [])
    | hd::tl ->
        let (l1, l2) = split tl in
        (* flipping the order should alternate elements *)
        (hd::l2, l1)
  end

let (l1, l2) = split [1;2;3;4;5;6;7;8;9]
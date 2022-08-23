exception Not_found

type 'a bst = Nil | Node of int * 'a * 'a bst * 'a bst

let rec search t key = begin
  match t with
  | Nil -> raise Not_found
  | Node (k, d, l, r) ->
    if key == k
    then d
    else
      if key < k
      then search l key
      else search r key
end

let rec insert t key data = begin match t with
  | Nil -> Node (key, data, Nil, Nil)
  | Node (key', data', left, right) ->
      if key < key'
      then Node (key', data', insert left key data, right)
      else Node (key', data', left, insert right key data)
    end

let rec inorder t =
  begin
    match t with
    | Nil -> []
    | Node (k, d, l, r) ->
    inorder l @ [(k, d)] @ inorder r
  end

let rec tree_of_list l =
  begin
    match l with
    | [] -> Nil
    | (k, d)::tl ->
    insert (tree_of_list tl) k d
  end

let test = tree_of_list [(12, "a");(5, "b");(17, "c");(1, "d");(3, "e");(2, "f")]
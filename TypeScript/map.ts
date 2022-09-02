function map<A, B>(l: A[], f: (x : A) => B) : B[]
{
    if (l.length == 0)
    {
        return [];
    }
    else
    {
        let [head, ...tail] = l;
        return [f(head), ...map(tail, f)];

    }
}

console.log(map([1,2,3,4,5], (x : number) : number => { return x + 1}))
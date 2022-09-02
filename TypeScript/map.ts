function map (l: any[], f: (x : any) => any) : any[]
{
    if (l.length == 0)
    {
        return [];
    }
    else
    {
        let out : any[] = [f(l[0])];
        out.push(...map(l.slice(1, l.length), f))
        return out;
    }
}

console.log(map([1,2,3,4,5], (x : number) : number => { return x + 1}))
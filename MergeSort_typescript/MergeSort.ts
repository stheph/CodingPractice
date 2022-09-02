function merge(l1: any[], l2: any[]) : any[]
{
    if ((l1.length == 0) && (l2.length == 0))
    {
        return [];
    }
    else if ((l1.length == 0))
    {
        return l2;
    }
    else if ((l2.length == 0))
    {
        return l1;
    }
    else
    {
        if (l1[0] < l2[0])
        {
            let merged : any[] = merge(l1.slice(1, l1.length), l2);
            let out : any[] = [l1[0]];
            out.push(...merged)
            return out
        }
        else
        {
            let merged : any[] = merge(l1, l2.slice(1, l2.length));
            let out : any[] = [l2[0]];
            out.push(...merged)
            return out
        }
    }
}

function split (l: any[]) : [any[], any[]] 
{
    let midpoint : number = Math.floor(l.length / 2);
    return [l.slice(0, midpoint), l.slice(midpoint, l.length)];
}

function mergesort (l: any[]) : any[]
{
    if ((l.length == 0) || (l.length == 1))
    {
        return l;
    }
    else
    {
        let [l1, l2] : [any[], any[]] = split(l)
        return merge(mergesort(l1), mergesort(l2))
    }
}

console.log(mergesort([1,8,3,6,9,3,2,2,3,8,0,6,4]))
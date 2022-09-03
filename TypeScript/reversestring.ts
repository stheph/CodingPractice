function reversestring(s : string) : string
{
    let out : string = "";
    for (let i = s.length - 1; i >= 0; i--)
    {
        out += s.charAt(i);
    }

    return out;
}

console.log(reversestring("testing"))
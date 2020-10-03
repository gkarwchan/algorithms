starRating=f=(x,i=5)=>i?"cxo"[x<1.5?x<.5|0:2]+f(x-2,i-1):""
starRating=x=>('o'.repeat((x+=.5)>>1)+['c'[~x&1]]).padEnd(5,'x')
starRating=f=(n,k=10)=>k?f(n,k-2)+"xco"[(k<n+.6)+(k<n+1.6)]:""
moonRating=r=>[2,4,6,8,10].map(x=>'xco'[(x<r+.6)+(x<r+1.6)]).join('')

[1.5,3.5,5.5,7.5]
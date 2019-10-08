function Secrets = rec8all(k,Keys,Shares)
Keys = gf(Keys,8)';
Shares = gf(Shares,8)';
V = gf(ones(k,k),8);
for p = 0:k-1
    V(:,p+1) = Keys.^p;
end
S = (V\Shares)';
Secrets = uint8(S.x);
end
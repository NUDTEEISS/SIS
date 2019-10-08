function reimg8(k,Keys)
tic
for i = 1:k 
    share{i} =  imread(['shares\share',num2str(Keys(i)),'.bmp']);
end
for i = 1:256
    for j = 1:256/k
        for p = 1:k
            Shares(p) = share{p}(i,j);
        end
        Secrets = rec8all(k,Keys,Shares);
        Simg(i,(j-1)*k+1:j*k) = Secrets;
    end
end
imwrite(Simg,'shares\recover.bmp');
toc
end

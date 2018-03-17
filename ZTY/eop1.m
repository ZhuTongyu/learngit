filename = 'test.txt';
a = importdata(filename);
b = a(1,:);
c = a(2,:);
% d = a(3,:);
% figure(1);
% plot(b,c);
% figure(2);
% plot(b,c);set(gca,'XDir','rev');//
e = b(1:2:end);
f = c(1:2:end);
plot(e,f);set(gca,'XDir','rev');

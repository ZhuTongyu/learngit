filename = 'test.txt';
a = importdata(filename);
b = a(1,:);
c = a(2,:);
figure(1);
plot(b,c);
figure(2);
plot(b,c);set(gca,'XDir','rev');

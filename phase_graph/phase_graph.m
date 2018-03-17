clc
clear variables;
filename = 'C:\Users\Tongyu\Desktop\spt_data\000_-569_LRR10_20180307 10-24-07.278.txt';
data = importdata(filename);
[filea,fileb] = size(data);
wide_b = find(data(:,2) == 22);
x = size(wide_b,1);
narrow_b = find(data(:,2) == 12);
y = size(narrow_b,1);
% a = wide_b(1);
% b= narrow_b(3);
% c= data(wide_b(1),11);
% d= data(wide_b(1),12);
% phase1= 180/pi*atan(d/c);
% phase2= 180/pi*atan(data(narrow_b(1),12)/data(narrow_b(1),11));
% phase3= 180/pi*atan(data(narrow_b(1),14)/data(narrow_b(1),13));
phase_1 = zeros(x,3);
phase_2 = zeros(x,3);
for loop = 1:x
    phase_1(loop,1) = 180/pi*atan(data(wide_b(loop),12)/data(wide_b(loop),11)) ...
                            -180/pi*atan(data(wide_b(loop),14)/data(wide_b(loop),13));
    phase_1(loop,2) = 180/pi*atan(data(wide_b(loop),14)/data(wide_b(loop),13)) ...
                            -180/pi*atan(data(wide_b(loop),16)/data(wide_b(loop),15));
    phase_1(loop,3) = 180/pi*atan(data(wide_b(loop),16)/data(wide_b(loop),15)) ...
                            -180/pi*atan(data(wide_b(loop),18)/data(wide_b(loop),17));                    
end
u = mean(phase_1);
for loop = 1:x
    phase_2(loop,1) = 180/pi*atan(data(wide_b(loop),12)/data(wide_b(loop),11));
                            
    phase_2(loop,2) = 180/pi*atan(data(wide_b(loop),14)/data(wide_b(loop),13));
                         
    phase_2(loop,3) = 180/pi*atan(data(wide_b(loop),16)/data(wide_b(loop),15));
    
    phase_2(loop,4) = 180/pi*atan(data(wide_b(loop),18)/data(wide_b(loop),17));
                                               
end
% phase1= 180/pi*atan(data(wide_b(2),12)/data(wide_b(2),11));
% phase2= 180/pi*atan(data(narrow_b(1),14)/data(narrow_b(1),13));
% phase3= 180/pi*atan(data(wide_b(1),16)/data(wide_b(1),15));
% phase4= 180/pi*atan(data(wide_b(1),18)/data(wide_b(1),17));
% 
% py1 = phase1-phase2;
% py2 = phase2-phase3;
% py3 = phase3-phase4;
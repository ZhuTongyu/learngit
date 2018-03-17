clc
clear variables;  %%  matlab 把矩阵输出excel表格 ， 通过excel完成矩阵数据调整，再用matlab绘制相位图
fileFolder = fullfile('C:\Users\TongYu\Desktop\spt_data');
dirOutput = dir(fullfile(fileFolder, '*.txt'));
filesname = {dirOutput.name}';
lengthFiles = length(dirOutput);

phase_wide = zeros(lengthFiles,4);
phase_narrow = zeros(lengthFiles,4);
for i = 1:lengthFiles
    data = importdata(strcat('C:\Users\Tongyu\Desktop\spt_data\',dirOutput(i).name));
    [filea,fileb] = size(data);
    
    wide_b = find(data(:,2) == 22);
    x = size(wide_b,1);
    
    narrow_b = find(data(:,2) == 12);
    y = size(narrow_b,1);
    

    phase_1 = zeros(x,3);  % 1 wide     
    phase_2 = zeros(y,3);  % 2 narrow
%     
%     phase_wide = zeros(lengthFiles,4);
%     phase_narrow = zeros(lengthFiles,4);
    
    for loop = 1:x
        phase_1(loop,1) = atan(data(wide_b(loop),12)/data(wide_b(loop),11)) ...
                                -atan(data(wide_b(loop),14)/data(wide_b(loop),13));
        phase_1(loop,2) = atan(data(wide_b(loop),14)/data(wide_b(loop),13)) ...
                                -atan(data(wide_b(loop),16)/data(wide_b(loop),15));
        phase_1(loop,3) = atan(data(wide_b(loop),16)/data(wide_b(loop),15)) ...
                                -atan(data(wide_b(loop),18)/data(wide_b(loop),17));                    
    end
    
    u = mean(phase_1);
    
    for loop = 1:y
        phase_2(loop,1) = atan(data(narrow_b(loop),12)/data(narrow_b(loop),11)) ...
                                -atan(data(narrow_b(loop),14)/data(narrow_b(loop),13));
        phase_2(loop,2) = atan(data(narrow_b(loop),14)/data(narrow_b(loop),13)) ...
                                -atan(data(narrow_b(loop),16)/data(narrow_b(loop),15));
        phase_2(loop,3) = atan(data(narrow_b(loop),16)/data(narrow_b(loop),15)) ...
                                -atan(data(narrow_b(loop),18)/data(narrow_b(loop),17));                               
    end  
    
    v = mean(phase_2);
    % 有没有更简便的操作
   phase_wide(i,:) = [i, u] ;
   phase_narrow(i,:) = [i, v];

end
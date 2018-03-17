clc
clear all;
fileFolder = fullfile('C:\Users\TongYu\Desktop\spt_data');
dirOutput = dir(fullfile(fileFolder, '*.txt'));
filesname = {dirOutput.name}';
lengthFiles = length(dirOutput);
a = dirOutput(1).name;

count_words = 0
count_ve = 0
count_de = 0
count_ki = 0
with open("myfile.txt", 'r') as f:
    for line in f:
        words = line.split()
        count_words += len(words)
        for i in range(0,len(words)):
            if(words[i]=='ki'):
                count_ki+=1;
            if(words[i]=='de'):
                count_de+=1
            if(words[i]=='ve'):
                count_ve+=1
print("Kelimeler :")                 
print(words)
print("kelime sayisi :")
print(count_words)
print("de sayisi :")
print(count_de)
print("ki sayisi :")
print(count_ki)
print("ve sayisi :")
print(count_ve)
input()
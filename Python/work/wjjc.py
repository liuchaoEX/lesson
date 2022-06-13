file = open('D:\\Code\\Python\\txt\\scores.txt', 'r', encoding='utf-8')#.txt文件和.py文件放在同一个文件夹
file_lines = file.readlines()
file.close()
final_scores = []
for i in file_lines:
    data =i.split()
    sum = 0
    for score in data[1:]:
        sum = sum + int(score)
        result = data[0]+str(sum)+'\n'
    final_scores.append(result)
r = open('result.txt','w',encoding='utf-8')
r.writelines(final_scores)
r.close()
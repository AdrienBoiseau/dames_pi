from Board import *

def update_list(list):
    for i in range(0,len(list)-3,2):
        if list[i]==list[i+2] and list[i+1]==list[i+3]:
            list[i+2]=''
            list[i+3]=''

    list2=[]
    for i in range(0, len(list), 2):
        if (not list[i] == '') or (not list[i + 1] == ''):
            list2+=list[i],list[i + 1]

    return list2

def write_list(list):
    for i in range(0,len(list),2):
        print('(',list[i],',',list[i+1],')')
    return


p=Board(10)

player=True
end=False


p.to_lines()





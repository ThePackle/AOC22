imp_list   = open('day1/input','r')
cal_list   = imp_list.read()
cal_groups = cal_list.split('\n\n')

elf_final = []
for elf_object in cal_groups:
    carried_cals = 0
    elf_cals = elf_object.split('\n')

    for elf_cal in elf_cals:
        if len(elf_cal) > 0:
            carried_cals += int(elf_cal)
    
    elf_final.append(carried_cals)

elf_final.sort()
elf_final.reverse()
elf_top3 = elf_final[0] + elf_final[1] + elf_final[2]
print ("MOST: {0}".format(elf_final[0]))
print ("TOP 3: {0}".format(elf_top3))
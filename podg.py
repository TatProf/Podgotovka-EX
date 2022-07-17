def surname(surnamee):
    # for i in range (len(surnamee)):   вариант1
    #     if i <= 4:
    #         print('*', end='')
    #     else:
    #         print(surnamee[i],end=' ')

    return  "*****" + surnamee[5:]          # вариант 2
print(surname('   мисенко'))
#surname('   мисенко'))
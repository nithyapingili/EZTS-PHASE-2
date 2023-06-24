#forest of 3 trees
Families={
    'Charley':{'Sam':{'Boxy','Roy'},
               'Nila':{'Pepsi'}},
    'Devi':{'Tommy':{'Tony'},
            'Timmy':{'Hamster'},
            'Tammy':{'Hamster'}},
    'Carlos':{'Diego':'Cat','Ferret':'Fox'}
    }
for Parent,Children in Families.items():
    print(f"{Parent}has{len(Children)}kids(s):")
    print(f"{',and'.join([str(Child)for Child in[*Children]])}")
    
            
    

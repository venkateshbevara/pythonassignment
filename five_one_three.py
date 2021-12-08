class five_one_three(data):
    d=five_one_three()
    def choice_m(choice):
        if(choice==1):
            entry()
        else:
            sys.exit()
    def entry():
        while(1):
           print("Enter the food item.enter none if that's all you have eaten")
           x=input()
           x=x.lower()
           if x=="none":
               break
           elif x in d.items:
               d.current_points+=1
               #calories=calories+items[x]
           elif x in non_items:
               d.current_points-=2
               #calories=calories+non_items[x]
           else:
               d.current_points-=1
               #calories=calories+100
           print("your currentpoints",current_points)
        result=current_points*10
        return result

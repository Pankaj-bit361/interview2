
employee=[
    {"name":"John","salary":3000,"designation":"developer"},
        {"name":"emma","salary":4000,"designation":"manager"},
            {"name":"kelly","salary":3500,"designation":"testor"}
]
max=0
val={}
for i in employee:

    if (i["salary"]>max):
        max=i["salary"]
        val=i
print(val)    

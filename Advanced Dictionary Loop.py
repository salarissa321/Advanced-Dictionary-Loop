


#----------------------------------------------------
#------------ Advanced Dictionary Loop---------
#-----------------------------------------------------


mySkills = {
    "Html" : "80%" ,
    "Css" : "20%" ,
    "Js" : "50%" ,
    "Php" : "70%"
}

# print(mySkills.items()) # dict_items([('Html', '80%'), ('Css', '20%'), ('Js', '50%'), ('Php', '70%')])

# for skill in mySkills :
#     # print(f"{skill}") # Html , Css , Js , Php
#     print(f"{skill} => {mySkills[skill]}") # Html => 80% # Css => 20% # Js => 50% # Php => 70% 



# for skill_key , skill_progress in mySkills.items() :
#     print(f"{skill_key} => {skill_progress}") # Html => 80% # Css => 20% # Js => 50% # Php => 70%  

myUltimateSkills = {
    "HTML" : {
        "Main" : "50%" ,
        "pugjs" : "60%"
    },
    "CSS" :{
        "Main" : "70%" ,
        "Sass" : "80"
    }
}

for main_key , main_value in myUltimateSkills.items() :
    # print(f"{main_key}") # HTML , CSS
    # print(f"{main_key} => {main_value}") # HTML => {'Main': '50%', 'pugjs': '60%'} # CSS => {'Main': '70%', 'Sass': '80'}
    print(f"{main_key} progress is :")
    for child_key , child_value in main_value.items() :
        print(f"- {child_key} => {child_value}") 

# HTML progress is :
#  Main => 50%
# - pugjs => 60%
# CSS progress is :
# - Main => 70%
# - Sass =>80




from flask import jsonify
import json
core_feel_list = {1:"Happy",2:"Sad",3:"Disgusted",4:"Angry",5:"Fearfull",6:"Bad",7:"Surprise"}
all_feels_list =   {
                    "Happy":{"Playfull":["Aroused","Cheeky"],"Content":["Free","Joyful"],"Interested":["Curious","Inquisitive"],"Proud":["Succesfull","Confident"],
                        "Accepted":["Respected","Valued"],"Powerful":["Courageous","Creative"],"Peaceful":["Loving","Thankful"],"Trusting":["Sensitive","Intimate"],
                        "Optimistic":["Hopeful","Inspired"]},
                    "Sad":{"Lonely":["Isolated","Abanadoned"],"Vulnerable":["Victimized","Fragile"],"Despair":["Grief","Powerless"],"Guilty":["Ashamed","Remorsefull"],"Depressed":{"Empty","Inferior"},
                        "Hurt":["Dissapointed","Embarrassed"]},
                    "Disgusted":{"Repelled":["Hesitant","Horrified"],"Awful":["Detestable","Nauseated"],"Dissapointed":["Revolted","Appalled"],"Disapproving":["Embarrased","judgmental"]},
                    "Angry":{"Critical":["Skeptical","Dismissive"],"Distant":["Numb","Withdrawn"],"Frustrated":["Annoyed","Infuriated"],"Aggressive":["Hostile","Provoked"],
                        "Mad":["Jealous","Furious"],"Bitter":["Violated","Indignant"],"Humillated":["Ridiculed","Disrespected"],"Let Down":["Resentful","Betrayed"]},
                    "Fearfull":{"Threatened":["Expose","Nervous"],"Rejected":["Persecuted","Excluded"],"Weak":["Insignificant","Worthless"],"Insecure":["Inferior","Inadequate"],
                        "Anxious":["Worried","Overwhelmed"],"Scared":["Frightened","Helpless"]},
                    "Bad":{"Bored":["Indifferent","Apathetic"],"Busy":["Pressured","Rushed"],"Stressed":["Overwhelmed---Repeats in fearfull","Out of Control"],"Tired":["Sleepy","Unfocussed"]},
                    "Surprise":{"Startled":["Shocked","Dismayed"],"Confused":["Disillusioned","Perplexed"],"Amazed":["Astonished","Awe"],"Excited":["Eager","Energetic"]}
                }


happy =   {
            "Playfull":["Aroused","Cheeky"],"Content":["Free","Joyful"],"Interested":["Curious","Inquisitive"],"Proud":["Succesfull","Confident"],
                "Accepted":["Respected","Valued"],"Powerful":["Courageous","Creative"],"Peaceful":["Loving","Thankful"],"Trusting":["Sensitive","Intimate"],
                "Optimistic":["Hopeful","Inspired"]
                }
                
sad =       {
            "Lonely":["Isolated","Abanadoned"],"Vulnerable":["Victimized","Fragile"],"Despair":["Grief","Powerless"],"Guilty":["Ashamed","Remorsefull"],"Depressed":{"Empty","Inferior"},
                "Hurt":["Dissapointed","Embarrassed"]
                }


Disgusted = {
            "Repelled":["Hesitant","Horrified"],"Awful":["Detestable","Nauseated"],"Dissapointed":["Revolted","Appalled"],
                "Disapproving":["Embarrased","judgmental"]
                }

Angry =     {
            "Critical":["Skeptical","Dismissive"],"Distant":["Numb","Withdrawn"],"Frustrated":["Annoyed","Infuriated"],"Aggressive":["Hostile","Provoked"],
                "Mad":["Jealous","Furious"],"Bitter":["Violated","Indignant"],"Humillated":["Ridiculed","Disrespected"],"Let Down":["Resentful","Betrayed"]
                }

Fearfull = {
            "Threatened":["Expose","Nervous"],"Rejected":["Persecuted","Excluded"],"Weak":["Insignificant","Worthless"],"Insecure":["Inferior","Inadequate"],
                "Anxious":["Worried","Overwhelmed"],"Scared":["Frightened","Helpless"]
                }

Bad =       {"Bored":["Indifferent","Apathetic"],"Busy":["Pressured","Rushed"],"Stressed":["Overwhelmed---Repeats in fearfull","Out of Control"],
            "Tired":["Sleepy","Unfocussed"]
                }

Surprise = {
            "Startled":["Shocked","Dismayed"],"Confused":["Disillusioned","Perplexed"],"Amazed":["Astonished","Awe"],"Excited":["Eager","Energetic"]
                }
                

print(Surprise)
#sad_list = {2:{"Lonely":["Isolated","Abanadoned"],"Vulnerable":["Victimized","Fragile"],"Despair":["Grief","Powerless"],"Guilty":["Ashamed","Remorsefull"],"Depressed":{"Empty","Inferior"},"Hurt":["Dissapointed","Embarrassed"]}}

"""
json = (json.loads("json_test.json"))



w = "Free"
temo = all_feels_list[1]
temo2 = list(temo.values())
for i in temo2:
    if w in i:
        print(i)
    else:
        print("no match")
        

"""


    
from django.shortcuts import render

def index(request):
    return render(request, 'main/home.html')

def home(request):
    return render(request,'main/home.html')

def happy(request):
    return render(request,'main/happy.html')

def sad(request):
    return render(request,'main/sad.html')

def angry(request):
    return render(request,'main/angry.html')

def mad(request):
    return render(request,'main/mad.html')

def disgusted(request):
    return render(request,'main/disgusted.html')

def fearfull(request):
    return render(request,'main/fearfull.html')

def surprised(request):
    return render(request,'main/surprised.html')


def start(request):
    return render(request, 'main/start.html', {'content':['If you would like to contact me, please email me','hskinsley@gmail.com']})

def about(request):
    return render(request, 'main/about.html')

def wheel(request):
	feelings = {'main':'happy',
			'second':'preasure',
			'third':['suffer','fatigue']}
			
			
			
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
						
	dict2 = {'dict1':all_feels_list}
	return render(request, 'personal/blog.html',dict2) 

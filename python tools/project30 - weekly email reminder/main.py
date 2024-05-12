# sending each Tuesday mail to work college to submit shifts for next week, adding Drake's quote because she's a fan
# the script is converted to exe by pyinstaller tool and runs daily on Windows Scheduler


import smtplib
import datetime as dt
import random

quotes = [
    "Live for today, plan for tomorrow, party tonight. ~ The Real Her",
    "Live without pretending, Love without depending, Listen without defending, Speak without offending. ~ Twitter",
    "Last name Ever, first name Greatest. ~ Forever",
    "The truth is, I'm really bad at taking compliments. I'm really self-conscious about my music. Even if I do a good job, I always wonder how I could have done it better. ~ 2021 Billboard Music Awards",
    "We don't like to do too much explaining, story stayed the same, I never changed it. ~ Started From the Bottom",
    "I rarely celebrate anything. For anyone watching this that's wondering how this happened, that's really the answer: It's being so unsure how you're getting it done that you just keep going in the hopes of figuring out the formula. Feeling so lucky and blessed that the fear of losing it keeps you up at night. ~ 2021 Billboard Music Awards",
    "I guess you lose some and you win some, as long as the outcome is income. ~ Over My Dead Body",
    "I'm a human being that's willing to show you I'm a human being. That, to me, is supreme confidence—the fact that I can express the issues I have. ~ CBC",
    "What bothers me most is sometimes I feel like I don't get enough credit 'cause I'm not enough of a loose cannon. People just want me to go off more and lose my composure. That's not me. I'm a naturally poised individual, I don't want to come out making mistakes. ~ CBC",
    "My excuse is that I'm young. ~ I'm On One",
    "Everyone who doubted me is asking for forgiveness. If you ain't been a part of it, at least you got to witness. ~ Forever",
    "When it comes to knowing what to say, to charm, I always had it. ~ GQ",
    "Count your blessings, not your problems. ~ Blessings",
    "I always want the truth, but it's dangerous. ~ Jaded",
    "I’ve never been reckless—it’s always calculated. I’m mischievous, but I’m calculated. ~ GQ",
    "I'm living inside a moment, not taking pictures to save it, I mean, how could I forget? My memory's never faded. ~ The Resistance",
    "I could stop right here and say, 'Okay. I own this. You know, it’s cool. I could stop,' but why? I don't want to stop. I want to take advantage and make myself the best possible me that I can be. So I’m going to work in the gym two hours a day. And try and be up there on stage, looking strong, looking iconic. ~ GQ",
    "There's times when I wish I was where I was back when I used to wish I was here. ~ Emotionless",
    "'Perfection' to me is, I walk away from a situation and say, 'I did everything I could do right there. There was nothing more that I could do.' I was a hundred percent, like the meter was at the top. There was nothing else I could have done. You know? Like, I worked as hard as I possibly could have. That’s perfection. ~ GQ",
    "Please, think before you come for the great one. ~ Back to Back",
    "I'm on a roll like Cottonelle. ~ All Me",
    "One of my biggest accomplishments is the fact that I didn't let this massive, massive change in my life destroy me. I'm just happy that I'm still intact. ~ Rap Radar Drake quote",
    "What a time this is, to be alive for this s**t. ~ Blue Tint",
    "You know it’s real when you are who you think you are. ~ Pound Cake",
    "I'm not confrontational, but if someone challenges, I'm not going to back down. ~ GQ",
    "I pulled my weight when it came to my pen. Anybody that knows me knows that my strongest talent is writing...that's why people ask me to write songs for them. ~ Rap Radar",
    "I gotta make it, I better make it, I promise if I'm not dead then I'm dedicated. ~ March 14",
    "I'm at a great place in my life. My life is about peace, my life is about drinking espressos and wine, I'm trying to make this album, I'm enjoying being a father, I'm enjoying my house. My mind isn’t plagued by beef. ~ Rap Radar",
    "Fresher than a pillow with a mint on it. ~ Lust for Life",
    "I'm actually here in front of you living the truth. I wake up in the morning and my heart is light, man. It's not heavy. I don't have skeletons in the closet on their way out. ~ GQ",
    "Jealousy is just love and hate at the same time. ~ Over My Dead Body",
    "I mean, I’m really trying. It's not like I'm just sitting here, just f**kin' shooting with my eyes closed. Like, I'm trying. I'm really trying to make music for your life. ~ The Fader",
    "It's funny when you coming in first but you hope that you're last, you just hope that it lasts. ~ Lust for Life Drake quote",
    "I like it when money makes a difference but don't make you different. ~ Time Flies",
    "I feel this great responsibility to see how far can we take it, how out of reach can I set that bar for whoever comes after. While I'm here, I'm gonna keep pushing that bar higher and higher up and make you really work for it. ~ GQ",
    "I just want to be remembered as somebody who was himself. Not a product. ~ The Fader",
    "I just have new goals, new places to go, new people to meet. I live off a different high point every day. ~ GQ",
    "I learned working with the negatives could make for better pictures. ~ HYFR (Hell Yeah F**king Right)",
    "All in all I learned a lesson from it though, you never see it coming you just get to see it go. ~ Fireworks",
    "We may be worlds apart in the sense of, you know, where you’re from, where I'm from, what I'm doing, what you're doing—but what are we talking about? We're talking about very simple human emotions. We're talking about love, sometimes. We're talking about triumph, we're talking about failure, we're talking about nerves. We're talking about fear. We're talking about doubt. It doesn't matter what you're doing—you gotta at least hear what I",
    "Everybody dies, but not everybody lives. ~ Moment for Life",
    "I'm thinking about this body of work—and asking myself: Where am I at in my life, how can I sum it up, and how can I make it relatable? ~ GQ",
    "Tables burn, bridges burn, you live and learn. ~ Pound Cake",
    "I just want to be a time-marker for my generation. ~ The Fader Drake quote",
    "I'm trying to do better than good enough. ~ The Resistance",
    "Not being vulnerable is never gonna be my thing. I'm always going to share with you what's going on in my life. ~ The Fader",
    "Always felt like my vision been bigger than the bigger picture. ~ How About Now",
    "I wanted to prove that there’s distance between me and the people you consider to be my peers. I have something special. ~ Rolling Stone",
    "Sometimes it’s about going there, not getting there. Sometimes it’s the journey that teaches you a lot about your destination. And sometimes when you get there, you’ll look back and you’ll realize that you wish you could go there again because all the experiences are the reason that you are who you are today. ~ High school graduation speech (via Rap-Up)",
    "Ayy B, I got your CD, you get an E for effort. ~ Tuscan Leather",
    "Life can always change, you have to adjust. ~ You Know You Know",
    "Life is like a confused teacher...first she gives the test and then teaches the lesson. ~ Twitter",
    "You can never reminisce when you forget it all. Careful what you wish for, you just might get it all. ~ Do It All",
    "It's funny. I remember I used to have this mentality where I'd be at the Grammys or at the MTV Awards, sitting at my seat, saying,'Oh, God, I hope they cancel my performance, or maybe the stage will break and I won't have to do this tonight—I'm nervous.' Like, on tour, I'd say, 'I hope something happens where they have to clear the building, and we'll get one night off.' This was early on, around the first album. But now I'm just like, 'Man, I hope they give me five extra minutes.' ~ Rolling Stone",
    "YOLO. ~ The Motto"
]


my_email = "beeragain3@gmail.com"
my_password = "icpnrfjkarctgedo "
gmail_smtp = "smtp.gmail.com"
noa_email = "Purple605@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    random_line = random.choice(quotes)
    #print(random_line)
    with smtplib.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= noa_email,
                            msg=f"Subject:Tuesday Reminder\n\nHey Noa !!\ndon't forget to submit shifts\n\n{random_line} \n\nElon")

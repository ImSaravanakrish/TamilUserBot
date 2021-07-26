
from random import choice

from userbot.utils import admin_cmd

# ================= CONSTANT =================

LOVESTR = [
    "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart.",
    "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
    "Love recognizes no barriers. It jumps hurdles, leaps fences, penetrates walls to arrive at its destination full of hope.",
    "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
    "The real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.",
    "I swear I couldn't love you more than I do right now, and yet I know I will tomorrow.",
    "When I saw you I fell in love, and you smiled because you knew it.",
    "In all the world, there is no heart for me like yours. / In all the world, there is no love for you like mine.",
    "To love or have loved, that is enough. Ask nothing further. There is no other pearl to be found in the dark folds of life.",
    "If you live to be a hundred, I want to live to be a hundred minus one day, so I never have to live without you.",
    "Some love stories aren't epic novels. Some are short stories. But that doesn't make them any less filled with love.",
    "As he read, I fell in love the way you fall asleep: slowly, and then all at once.",
    "I've never had a moment's doubt. I love you. I believe in you completely. You are my dearest one. My reason for life.",
    "Do I love you? My god, if your love were a grain of sand, mine would be a universe of beaches.",
    "I am who I am because of you.",
    "I just want you to know that you're very special... and the only reason I'm telling you is that I don't know if anyone else ever has.",
    "Remember, we're madly in love, so it's all right to kiss me any time you feel like it.",
    "I love you. I knew it the minute I met you.",
    "I loved her against reason, against promise, against peace, against hope, against happiness, against all discouragement that could be.",
    "I love you not because of who you are, but because of who I am when I am with you.",
]

DHOKA = [
    "Humne Unse Wafa Ki, Aur Dil Bhi Gya Toot, Wo Bhi Chinaal Nikli, Uski Maa ki Chut.",
    "Dabbe Me Dabba, Dabbe Me Cake ..Tu Chutiya Hai Zara Seesha To Dekh.",
    "Kaam Se Kaam Rakhoge Toh Naam Hoga, Randi Log Ke Chakkkar Me Padoge to Naam Badnaam Hoga.",
    "Usne Kaha- Mah Lyf maH Rule, Maine Kaha Bhag BSDK , Tujhy Paida Karna hi Teri Baap ki Sabse Badi Vul.",
    "Humse Ulajhna Mat, BSDK Teri Hasi Mita Dunga, Muh Me Land Daal Ke..Sari Hosiyaari Gand Se Nikal Dunga.",
    "Aur Sunau Bhosdiwalo ..Kya Haal Hai?..Tumhare Sakal Se Zayda Toh Tumhare Gand Laal Hai!!",
    "Pata Nhi Kya Kashish Hai Tumhare Mohabbat Me,Jab Bhi Tumhe Yaad Karta Hu Mera Land Khada Ho Jata Hai.",
    "Konsa Mohabbat Kounsi Story, Gand Faad Dunga Agr Bolne Aayi Sorry!",
    "Naam Banta Hai Risk Se, Chutiya Banta Hai IshQ Se.",
    "Sun Be, Ab Tujhy Mere Zindegi Me Ane ka Koi Haq Nhi,,Aur Tu 1 Number Ki Randi Hai Isme KOi Saq Nhi.",
    "Beta Tu Chugli Karna Chor De , Hum Ungli Karna Chor Dengy.",
]

METOOSTR = [
    "Me too thanks",
    "Haha yes, me too",
    "Same lol",
    "Me irl",
    "Same here",
    "Haha yes",
    "Me rn",
]


GDNOON = [
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good Afternoon Dear!`",
    "`With a deep blue sky over my head and a relaxing wind around me, the only thing I am missing right now is the company of you. I wish you a refreshing afternoon!`",
    "`The day has come a halt realizing that I am yet to wish you a great afternoon. My dear, if you thought you were forgotten, you’re so wrong. Good afternoon!`",
    "`Good afternoon! May the sweet peace be part of your heart today and always and there is life shining through your sigh. May you have much light and peace.`",
    "`With you, every part of a day is beautiful. I live every day to love you more than yesterday. Wishing you an enjoyable afternoon my love!`",
    "`This bright afternoon sun always reminds me of how you brighten my life with all the happiness. I miss you a lot this afternoon. Have a good time`!",
    "`Nature looks quieter and more beautiful at this time of the day! You really don’t want to miss the beauty of this time! Wishing you a happy afternoon!`",
    "`What a wonderful afternoon to finish you day with! I hope you’re having a great time sitting on your balcony, enjoying this afternoon beauty!`",
    "`I wish I were with you this time of the day. We hardly have a beautiful afternoon like this nowadays. Wishing you a peaceful afternoon!`",
    "`As you prepare yourself to wave goodbye to another wonderful day, I want you to know that, I am thinking of you all the time. Good afternoon!`",
    "`This afternoon is here to calm your dog-tired mind after a hectic day. Enjoy the blessings it offers you and be thankful always. Good afternoon!`",
    "`The gentle afternoon wind feels like a sweet hug from you. You are in my every thought in this wonderful afternoon. Hope you are enjoying the time!`",
    "`Wishing an amazingly good afternoon to the most beautiful soul I have ever met. I hope you are having a good time relaxing and enjoying the beauty of this time!`",
    "`Afternoon has come to indicate you, Half of your day’s work is over, Just another half a day to go, Be brisk and keep enjoying your works, Have a happy noon!`",
    "`Mornings are for starting a new work, Afternoons are for remembering, Evenings are for refreshing, Nights are for relaxing, So remember people, who are remembering you, Have a happy noon!`",
    "`If you feel tired and sleepy you could use a nap, you will see that it will help you recover your energy and feel much better to finish the day. Have a beautiful afternoon!`",
    "`Time to remember sweet persons in your life, I know I will be first on the list, Thanks for that, Good afternoon my dear!`",
    "`May this afternoon bring a lot of pleasant surprises for you and fills you heart with infinite joy. Wishing you a very warm and love filled afternoon!`",
    "`Good, better, best. Never let it rest. Til your good is better and your better is best. “Good Afternoon`”",
    "`May this beautiful afternoon fill your heart boundless happiness and gives you new hopes to start yours with. May you have lot of fun! Good afternoon dear!`",
    "`As the blazing sun slowly starts making its way to the west, I want you to know that this beautiful afternoon is here to bless your life with success and peace. Good afternoon!`",
    "`The deep blue sky of this bright afternoon reminds me of the deepness of your heart and the brightness of your soul. May you have a memorable afternoon!`",
    "`Your presence could make this afternoon much more pleasurable for me. Your company is what I cherish all the time. Good afternoon!`",
    "`A relaxing afternoon wind and the sweet pleasure of your company can make my day complete. Missing you so badly during this time of the day! Good afternoon!`",
    "`Wishing you an afternoon experience so sweet and pleasant that feel thankful to be alive today. May you have the best afternoon of your life today!`",
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good afternoon dear!`",
    "`Noon time – it’s time to have a little break, Take time to breathe the warmth of the sun, Who is shining up in between the clouds, Good afternoon!`",
    "`You are the cure that I need to take three times a day, in the morning, at the night and in the afternoon. I am missing you a lot right now. Good afternoon!`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`I pray to god that he keeps me close to you so we can enjoy these beautiful afternoons together forever! Wishing you a good time this afternoon!`",
    "`You are every bit of special to me just like a relaxing afternoon is special after a toiling noon. Thinking of my special one in this special time of the day!`",
    "`May your Good afternoon be light, blessed, enlightened, productive and happy.`",
    "`Thinking of you is my most favorite hobby every afternoon. Your love is all I desire in life. Wishing my beloved an amazing afternoon!`",
    "`I have tasted things that are so sweet, heard words that are soothing to the soul, but comparing the joy that they both bring, I’ll rather choose to see a smile from your cheeks. You are sweet. I love you.`",
    "`How I wish the sun could obey me for a second, to stop its scorching ride on my angel. So sorry it will be hot there. Don’t worry, the evening will soon come. I love you.`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`With you every day is my lucky day. So lucky being your love and don’t know what else to say. Morning night and noon, you make my day.`",
    "`Your love is sweeter than what I read in romantic novels and fulfilling more than I see in epic films. I couldn’t have been me, without you. Good afternoon honey, I love you!`",
    "`No matter what time of the day it is, No matter what I am doing, No matter what is right and what is wrong, I still remember you like this time, Good Afternoon!`",
    "`Things are changing. I see everything turning around for my favor. And the last time I checked, it’s courtesy of your love. 1000 kisses from me to you. I love you dearly and wishing you a very happy noon.`",
    "`You are sometimes my greatest weakness, you are sometimes my biggest strength. I do not have a lot of words to say but let you make sure, you make my day, Good Afternoon!`",
    "`Every afternoon is to remember the one whom my heart beats for. The one I live and sure can die for. Hope you doing good there my love. Missing your face.`",
    "`My love, I hope you are doing well at work and that you remember that I will be waiting for you at home with my arms open to pamper you and give you all my love. I wish you a good afternoon!`",
    "`Afternoons like this makes me think about you more. I desire so deeply to be with you in one of these afternoons just to tell you how much I love you. Good afternoon my love!`",
    "`My heart craves for your company all the time. A beautiful afternoon like this can be made more enjoyable if you just decide to spend it with me. Good afternoon!`",
]


CHASE_STR = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "`Get back here!`",
    "`Not so fast...`",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "`Jokes on you, I'm everywhere`",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "`Go bother someone else, no-one here cares.`",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    '"Oh, look at me! I\'m so cool, I can run from a bot!" - this person',
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]


HELLOSTR = [
    "Hi !",
    "‘Ello, gov'nor!",
    "What’s crackin’?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "`Hey, howdy, hi!`",
    "What’s kickin’, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`I come for peace!`",
    "Ahoy, matey!",
    "`Hi !`",
]

CONGRATULATION = [
    "`Congratulations and BRAVO!`",
    "`You did it! So proud of you!`",
    "`This calls for celebrating! Congratulations!`",
    "`I knew it was only a matter of time. Well done!`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]

BYESTR = [
    "`Nice talking with you`",
    "`I've gotta go!`",
    "`I've gotta run!`",
    "`I've gotta split`",
    "`I'm off!`",
    "`Great to see you,bye`",
    "`See you soon`",
    "`Farewell!`",
]

GDNIGHT = [
    "`இப்போது ஓய்வெடுக்கவும்.நாள் முடிந்துவிட்டது.நீங்கள் உங்கள் சிறந்த செய்தீர்கள்.நாளை நீ நன்றாக செய்வாய்.இனிய இரவு😇!`",
    "`குட்டி இரவில்🤗,செல்ல தூக்கத்தில்😴,சின்ன கனவு காணும் செல்ல இதயத்திற்கு❤️!சின்ன மனசு சொல்லும்🥰 இரவு வணக்கும்🙏!`",
    "`நம் கவலை மூட்டைகளை இறக்கி வைக்க தருணம் தரும் இரவு🤗!இனிய இரவு வணக்கம்🥱!`",
    "`தொட்டு தொட்டு ரசிக்கும் கண் இமைகளை கொஞ்ச நேரம் கட்டி அணைக்க அனுமதிப்போம்😒!`",
    "`அணைந்து போன கனவுகளைசரி செய்ய இந்த இதமான இரவு🤗!இனிய இரவு வணக்கம்🙏!`",
    "`இரவின் மடியினில்🥰,விழிகளை மூடி😑,கவலைகளை மறந்து தூங்கிடுவோம்🤗!இனிய இரவு வணக்கம்🥱!`",
    "`எத்தனை நட்சத்திரம் மினுமினுத்தாலும் ஏனோ மனம் ஏங்குகிறது😧வராத அந்த ஒரு நிலவுக்காக😪 இனிய இரவு வணக்கம்🙏!`",
    "`இரவுகள் நம்மை உறங்க விட்டாலும் சில நினைவுகள் உறங்க விடுவதில்லை🤷‍♀️! இனிய இரவு வணக்கம்🙏!`",
    "`கற்பனை கனவு கலைந்துவிடும் என்று தெரிந்தும் கண்கள் கனவு காண பயணிக்கிறது🥱!,இனிய இரவு வணக்கம்🙏!`",
    "`நேற்று வந்த மேகங்கள் இன்று வானில் இல்லை🤷‍♂,இன்று வந்த சோகங்கள் நாளை நம்மை தொடராது🤗! இனிய இரவு வணக்கம்😴!`",
    "`எந்த பிரச்சனையும் இல்லை, அன்பே நண்பர்!ஒரு நல்ல இரவு😴!`",
    "`இரவு நீங்கள் நட்சத்திரங்களுடன் நிரப்பலாம்🥰.ஒவ்வொருவருக்கும் எண்ணலாம்😁, உங்களுக்கு திருப்தி கொடுங்கள்😅!`",
    "`நல்ல இரவு உங்கள் கனவுகளை உயிருடன் வைத்திருங்கள்🥲!`",
    "`இன்றிரவு உங்களுக்கு எந்த நடவடிக்கையும் இல்லை🤷‍♂️, நண்பன்!நீங்கள் வரவிருக்கும் மீதமுள்ள ஓய்வு விரைவாக வரலாம்😇!நாளை நீங்கள் செய்யும் செயல்பாடு உங்கள் வேகத்துடன் பொருந்தும் மற்றும் உங்கள் சொந்த தயாரிப்பாக இருக்கும்😍!`",
    "`இரவில் இருள் ஒரு தூக்கத்தில் நீங்கள் ஒரு தூக்கத்தில் இருக்க வேண்டும்!அன்பே நண்பர், இந்த உணர்வு அடுத்த நாள் மூலம் உங்களைச் செயல்படுத்தலாம்!இரவு வணக்கம்🙏!`",
    "`நிலவை பார்க்கும் போது நீ தூரமாய் இருப்பதாய் உணர்கிறேன்1😪, என் நிழலை பார்க்கும் போது நீ என்னோடு இருப்பதை உணர்கிறேன்🥰. இனிய இரவு வணக்கம்🤗!`",
    "`நண்பர், நீங்கள் விஷயங்களை பெற தயங்க வேண்டாம்😁!இன்றைய தினம் ஓய்வெடுக்கவும்😶, நாளை இன்னும் செய்யுங்கள்🤗!`",
    "`வீழும் நட்சத்திரங்களாய் இன்றி வாழும் நில்வினை போல் கொண்ட நட்பே🥰! நல் இரவு வணக்கம்🤗🥱!`",
    "`அமைதியான இரவு..!🤗அம்சமான நிலவு..!❤️ அர்ப்பரிக்கும் நட்சத்திரங்கள்..!😇அசரவைக்கும் பனிக்காற்றில் அசந்து தூங்கும் என் நண்பனுக்கு..! இனிய இரவு வணக்கம்🥱🙏!`",
    "`இரவின் மயக்கத்தில் மொட்டுகளும் உறங்கும் உங்கள் மனதும் உறங்கட்டும் காலையில் புன்னகையுடன் மலர என் இனிய இரவு வணக்கம் 🙏!`",
    "`பேய்  வர நேரம் ஆச்சு சீக்கிரம் பொய் முகத்தை மூடி படுத்துக்கோ😳 இல்லேனா பாவம் பேய்  பயந்துடும்🤣!  குட் நைட்😴!`",
    "`சிங்கம் தூங்கும் போது நீ எழுப்பினாலும்,நீ தூங்கும் போது சிங்கம் எழுப்பினாலும்,சாவு உனக்கு தான்😂 அதனாலஎன்ன டிஸ்டர்ப் பண்ணாத நா தூங்க போறேன்🥱.`",
    "`விடியும் வரை தூங்குவது தூக்கம் அல்ல🤦‍♂️,நம்மால் முடியும் வரை தூங்குவதுதான் தூக்கம்🤣!சோ நல்லா தூங்குங்க🤗!`",
    "`அச்சச்சோ😧 நீங்க இன்னும் தூங்கலையா🤭?என்னோட குட் நைட் மெசேஜ் காக வெயிட் பண்றீங்களா🤔?ஓகே…. ஓகே…. குட் நைட்..ஸ்வீட் ட்ரம்ஸ்🤗!`",
    "`பிசாசு விசிறி வீச🤭,பேய்கள் தாலாட்டு  பாட🤪,பூதங்கள் இசை அமைக்க😬,காட்டேரி காலை அமுக்க🤒,மோகினி கதை சொல்ல😳, அவைகளின் நடுவில் இன்பமாக தூங்கு🤣,குட் நைட்😴!`",
    "`நிலவின் ஒளியில் நீ உறங்க🥰,விண்மீன் கண்டு கண் சிமிட்ட🥰,தென்றல் உனக்கு தாலாட்டு பாட😍,என் செல்லாமை நீ “கருங்குரங்கு”😁,😳சாரி சாரி கண்ணுறங்கு😂.`",
    "`இரவின் மடியில் பகலும் தூங்கும்😊! இனிய கனவில் நீயும் தூங்கு🥰! கரையின் மடியில் அலையும் தூங்கும்😍!கவலை மறந்து நீயும் தூங்கு😴!`",
    "`அழகான இரவு நேரம்😇!கண்கள் உறங்கும் நேரம்🥱!கனவுகள் மலரும்நேரம்😴! உரிமையோடு சொல்கிறேன😊! குட் நைட்🥰!`",
    "`செல்லும் செல்லும் நோக்கியா மெசேஜ் அனுப்ப மாட்டிய😒 உன் செல் போன் என்ன ஓட்டையா🤭 நைட் டிபன் சாப்டியா😇 டைம் அ  கொஞ்சம் பாத்தயா..குட் நைட் சொல்ல மாட்டியா 😒!`",
    "`படிக்கும் போது தூக்கம் வந்தா என்ன பண்ணனும்😕? படிப்புதான் வரல,தூக்கமாவது வருதே என்று தூங்கிறணும்🙊,நீங்க போய் தூங்குங்க.குட் நைட்🥱!`",
    "`இனிய இரவு என் நண்பா😇.நீங்கள் தூங்கும்போது இறைவன் உங்களைப் பார்த்துக் கொண்டிருப்பதை நான் பிரார்த்திக்கிறேன்🤭.இனிமையான கனவுகள்🤗!`",
    "`இருள் எப்போதும் நீடிக்கும்🥶.நம்பிக்கையை உயிருடன் வைத்திருங்கள்🙂.இனிய இரவு☺️!`",
    "`இனிய இரவு😌! நான் உங்கள் கனவில் வர விரும்புகிறேன்😋!`",
    
]

GDMORNING = [
    "`நாளை ஒரு சரியான திட்டத்தை விட இன்று ஒரு நல்ல திட்டம் சிறந்தது☺️. காலை வணக்கம்🥰!`",
    "`வாழ்க்கை நிச்சயமற்ற தன்மைகளால் நிறைந்துள்ளது😑,ஆனால் ஒவ்வொரு சூரிய அஸ்தமனத்திற்கும் பிறகு எப்போதும் சூரிய உதயம் இருக்கும்❤️. காலை வணக்கம்🥰!`",
    "`உங்கள் நேற்று எவ்வளவு மோசமாக இருந்தது என்பது முக்கியமல்ல🙅‍♀. இன்று, நீங்கள் அதை ஒரு நல்லதாக மாற்றப் போகிறீர்கள்🤝. உங்களுக்கு ஒரு காலை வணக்கம்🤗!`",
    "`உங்கள் கனவுகளை நனவாக்க விரும்பினால், முதலில் நீங்கள் செய்ய வேண்டியது எழுந்திருப்பதுதான்😝. காலை வணக்கம்😊!`",
    "`ஒவ்வொரு நாளும் உங்கள் வாழ்க்கையின் மிக அழகான நாளாக மாற வாய்ப்பளிக்கவும்🙂. காலை வணக்கம்🤗!`",
    "`ஒவ்வொரு காலையிலும் நாம் மீண்டும் பிறக்கிறோம்😇. இன்று நாம் செய்வது மிக முக்கியமானது🥰. காலை வணக்கம்🙏!`",
    "`காலை வணக்கம் அன்பே😻! இன்று நீங்கள் விலகும்போது உங்கள் நாள் உண்மையான வெற்றிகளிலும் உண்மையான மகிழ்ச்சியிலும் மூழ்கட்டும்😌.`",
    "`நீங்கள் எழுந்த ஒவ்வொரு நாளும் அப்பால் செல்ல ஒரு வாய்ப்பு😍. காலை வணக்கம்🥰!`",
    "`சிரிப்பு இல்லாத ஒரு நாள் வீணாகும் நாள்😒. நல்ல காலை☺️!`",
    "`வாய்ப்புகள் சூரிய உதயங்கள் போன்றவை😐,நீங்கள் அதிக நேரம் காத்திருந்தால், நீங்கள் அவர்களை இழக்கிறீர்கள்🥺. நல்ல காலை🥰!`",
    "`காலை வணக்கம்😻! உங்கள் நாள் மகிழ்ச்சியையும் மகிழ்ச்சியையும் நிரப்புகிறது என்று நம்புகிறேன்😕.`",
    "`நீங்கள் எங்கு சென்றாலும் நேர்மறையைப் பரப்புங்கள்😍! காலை வணக்கம்😘!`",
    "`தினமும் நன்றாக இருக்காது😞, ஆனால் ஒவ்வொரு நாளும் ஏதோ நல்லது இருக்கிறது❤️. காலை வணக்கம்🥰!`",
    "`வாழ்க்கை ஒரு ரோஜா செடி மாதிரி😕 முள்ளும் இருக்கும் மலரும் இருக்கும்😐 முல்லை கண்டு பயந்து விடாதே😌 மலரை கண்டு மயங்கி விடாதே😛. இனிய காலை வணக்கம்😄!`",
    "`விடியும் என்ற எண்ணத்தில் உறங்க செல்லும் நீ😌, முடியும் என்ற எண்ணத்தோடு எழுந்திரு சாதிக்கலாம்😻! இனிய காலை வணக்கம்🥰!`",
    "`தவறி விழுந்த விதையே முளைக்கும் போது தடுமாறி விழுந்த உன் வாழ்க்கை மட்டும் சிறக்காதா😏. காலை வணக்கம்🥰!`",
    "`எதிர்பார்த்த வாழ்க்கை யாருக்கும் அமைவது இல்லை😞, எதிர் பார்க்காமல் யாரும் வாழ்வது இல்லை😐. இனிய காலை வணக்கம்🥳!`",
    "`இன்று வரும் துன்பங்களை கண்டு ஒழிந்தால் நாளை வரும் துன்பங்களை யார் வரவேற்பது😒. காலை வணக்கம்😍!`",
    "`துன்பம் நேர்ந்த காலத்தை மறந்து விடு😐,ஆனால் அது உனக்கு கற்பித்த பாடத்தை மறந்து விடாதே🙅‍♀ இனிய காலை வணக்கம்🥰!`",
    "`ஒரு குறிக்கோளை முடிவு செய்த பின் அதற்கான முயற்சிகளில் மட்டும் கவனம் செலுத்துங்கள்😄. இனிய காலை வணக்கம்🥰!`",
    "`உன்னை போல இந்த உலகில் யாரும் இல்லை🤐 அதற்கு உன் கை ரேகைகளே சாட்சி🤷‍♀! இனிய காலை வணக்கம்😍!`",
    "`அடுத்தவர்களிடம் குறைகளை தேடுவதை விடநிறைகளை தேடு உன் மனம் பக்குவமடையும்😊. இனிய காலை வணக்கம்🤗!`",
    "`தண்ணீரை கூட சல்லடையில் அள்ளலாம் பனிக்கட்டியாக ஆகும் வரை காத்திருந்தாள்😉.இனிய காலை வணக்கம்❤️!`",
    "`ஆவலாய் காத்திருக்கிறோம்❤️, மழைக்காக குடையும்😍, உனக்காக நானும்😘! காலை வணக்கம்🥰!`",
    "`நம் வாழ்வில் திரும்ப பெற முடியாதவை உயிரும் ,நேரமும் ,சொற்களும்❤️. இனிய காலை வணக்கம்😍!`",
    "`வேதனைகளை வென்று விட்டால் அதுவே ஒரு சாதனை தான்😱. இனிய காலை வணக்கம்🤗!`",
    "`எல்லா சமயமும் கூறுவது தீமையை செய்யாதே நன்மையை செய்😕.இனிய காலை வணக்கம்🥰!`",
    "`உதிக்கும் சூரியனை போல உங்கள் வாழ்க்கை நன்கு மிளிரட்டும்😅. இனிய காலை வணக்கம்🥳!`",
    "`தோல்வி உன்னை துரத்தினால் வெற்றியை நோக்கி நீ ஓடு🥰. இனிய காலை வணக்கம்🤗!`",
   
]


@borg.on(admin_cmd(pattern=f"love$", outgoing=True))
async def love(chutiyappa):
    await chutiyappa.edit(choice(LOVESTR))


@borg.on(admin_cmd(pattern=f"dhoka$", outgoing=True))
async def katgya(chutiya):
    await chutiya.edit(choice(DHOKA))


@borg.on(admin_cmd(pattern=f"metoo$", outgoing=True))
async def metoo(hahayes):
    await hahayes.edit(choice(METOOSTR))


@borg.on(admin_cmd(pattern=f"gnoon$", outgoing=True))
async def noon(noon):
    await noon.edit(choice(GDNOON))


@borg.on(admin_cmd(pattern=f"chase$", outgoing=True))
async def police(chase):
    await chase.edit(choice(CHASE_STR))


@borg.on(admin_cmd(pattern=f"congo$", outgoing=True))
async def Sahih(congrats):
    await congrats.edit(choice(CONGRATULATION))


@borg.on(admin_cmd(pattern=f"qhi$", outgoing=True))
async def hoi(hello):
    await hello.edit(choice(HELLOSTR))


@borg.on(admin_cmd(pattern=f"gbye$", outgoing=True))
async def bhago(bhagobc):
    await bhagobc.edit(choice(BYESTR))


@borg.on(admin_cmd(pattern=f"gn$", outgoing=True))
async def night(night):
    await night.edit(choice(GDNIGHT))


@borg.on(admin_cmd(pattern=f"gm$", outgoing=True))
async def morning(morning):
    await morning.edit(choice(GDMORNING))

@borg.on(admin_cmd(pattern="gnt$"))
async def gn(event):
    await event.edit(
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･"
    )


@borg.on(admin_cmd(pattern="gmg$"))
async def gm(event):
    await event.edit(
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･"
    )


# by @turquoise-giggle
@borg.on(admin_cmd(pattern="gmg2$"))
async def gn(event):
    await event.edit(
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･"
    )


# by @turquoise-giggle
@borg.on(admin_cmd(pattern="gnt2$"))
async def gm(event):
    await event.edit(
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･"
    )


# by  @Halto_Tha
@borg.on(admin_cmd(pattern=r"lmoon$"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕"
    )


@borg.on(admin_cmd(pattern=r"city$"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁
🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                        👬     🌴/            l  🚔    \🌲
      🌲/   🚖     l        \
          🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )


# @PhycoNinja13b 's Part begin from here


@borg.on(admin_cmd(pattern=r"hi ?(.*)"))
async def hi(event):
    giveVar = event.text
    cat = giveVar[4:5]
    if not cat:
        cat = "🌺"
    await event.edit(
        f"{cat}✨✨{cat}✨{cat}{cat}{cat}\n{cat}✨✨{cat}✨✨{cat}✨\n{cat}{cat}{cat}{cat}✨✨{cat}✨\n{cat}✨✨{cat}✨✨{cat}✨\n{cat}✨✨{cat}✨{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁"
    )


@borg.on(admin_cmd(pattern=r"cheer$"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit(
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐"
    )


@borg.on(admin_cmd(pattern=r"getwell$"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")


@borg.on(admin_cmd(pattern=r"luck$"))
async def luck(event):
    if event.fwd_from:
        return
    await event.edit(
        "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@borg.on(admin_cmd(pattern=r"sprinkle$"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit(
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀"
    )

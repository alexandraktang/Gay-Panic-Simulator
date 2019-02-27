# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mel = Character("Mel")
define p = Character("[playername]")
define c = Character("Claire")

image carbg_1 = im.Scale("carbg_1.png", 1280, 720)
image carbg_2 = im.Scale("carbg_2.png", 1280, 720)
image carbg_3 = im.Scale("carbg_3.png", 1280, 720)

image andie_normal = im.Scale("andie_normal.png", 1280, 720)
image andie_dum = im.Scale("andie_dum.png", 1280, 720)
image andie_annoyed = im.Scale("andie_annoyed.png", 1280, 720)
image andie_thinking = im.Scale("andie_thinking.png", 1280, 720)
image andie_laugh = im.Scale("andie_laugh.png", 1280, 720)
image andie_side = im.Scale("andie_side.png", 1280, 720)
image andie_disappoint = im.Scale("andie_disappoint.png", 1280, 720)
image andie_embarrassed = im.Scale("andie_embarrassed.png", 1280, 720)
image andie_excite = im.Scale("andie_excite.png", 1280, 720)

image mel_angry = im.Scale("mel_angry.png", 1280, 720)
image mel_surprise = im.Scale("mel_surprise.png", 1280, 720)
image mel_disappoint = im.Scale("mel_disappoint.png", 1280, 720)
image mel_smolsmile = im.Scale("mel_smolsmile.png", 1280, 720)
image mel_angry = im.Scale("mel_angry.png", 1280, 720)
image mel_speaking = im.Scale("mel_speaking.png", 1280, 720)
image mel_bigsmile = im.Scale("mel_bigsmile.png", 1280, 720)


# The game starts here.

label start:
    
    $ friendship = 0
    $ andie_gay = "false"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene carbg_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # These display lines of dialogue.
    
    python:
        playername = renpy.input("what's your name?")
        playername = playername.strip()

        if not playername:
             playername = "Andie"
             
    show andie_embarrassed

    "there's an awkward shuffle as i fold my arms together, trying to maintain {i}some{/i} semblance of
     nonchalance."

    "unfortunately, that's a high request considering my half of the car looks as though it'd just
     come out of a storm."
    
    hide andie_embarrassed
    show andie_annoyed
     
    "stupid bee."
    
    scene carbg_2
    
    show andie_side
    
    "i look over at mel, who continues driving as though the ordeal hadn't happened at all."
    
    "if i stared at her any longer, i'd probably start to doubt it happened myself."
    
    show mel_speaking
    
    mel "take a picture. it'll last longer."
    
    menu:
        "do you have a camera then?":
            $ friendship += 5
            hide mel_speaking
            hide andie_side
            show andie_thinking
            p "do you have a camera then?"
            show mel_surprise
            "the quirk in one of mel's eyebrows has me reeling in triumph."
            "{i}finally{/i}, a reaction!"
        
        "i don't want to forget what you look like.":
            hide mel_speaking
            hide andie_side
            show andie_dum
            p "i-"
            p "i don't want to forget what you look like."
            $ friendship += 10
            hide andie_dum
            show mel_surprise
            "and it's true."
            "somewhat."
            show andie_normal
            "it's been a while since i'd last seen her, and it's strange considering how often we used to 
             see each other." 
            "to forget the face of someone you used to know so well... isn't that a bit scary?"
            
        "i wasn't looking at you...":
            $ friendship -= 5
            hide mel_speaking
            hide andie_side
            show andie_normal
            p "i wasn't looking at you..."
            show mel_disappoint
            "that's a blatant lie and we both know it."
        
        "sorry.":
            hide mel_speaking
            p "sorry."
            hide andie_side
            p "i didn't realize i was staring."
            
    scene carbg_3
            
    "mel's always been the quietest of us three. silence was a rather foreign concept to claire and myself."
    
    "throughout high school, claire and i were constantly debating something outlandish in the halls."
    
    "our most heated argument was over whether stars have feelings or not."
    
    show andie_annoyed
    
    "and while i'm certain stars have feelings and claire's {i}definitely{/i} wrong... it's besides
     the point."
    
    hide andie_annoyed
    show andie_normal
    
    "mel always followed along behind us, silently amused by our arguments but refused to get between them."
    
    "it'd always felt like mel was somewhere else, even when she was standing right there with us."
    
    "even now, it feels like she isn't actually here."
    
    "she keeps her eyes trained on the road, just as they've been for the past three hours. i don't 
     think she's looked at me since she picked me up."
    
    show andie_embarrassed
    
    "well, other than during my fiasco earlier."
    
    hide andie_embarrassed
    show andie_side
    
    "i wonder what she's thinking about."
    
    menu:
        "ask her what she's thinking about.":
            hide andie_side
            p "penny for your thoughts?"
            "the question hangs in the air for a moment before i register mel's voice, soft and calm."
            show mel_speaking
            mel "nothing really."
            hide mel_speaking
            show andie_boredawk
            "....well, that didn't work."
            "maybe i should press her for more."
            menu:
                "press her for more.":
                    show andie_dum
                    p "nothing?"
                    hide andie_dum
                    show mel_surprise
                    "she shifts in her seat ever so slightly, shoulders tensing."
                    hide mel_surprise
                    show mel_speaking
                    mel "well, what exactly are you looking for?"
                    hide mel_speaking
                    show andie_dum
                    p "{i}well...{/i} what's been going on in your life?"
                    p "we haven't seen each other in eight months."
                    hide andie-dum
                    show mel_speaking
                    mel "i saw you two weeks ago."
                    hide mel_speaking
                    p "w-wait, what?"
                    scene carbg_2
                    show andie_dum
                    show mel_speaking
                    mel "you were in the dining hall, probably playing some game on your phone like always."
                    hide mel_speaking
                    show mel_disappoint
                    mel "i see you quite often actually."
                    hide mel_disappoint
                    hide andie_dum
                    show andie_side
                    "i... i can't say i remember seeing her around."
                    "i know we go to the same college, but i just figured we ran different paths."
                    "i feel kind of foolish."
                
                "switch the subject.":
                    "on second thought, maybe we should just switch subjects."
                    "i don't want to pry for more if she's not willing to share."
                    "maybe we should talk about..."
                    menu:
                        "yoga.":
                            p "have you ever considered that downward dog looks more like a stretching
                               cat?"
                            show mel_surprise
                            mel "i don't follow."
                            p "{i}you know...{/i} that pose where you put your head down and your butt
                               in the air?"
                            hide mel_surprise
                            show mel_smolsmile
                            "i think i hear mel stiffling a laugh."
                            $ friendship += 10
                            mel "i don't think that's how you want to explain that."
                            menu:
                                "head down, ass up?":
                                    show andie_laugh
                                    p "head down, ass up?"
                                    $ friendship += 20
                                    p "that better?"
                                    scene carbg_2
                                    show andie_laugh
                                    show mel_bigsmile
                                    mel "i don't know why i'm laughing at this."
                                    p "i didn't take you for a person who laughs at dirty jokes."
                                    mel "and i didn't take you for a person who told them."
                                    p "touche."
                                    
                                "shake your tail feather?":
                                    show andie_laugh
                                    p "shake your tail feather?"
                                    "i twist in my seat, arms held to my sides like wings, as mel shakes
                                     her head, smile still tugging at the corners of her lips."
                                    p "right, chicken little?"
                                    hide mel_smolsmile
                                    mel "oh boy."
                                    "in the first couple of months the three of us got to know each other,
                                     claire and i were desperate for nicknames as a way of solidifying our
                                     {i}squad-ness{/i}."
                                    "we'd instantly dubbed mel chicken little, being the shortest in our trio
                                     and donning glasses."
                                    "unfortunately, that left claire and i with runt and abby respectively.
                                     and declaring herself too beautiful to be the ugly duckling, she
                                     was runt and i was left with--"
                                    show mel_speaking
                                    mel "ugly duckling, was it?"
                                    hide andie_laugh
                                    hide mel_speaking
                                    show andie_embarrassed
                                    p "abby, actually."
                                    scene carbg_2
                                    show mel_speaking
                                    mel "well, for what it's worth..."
                                    hide mel_speaking
                                    show mel_disappoint
                                    mel "you're definitely not ugly."
                                    show andie_embarrassed
                                    mel "and i'm sorry we gave you that nickname."
                                    mel "you deserve better than that."
                                    hide mel_disappoint
                                    hide andie_embarrassed
                                    show andie_side
                                    p "it's--"
                                    p "it's nothing."
                                    $ friendship += 10
                                    
                        "space jam.":
                            show andie_excite
                            p "space jam. favorite character. go!"
                            hide andie_excite
                            show mel_speaking
                            mel "w-wait, what?"
                            hide mel_speaking
                            show andie_dum
                            p "space jam!"
                            p "the movie that made us all love michael jordan!"
                            hide andie_dum
                            show andie_disappoint
                            "suddenly, i recall a moment in the movie with utter distain and can't help as my next
                             comment comes out garbled."
                            p "...even though the baseball scene was painful."
                            hide andie_disappoint
                            scene carbg_2
                            show mel_speaking
                            mel "the entire movie was... {i}something{/i}."
                            hide mel_speaking
                            show andie_laugh
                            p "a film for the ages!"
                            show mel_smolsmile
                            mel "i guess."
                            show andie_side
                            p "so, favorite character?"
                            hide mel_smolsmile
                            show mel_disappoint
                            mel "{i}um.{/i}"
                            mel "lola, i guess?"
                            hide andie_side
                            show andie_excite
                            p "me too!"
                            hide mel_disappoint
                            show mel_smolsmile
                            p "she's so badass! showing up all the guys like that."
                            hide mel_smolsmile
                            p "i wanted to be like her."
                            mel "yeah..."
                            mel "me too."
                            $ friendship += 10
                            
        "don't press it.":
            hide andie_side
            "i decide not to bother her. she seems deeply concentrated on the road."
            "i also just... don't know what to say."
            "it's been so long since we last spoke."
            "and we didn't even {i}really{/i} speak."
            show mel_speaking
            mel "i--"
            hide mel_speaking
            show mel_disappoint
            show andie_side
            "mel starts, only to shut her mouth and avert her gaze."
            "her fingers tap against the wheel rhythmically, though each tap only unsettles me further 
             in the painful silence that engulfs us."
            mel "sorry."
            mel "i've... kind of been on edge lately."
            hide mel_disappoint
            show mel_speaking
            mel "i didn't mean to be a poor host or anything."
            hide mel_speaking
            show mel_disappoint
            mel "and if it's any consolation..."
            mel "i {i}am{/i} glad to see you."
            hide andie_side
            show andie_embarrassed
            "my cheeks heat up from her sudden confession and i can barely find the words to respond."
            p "y-yeah, me too."
            hide andie_embarrassed
            show andie_dum
            p "i'm glad to see {i}you{/i}, i mean."
            p "not that i'm glad to see me."
            $ friendship += 5
            hide andie_dum
            "{i}nice.{/i}"
            
    scene carbg_1
    
    "silence falls over the car once again, though this time it rests more comfortably on our shoulders."
    
    "i listen to the gentle hum of the cars on the road and sink deeper into my seat with a sense of ease that i hadn't
     quite gotten since we first planned this trip."
    
    "i was worried about seeing the two of them again."
    
    "mel, more than claire, if i'm being honest."
    
    "it's been eight months since we last saw each other as a group and we promised then we'd visit claire at her
     university in los angeles."
    
    "i just didn't think that time would come so soon."
    
    show andie_boredawk
    
    "or that it'd actually happen."
    
    hide andie_boredawk
    
    show andie_dum
    show mel_speaking
    
    "a buzz from our phones startles me from my thoughts, and from the look on her face, mel from her own."
    
    "soon after, a barrage of buzzes ring from both our screens. it's a text from claire in the group chat,
     asking for an update on our trip."
    
    hide andie_dum
    
    p "i'll answer it."
    
    hide mel_speaking
    
    "mel nods affirmatively, regaining her composure."

    show mel_speaking
    
    mel "that'd be helpful. thanks."
    
    hide mel_speaking
    
    "i unlock my phone eagerly, quite starved for the distraction."
    
    "despite my beginnings at a breakthrough with mel, i need something to recharge myself in the time between."
    
    "awkward silences are great and all but only with crushes and not with best friends."
    
    "actually, not even with crushes."
    
    show andie_laugh
    
    "i open the chat and immediately grin as i read the message."
    
    c "not to be That Guy but..."
    c "ARE WE THERE YET?"
    c "kidding kidding, i'm just so excited."
    c "that and i've had too many cups of coffee."
    c "let me know your eta whenever you can!"
    
    "i quickly type back a response, opting to tease her instead of answering."
    
    p "we're on our way! we agreed on utah, right?!"
    c "what!!!!"
    c "i thought we said montana!!!"
    c "great, i'm going to need to catch another flight."
    p "and mel's in louisana!!!"
    c "this is a disaster!!!"
    p "guess we'll just have to meet in the middle."
    c "kansas?"
    p "are we going to oz? you've outdone yourself."
    c "you know me too well."
    p "all jokes aside, we're about an hour and a half away? we'll let you know as we get closer."
    c "do share! drive safely!"
    c "love you!"
    "a second goes by before claire sends another message."
    c "tell me you love me too!!!"
    p "i love..."
    p "your hair."
    c "good enough!!!"
    
    "i can't wipe the grin off my face from our banter and mel seems to notice as she speaks again."
    
    show mel_speaking
    
    mel "i take that grin as we still have a place to stay tonight?"
    
    hide mel_speaking
    
    p "'course. the world of oz has countless places to sleep."
    
    show mel_surprise
    
    mel "not sure what that means, but i assume the answer lies in those texts."
    
    hide mel_surprise
    show mel_smolsmile
    
    p "precisely."
    
    scene carbg_1
    
    "rolling her shoulders, mel glances over at me quickly before refocusing her gaze."
    
    show mel_speaking
    
    mel "you think she's alright?"
    
    hide mel_speaking
    show andie_side
    
    p "what do you mean?"
    
    show mel_speaking
    
    mel "i don't know. it's been a while."
    mel "and despite how rambunctious cla--"
    
    hide andie_side
    show andie_laugh
    
    p "{i}rambunctious?{/i}"
    hide mel_speaking
    show mel_smolsmile
    p "did you suddenly age on me?"
    $ friendship += 5
    
    hide mel_smolsmile
    show mel_bigsmile
    
    mel "i'm eighty years old."
    mel "leave me alone."
    
    hide mel_bigsmile
    hide andie_laugh
    
    scene carbg_3
    
    mel "anyway... what do you think? do you think she's okay?"
    
    menu:
        "she sounded fine in the messages.":
            show andie_thinking
            p "she sounded fine in the messages."
            show mel_speaking
            mel "she's good at pretending."
            hide andie_thinking
            mel "remember that time with billy at homecoming?"
            mel "we didn't find out until the next month."
            hide mel_speaking
            show andie_annoyed
            p "oh, yeah."
            p "what a dick."
            hide andie_annoyed
            mel "yeah."
            show andie_side
            p "you think that happened again?"
            show mel_speaking
            mel "what? that billy hit her up in california and stood her up again?"
            hide andie_side
            hide mel_speaking
            show andie_laugh
            show mel_bigsmile
            p "don't get {i}sassy{/i} on me."
            hide mel_bigsmile
            mel "i'm... just saying."
            hide andie_laugh
            $ friendship += 10
            
        
        "maybe she has a horde of paparazzi surrounding her these days.":
            show andie_thinking
            p "maybe she has a horde of paparazzi surrounding her these days."
            show mel_smolsmile
            p "living out that LA life we always dreamed of."
            hide andie_thinking
            show andie_side
            p "think we'll be scouted tonight and get to quit college?"
            show mel_surprise
            mel "tired of college so soon?"
            hide andie_side
            p "i just want to collect checks in my underwear."
            hide mel_surprise
            show mel_smolsmile
            mel "don't we all."
            hide andie_side
            $ friendship += 5
    
        "i don't know.":
            
            show andie_boredawk
            p "i don't know."
            p "wouldn't claire tell us if something were wrong?"
            show mel_disappoint
            mel "i don't know."
            mel "sometimes... your best friends are the hardest people to tell."
       
    scene carbg_1
    
    p "i think she's fine."
    show andie_thinking
    p "unless..."
    hide andie_thinking
    p "do you know something that i don't?"
    
    "mel shakes her head, though she seems to be lost in thought again."
    
    "suddenly, i feel as though we've ended up back where we started and i shift awkwardly in my seat."
    
    "when did the mood get so dull?"
    
    show andie_dum
    
    p "hey, mind if i turn on some music?"
    
    hide andie_dum
    show mel_speaking
    mel "oh, sure. you can find some cds over there, or the radio, or plug in the aux cord."
    hide mel_speaking
    
    show andie_laugh
    p "did you just say..."
    p "{i}cds{/i}?"
    
    show mel_surprise
    mel "what?"
    hide mel_surprise
    
    show mel_speaking
    mel "i like having the physical disk."
    mel "it's tangible."
    hide mel_speaking
    
    p "alright."
    p "i guess i'll give your ol' records a shot."
    
    hide andie_laugh
    
    "i pull open the compartment before me, cases falling forward at the sudden intrusion."
    
    "my fingers sift through the different casings, eyes giving each a quick glance as i barrel on through, until
     one particular case catches my eye."
    
    "its case is the same size as the others but seems to be decorated by hand, like a mixtape of sorts."
    
    "i pull it out curiously, turning it over in my hands."
    
    show andie_thinking
    "{i}this is where i keep you in my mind{/i}, it reads."
    hide andie_thinking
    
    "the text is surrounded by stickers of guitars, hearts, and rainbows. spaced between the stickers are small
     doodles, some of which look much like mel with another girl."
    
    "i flip the case over in my hands in search of a track list, the first of which is..."
    
    show andie_dum
    
    "{i}girls like girls{/i} by lesbian jesus herself."
    
    "i blink at the case in my hands, not sure what to do next."
    
    "it feels as though i've stumbled upon something intimate, something mel was hiding."
    
    "should i say... something?"
    
    hide andie_dum
    
    menu:
        "put it back without a word.":
            "i lean forward to slip the case back in when mel's voice cuts through the silence."
            show mel_speaking
            mel "did you find--"
            hide mel_speaking
            show andie_side
            show mel_disappoint
            mel "oh."
            $ friendship -= 5
            hide andie_side 
            hide mel_disappoint
            
            
        "ask mel.":
            "i can barely collect my thoughts, choosing to run my index finger along the edge of the case in the meantime."
            show andie_disappoint
            "why is this so hard to say?"
            p "mel?"
            show mel_surprise
            mel "yeah?"
            hide mel_surprise
            "she glances at me before the question is able to leave my mouth."
            show mel_disappoint
            mel "oh."
            $ friendship -= 5
            hide mel_disappoint
            hide andie_disappoint
     
    scene carbg_2
    show andie_disappoint
    show mel_disappoint
    
    "we sit quietly, letting the hum of the car take over."
    
    "i can still feel my face flushed, heart drumming loudly in my chest."
    
    "this... isn't how mel wanted me to find out. i'm sure of that much."
    
    p "you--"
    
    mel "i--"
    
    hide andie_disappoint
    hide mel_disappoint
    show andie_side
    show mel_speaking
    
    mel "you first."
    
    hide mel_speaking
    hide andie_side
    show mel_disappoint
    show andie_disappoint
    
    p "i was just going to say..."
    
    menu:
        "you don't have to explain yourself to me.":
            $ friendship += 20
            p "you don't have to explain yourself to me."
            p "while this... isn't exactly ideal, i want this to be on your terms."
            "mel nods slowly as if weighing my words down, taking them at face value."
            hide mel_disappoint
            hide andie_disappoint
        
        "you have a girlfriend?":
            $ friendship -= 5
            hide andie_disappoint
            show andie_laugh
            p "you have a girlfriend?"
            p "that's great!"
            hide mel_disappoint
            show mel_surprise
            mel "i-- uh, thanks!"
            hide mel_surprise
            hide andie_laugh
        
        "you too?":
            $ friendship += 10
            $ andie_gay = "true"
            p "you too?"
            "i let go of my breath, allowing my shoulders to slump."
            hide mel_disappoint
            show mel_surprise
            p "me too."
            hide mel_surprise
            
    
    if andie_gay == "false":
        menu:
            "i'm also... {i}y'know{/i}.":
                $ friendship += 10
                $ andie_gay = "true"
                show andie_embarrassed
                p "i'm also... {i}y'know{/i}."
                show mel_surprise
                mel "oh!"
                hide mel_surprise
                show mel_smolsmile
                mel "i'm not surprised."
                hide mel_smolsmile
                show andie_dum
                p "what?!"
                show mel_bigsmile
                "mel shrugs her shoulders, grinning from ear to ear."
                mel "intuition."
                hide andie_dum
                hide mel_bigsmile
                
            "never mind.":
                "this is mel's moment."
                "i want her to have the floor regardless of what it is i may have to say."
                "mel comes first."
    
    "mel sighs."
    
    "i don't blame her. all i can seem to do is sigh too."
    
    show mel_speaking
    
    mel "she's... not my girlfriend."
    
    hide mel_speaking
    show mel_disappoint
    
    mel "{i}anymore.{/i}"
    
    show andie_side
    
    "i can see a tremble in her shoulders, which she stabilizes with a deep breath."
    
    "i give her my undivided attention. it's the least i can do."
    
    hide mel_disappoint
    show mel_speaking
    
    mel "we broke up after my brother outed me."
    
    hide andie_side
    show andie_dum
    
    p "eddie?!"
    
    hide mel_speaking
    show mel_smolsmile
    
    mel "it was an accident."
    
    hide mel_smolsmile
    show mel_disappoint
    
    mel "he mispoke... around our parents."
    
    hide andie_dum
    
    mel "and after that, i was just tired of hiding from them."
    
    hide mel_disappoint
    show mel_angry
    
    mel "but my parents weren't the most receptive."
    mel "they're convinced america's {i}brainwashed{/i} me."
    mel "as bizarre as that is."
    
    hide mel_angry
    show andie_annoyed
    
    p "that's terrible."
    
    show mel_disappoint
    
    mel "yeah..."
    mel "but they're my parents."
    mel "and they won't bother listening."
    mel "not much i can do when they won't give me the time of day."
    
    hide mel_disappoint
    hide andie_annoyed
    
    "we let a moment go and i twiddle my thumbs nervously, not feeling it was my place to prompt further conversation."
    
    show mel_speaking
    
    mel "it put a strain on our relationship."
    mel "kina and mine, i mean."
    mel "while my world was crashing down, i wasn't exactly receptive to her."
    
    hide mel_speaking
    show andie_disappoint
    
    p "that's okay."
    p "you were going through a lot."
    $ friendship += 5
    
    show mel_speaking
    
    mel "i--"
    
    hide andie_disappoint
    
    mel "i meant to tell you guys."
    mel "i was going to over this vacation."
    hide mel_speaking
    show mel_disappoint
    
    mel "i guess that's why i've been so... aloof."
    
    show andie_laugh
    
    p "{i}riiiight...{/i} because you've never really been."
    
    hide mel_disappoint
    show mel_smolsmile
    
    
    "the corners of her lips tilt up into a smile, soft yet reserved."
    $ friendship += 5
    
    hide mel_smolsmile
    show mel_speaking
    hide andie_laugh
    
    "she opens her mouth to speak."
    
    hide mel_speaking
    show mel_disappoint
    
    "then seems to think better of it."
    
    "until she finally blurts."
    
    hide mel_disappoint
    show mel_speaking
    
    mel "this... doesn't change anything, right?"
    
    hide mel_speaking
    show andie_dum
    
    p "what do you mean?"
    
    show mel_speaking
    
    mel "you're not..."
    
    hide mel_speaking
    show mel_disappoint 
    
    mel "{i}disappointed{/i}, are you?"
    
    if andie_gay == "true":
        hide andie_dum
        show andie_laugh
        p "mel..."
        p "i'm gay too."
        $ friendship += 5
        show mel_smolsmile
        mel "right."
        hide mel_smolsmile
        show mel_bigsmile
        mel "how could i forget?"
        
        
    if andie_gay == "false":
        p "mel..."
        p "you're one of my best friends."
        p "i'm not letting you go that easily."
        $ friendship += 5
        hide andie_dum
        show mel_smolsmile
        mel "right."
        "she nods her head, seemingly convincing herself of my words."
        hide mel_smolsmile
        show mel_bigsmile
        mel "{i}right.{/i}"
    
    show andie_dum
    
    p "now tell me..."
    
    hide andie_dum
    hide mel_bigsmile
    show mel_speaking

    mel "hm?"
    
    show andie_laugh
    
    p "what do you think of hayley kiyoko's new album?"
    
    hide mel_speaking
    show mel_bigsmile
    
    mel "do i even have to answer that?"
    mel "it's obviously my favorite."
    
    "suddenly, the next hour doesn't seem so difficult."
    "and as excited as i am to see claire, i can't help but want to bask in the glow of coming to an understanding
     with mel."
    "maybe, this trip was just what we needed after all."
    
    hide andie_laugh
    show andie_thinking
    
    if andie_gay == "false":
        "now... how do i come out to both of them?"
    
    if andie_gay == "true":
        "now... how do we come out to claire?"
    
    hide andie_thinking
    show andie_laugh
    "\[END.\]"
    "You collected [friendship] friendship points!"
    "THANKS FOR PLAYING THE GAME."
    "THIS IS A WORK IN PROGRESS."
    
    # This ends the game.

    return


label A1_04:
###############

  $ persistent.scene_number = "A1_04" # current scene


# Scene 04
# 
# Backgrounds:
# Apartment Interior(day)
# School Entrance (day)
# Office (day)
# Classroom (day)
# 
# Sprites:
# Beatrice, Hilda, Mr. + Mrs. Wilhelm, Ms. Claes, Mr. Bosworth, Ela
# 
# Music:
# Schooltheme
#
# Sound Effects:
# door closing
#
#-# >open to apartment interior (day)
scene mainbuilding
with Dissolve(0.5)
#--#

$ renpy.music.set_volume(0.5)
play music "music/effects/City Night Ambience.mp3" fadein 1.0 loop

n "Morning comes almost too quickly. I thought days like this were supposed to take forever to get to, like Christmas morning, or the day after a hard test."

n "I zone out through breakfast, the entire car ride, and up to our arrival at the main gate."

n "The gate in question isn't particularly imposing, or really even all that scary."

n "I'm not even that nervous as I cross the gate and into the main campus, populated with a few students wandering the walkways to and from the various buildings."

n "But, I still have this feeling, the one that sticks in the back of your head, asking things like \"did I forget to lock the door,\" or  \"do I look weird walking around here?\""

n "I try my best to shake it off, but it's no good."

show hilda P2_E2:
  alpha 0.0 xalign 0.0 yalign -0.2
  easein 1.0 xalign 0.1 alpha 1.0
with Dissolve(0.5)

show beatrice P2_E1:
  alpha 0.0 xalign 1.00 yalign 1.0
  easein 1.0 xalign 0.9 alpha 1.0
with Dissolve(0.5)

show mum P1_E2:
  xalign 0.4 yalign -0.2 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.4 yalign -0.2 alpha 1.0
with Dissolve(0.5)

show dad P2_E2:
  xalign 0.7 yalign 1 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.6 yalign 1 alpha 1.0
with Dissolve(0.5)
#--#

mum "\"Erik, how are you feeling? You haven't said a thing since we got here.\""

erik "\"I'm alright. Just... \""

mum "\"Nervous?\""

erik "\"A little.\""

n "Mum nods in understanding and pats me on the shoulder."

mum "\"Just tell me if you don't feel good and we'll go somewhere so you can take a break.\""

stop music fadeout 1.0

erik "\"Sure.\""

$ renpy.music.set_volume(1.0)
play music "music/Be Green Afternoon.mp3" fadein 1.0 loop

n "The main building we're approaching is the largest on campus; it's three stories tall, and definitely very old. A mass of ivy coats the entrance, adding a natural green patina to the stonework."

mum "\"Isn't this building pretty, Erik? This is where you'll be going for classes.\""

erik "\"It's nice. I like older buildings like this. It’s kind of like the old church back at home.\""

#-# >Screen Shake

scene entrance1
with hpunch
#--#

Voice "\"GOOD MORNING!\""

n "Suddenly, a booming voice emerges from the building. Despite the distance, I can hear it very clearly. Is there a loudspeaker nearby?"

n "A large man comes out from behind the archway of the entrance. He's waving at us to come inside."

dad "\"Ah, that'll be Dr. Bosworth.\""

hilda "\"Is he always so...?\""

n "I tilt my head disbelievingly toward the man."

dad "\"...Yes.\""

#-# >Bosworth enter right

show bosworth P1_E4:
  offscreenright
  alpha 0.0 xalign 0.9 yalign 0.0
  easein 1.0 xalign 0.8 alpha 1.0
#--#

bosworth "\"Hello again, Mr. and Mrs Wilhelm! So good to see you again, yes, yes...\""

n "The large man – Dr. Bosworth – is vigorously shaking my parent's hands, as if they were old friends seeing each other again."

show bosworth P1_E2
with Dissolve (0.25)

bosworth "\"And this must be Erik!\""

n "He approaches me. Despite us being almost similar in height, I can't help but feel... diminished by his presence."

bosworth "\"Your parents have already told me so much about you, Erik. Such a gentleman to be joining our halls!\""

n "He steps back and takes a bow."

bosworth "\"On behalf of all the staff here, welcome to Saint Dymphna's Privatgymnasium.\""

erik "\"Uh, thanks...\""

n "He claps his hands together loud enough to scare some of the nearby birds away."

bosworth "\"Well, then, we have a lot of ground to cover today! There's some paperwork inside for you and your parents to sign, the tour, the ritual...\""

erik "\"Ritual?\""

show bosworth P1_E4
with Dissolve (0.25)

bosworth "\"Kidding, kidding!\""

n "He herds us inside with a jolly laugh."

#-# >Fade to interior building

scene mainlobby
with Dissolve(0.5)
show bosworth P1_E2:
  xalign 0.9 yalign 0.0 alpha 0.0
  easein 0.5 alpha 1.0
show mum P1_E2:
  xalign 0.3 yalign 0.0 alpha 0.0
  easein 0.5 alpha 1.0
#--#

bosworth "\"If you don't mind, I'd like to begin with a short one-on-one with Erik. Please, make yourselves comfortable in the lobby here.\""

mum "\"We'll be right here, then.\""

#-# >Fade to office (day)

image BosworthOffice:
  im.Scale("images/Backgrounds/BosworthOffice.png", config.screen_width, config.screen_height)
scene BosworthOffice
with Dissolve (0.5)

n "Bosworth's office is very organized – bookshelves containing dozens of volumes, paperwork neatly stacked, and a desk polished to a mirror shine. It's almost intimidatingly perfect."

n "He settles into his massive desk chair and shuffles a few papers. Gesturing to the chair opposite his, he offers me a seat."

show bosworth P1_E2:
  xalign 0.8 yalign 0.0 alpha 0.0
  easein 0.5 alpha 1.0
  

n "..."

n "It’s incredibly comfortable. Clearly, this school spares no expense."

bosworth "\"Now, let's get down to business. Erik, I just have a few questions for you. We like to get a feel for new students by asking them about their comfort levels and what they want out of this school.\""

erik "\"Okay, makes sense.\""

bosworth "\"Glad to hear it! So, my first question: do you prefer lessons in English, or another language? Does one or the other make you more comfortable?\""

erik "\"I don't have any preference.\""

show bosworth P1_E4
with Dissolve (0.25)

bosworth "\"Splendid! I have just the teacher for you. Ms. Claes is one of our English speaking instructors, and I think you'll get along with her just fine.\""

show bosworth P1_E2
with Dissolve (0.25)

erik "\"Sounds good to me. I take it English classrooms have students from a wider variety of countries?\""

bosworth "\"Ha ha! You're a smart, lad. Yes, that's correct – we have a lot of people coming in from all over Europe, so we do our best to accommodate everyone.\""

bosworth "\"If you wanted a German classroom, you'd probably see more people who are native to Germany, Switzerland, or Austria, which some students would be more comfortable with.\""

erik "\"Makes sense.\""

n "Bosworth nods in agreement, marking my responses on a sheet of paper."

bosworth "\"Indeed, indeed. Next question: How do you feel about coming here?\""

n "I shift a little bit in the chair. I wasn’t expecting such a frank line of questioning."

erik "\"I'm kind of nervous moving here. It's a new school, after all.\""

n "In truth, I'm kind of freaking out inside. This is all a lot to take in."

n "Even though I was anticipating this."

n "My leg twinges a little bit, as if reacting to my state of mind."

n "Bosworth smiles sympathetically."

bosworth "\"It's not uncommon for our students to feel what you're feeling, Erik. We at St. Dymphna's are always trying our best to listen to when students aren't well or are feeling stressed.\""

n "His words are well-practiced and clearly part of a much longer speech – something of which he must have had years, maybe decades, of practicing his delivery."

n "Nonetheless, I feel a little better that he said it."

bosworth "\"Is there anything you need before you get started at school? Anything you want me to tell your teachers or supervisors?\""

n "Once again his words are practiced, yet genuine."

erik "\"Where can I go for a good walk?\""

show bosworth P1_E4
with Dissolve (0.25)

n "Bosworth chuckles at my response."

bosworth "\"I'm happy to inform you that the campus has an excellent series of footpaths for you to use at your leisure! When you take the tour, I'm sure your guide will do their best to point that out to you.\""

show bosworth P1_E2
with Dissolve (0.25)

bosworth "\"And my last question, before I let you go on your way: Would you like to meet Ms. Claes right now? Your parents and I have just a few more forms to fill out, but I'd like for you to meet her before your tour.\""

erik "\"Uh, sure. It would be nice to meet her.\""

bosworth "\"Wonderful! I'll give her a call. In the meantime, why don't you let your family know you're all done with me?\""

erik "\"Sure.\""

play sound "music/effects/door open and close.mp3"

#-# >Fade to interior building 2
scene mainlobby
with Dissolve(1.0)
#--#

show mum P1_E2:
  xalign 0.0 yalign -0.2 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.1 yalign -0.2 alpha 1.0
with Dissolve(0.5)

show dad P2_E2:
  xalign 0.2 yalign 1 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.3 yalign 1 alpha 1.0
with Dissolve(0.5)

show hilda P2_E2:
  alpha 0.0 xalign 0.4 yalign -0.2
  easein 1.0 xalign 0.5 alpha 1.0
with Dissolve(0.5)

show beatrice P2_E1:
  alpha 0.0 xalign 0.6 yalign 1.0
  easein 1.0 xalign 0.7 alpha 1.0
with Dissolve(0.5)

erik "\"Okay, all done.\""

mum "\"How did it go, Erik?\""

beatrice "\"Is he nice?\""

erik "\"It went well, and yeah, Dr. Bosworth is actually pretty nice.\""

bosworth "\"I'm glad to hear!\""

show mum P1_E2:
  xalign 0.1 yalign -0.2 zoom 1.0
  easein 1.0 xalign 0.0

show dad P2_E2:
  xalign 0.3 zoom 1.0
  easein 1.0 xalign 0.2

show hilda P2_E2:
  xalign 0.5
  easein 1.0 xalign 0.4

show beatrice P2_E1:
  xalign 0.7
  easein 1.0 xalign 0.6

show bosworth P1_E2:
  xalign 1.0 yalign 0.0
with Dissolve(0.5)

n "I turn around, not realizing the man I'm talking about has already finished his call."

bosworth "\"Ms. Claes is in her office at the end of this hallway, Erik. She'll be expecting you in a minute. Now, I'll need to steal you two away, Mr. and Mrs. Wilhelm. Just a few bits and pieces of last-minute paperwork...\""

show bosworth P1_E2:
    easein 1.0 alpha 0.0

show mum P1_E2:
  easein 1.0 alpha 0.0

show dad P2_E2:
  easein 1.0 alpha 0.0

n "He guides them into the office and I'm left with Beatrice and Hilda."

#-# >Beatrice and Hilda enter in from left

hide dad
hide mum
hide bosworth

erik "\"Well, shall we?\""

n "My sisters nod in agreement."

play sound "music/effects/Knock Knock.mp3"

n "I lead the way down to Ms. Claes' office and knock gingerly on the door a few times."

Voice "\"Come in.\""

#-# >fade to office (day)
scene classroom1
with Dissolve (0.5)
play sound "music/effects/door open and close.mp3"
#--#

show claes P1_E1:
  alpha 0.0 xalign 0.8 yalign -0.25
  easein 1.0 xalign 0.7 alpha 1.0
#--#
show hilda P1_E2:
  offscreenleft
  alpha 0.0 xalign 0.2 yalign -0.2
  easein 1.0 xalign 0.3 alpha 1.0
show beatrice P1_E1:
  offscreenleft
  alpha 0.0 xalign -0.1 yalign 1.0
  easein 1.0 xalign 0.0 alpha 1.0

n "A young woman, probably a few years older than Hilda, greets us."

n "Her voice is prim, proper, and polite – very teacher-esque."

erik "\"Thanks. I was told you'll be my homeroom teacher?\""

claes "\"That is correct. I teach English, primarily, but I also hold some of the mathematics courses here on campus.  Oh, and you two are...?\""

beatrice "\"I'm Erik's older sister, Beatrice Wilhelm.\""

hilda "\"And I'm his other older sister, Brunhilde Wilhelm. Call me Hilda!\""

n "They both shake hands with Ms. Claes, who smiles warmly."

claes "\"It's nice to see family members so interested in this school.  Where are you coming from?\""

hilda "\"We actually live in Vienna, but Erik here is from Basel-Stadt.\""

claes "\"Oh! Have you shown him the city? We offer trips into the city on most weekends.\""

beatrice "\"We have; Erik seemed to like it a lot!\""

erik "\"It's a nice city – I'd like to explore it some more soon.\""

claes "\"Have you taken the tour of the campus yet?\""

erik "\"Not yet – we'll be going after my parents finish up some paperwork with Dr. Bosworth.\""

play sound "music/effects/door open and close.mp3"

#-# >Ela enters from right
show ela P1_E1:
  offscreenright
  alpha 0.0 xalign 1.1 yalign -0.25
  easein 1.0 xalign 1.0 alpha 1.0
#--#

n "Suddenly, a young girl enters from outside."

Voice "\"Is Erik here?\""

erik "\"Uh, yes, that's me.\""

show ela P1_E2
with Dissolve (0.25)

ela "\"Great! I'm Ela. I'll be giving you the tour of the campus!\""

n "Ela is a dark-skinned, slender girl, about my age. Her uniform is neatly pressed – almost like it's out of the glossy pamphlets the school sent me. Her hair tumbles out from beneath her beret."

erik "\"Nice to meet you, Ela.\""

#-# >ela_smile.png
show ela P1_E1
with Dissolve(0.25)
#--#

ela "\"It's nice to meet you too, Erik.\""

ela "\"Now, let's get started, shall we? Right this way, please!\""

stop music fadeout 1.0

#-# >end

scene PitchBlack
#--#




########

jump A1_05 # jump A?_??

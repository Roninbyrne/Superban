from pyrogram import Client, filters
from pyrogram.types import Message

fixed_texts = [
    """ᴀʟʟᴇɴ 
93. HIV that causes AIDS, first starts destroying: 
(1) Leucocytes 
(2) Helper T- Lymphocytes 
(3) Thrombocytes 
(4) B- Lymphocytes


Sol. NO                                ᴍᴏᴅᴜʟᴀʀ 
2 
 is not used as food preservative.


103. Identify the pair of heterosporous pteridophytes 
among the following : 
(1) Selaginella and Salvinia 
(2) Psilotum and Salvinia 
(3) Equisetum and Salvinia 
(4) Lycopodium and Selaginella 
Ans. (1)  

104. Frequency of recombination between gene pairs on 
same chromosome as a measure of the distance 
between genes to map their position on  
chromosome, was used for the first time by  


(1) Sutton and Boveri (2) Alfred Sturtevant 

(3) Henking       (4) Thomas Hunt Morgan 
Ans. (2)""",

    """ᵃˡˡᵉⁿ ᵐᵒᵈᵘˡᵉˢ (²⁰²⁴ - ²⁵ )

ᵈⁱˢᶜᵒᵛᵉʳʸ ᵒᶠ ʳᵉ
ʳᵉ ᵉˣⁱˢᵗ ᵒⁿˡʸ ⁱⁿ ᵖʳᵒᵏᵃʳʸᵒᵗᵉˢ (ᵇᵃᶜᵗᵉʳⁱᵃ)
ʳᵉ ⁱˢ ᵃ ᵖᵃʳᵗ ᵒᶠ ᵈᵉᶠᵉⁿᶜᵉ ˢʸˢᵗᵉᵐ ᵒᶠ ᵇᵃᶜᵗᵉʳⁱᵃ ʷʰⁱᶜʰ ᵖʳᵒᵛⁱᵈᵉˢ ᵈᵉᶠᵉⁿᶜᵉ ᵃᵍᵃⁱⁿˢᵗ ᵛⁱʳᵘˢᵉˢ (ᵇᵃᶜᵗᵉʳⁱᵒᵖʰᵃᵍᵉ) ʳᵉ ⁿᵉᵛᵉʳ ᶜᵘᵗ ⁱᵗˢ ᵒʷⁿ ᵇᵃᶜᵗᵉʳⁱᵃˡ ᵈⁿᵃ ᵇᵉᶜᵃᵘˢᵉ ᵗʰᵉⁱʳ ʳᵉˢᵗʳⁱᶜᵗⁱᵒⁿ ˢⁱᵗᵉ ⁱˢ ᵐᵒᵈⁱᶠⁱᵉᵈ ᵇʸ ᵐᵉᵗʰʸˡᵃᵗⁱᵒⁿ. ⁱⁿ ᵗʰᵉ ʸᵉᵃʳ ¹⁹⁶³, ᵗʰᵉ ᵗʷᵒ ᵉⁿᶻʸᵐᵉˢ ʳᵉˢᵖᵒⁿˢⁱᵇˡᵉ ᶠᵒʳ ʳᵉˢᵗʳⁱᶜᵗⁱⁿᵍ ᵗʰᵉ ᵍʳᵒʷᵗʰ ᵒᶠ ᵇᵃᶜᵗᵉʳⁱᵒᵖʰᵃᵍᵉ ⁱⁿ ᵉˢᶜʰᵉʳⁱᶜʰⁱᵃ ᶜᵒˡⁱ ʷᵉʳᵉ ⁱˢᵒˡᵃᵗᵉᵈ. ᵒⁿᵉ ᵒᶠ ᵗʰᵉˢᵉ ᵃᵈᵈᵉᵈ ᵐᵉᵗʰʸˡ ᵍʳᵒᵘᵖˢ ᵗᵒ ᵈⁿᵃ, ʷʰⁱˡᵉ ᵗʰᵉ ᵒᵗʰᵉʳ ᶜᵘᵗ ᵈⁿᵃ. ᵗʰᵉ ˡᵃᵗᵉʳ ʷᵃˢ ᶜᵃˡˡᵉᵈ ʳᵉˢᵗʳⁱᶜᵗⁱᵒⁿ ᵉⁿᵈᵒⁿᵘᶜˡᵉᵃˢᵉ.  ᵗʰᵉ ᶠⁱʳˢᵗ ʳᵉˢᵗʳⁱᶜᵗⁱᵒⁿ ᵉⁿᵈᵒⁿᵘᶜˡᵉᵃˢᵉ–ʰⁱⁿᵈ ⁱⁱ.  ʰⁱⁿᵈ ⁱⁱ ᶠᵘⁿᶜᵗⁱᵒⁿⁱⁿᵍ ᵈᵉᵖᵉⁿᵈᵉᵈ ᵒⁿ ᵃ ˢᵖᵉᶜⁱᶠⁱᶜ ᵈⁿᵃ ⁿᵘᶜˡᵉᵒᵗⁱᵈᵉ ˢᵉᵠᵘᵉⁿᶜᵉ ʷᵃˢ ⁱˢᵒˡᵃᵗᵉᵈ ᵃⁿᵈ ᶜʰᵃʳᵃᶜᵗᵉʳⁱˢᵉᵈ ᶠⁱᵛᵉ ʸᵉᵃʳˢ ˡᵃᵗᵉʳ. ⁱᵗ ʷᵃˢ ᶠᵒᵘⁿᵈ ᵗʰᵃᵗ ʰⁱⁿᵈ ⁱⁱ ᵃˡʷᵃʸˢ ᶜᵘᵗ ᵈⁿᵃ ᵐᵒˡᵉᶜᵘˡᵉˢ ᵃᵗ ᵃ ᵖᵃʳᵗⁱᶜᵘˡᵃʳ ᵖᵒⁱⁿᵗ ᵇʸ ʳᵉᶜᵒᵍⁿⁱˢⁱⁿᵍ ᵃ ˢᵖᵉᶜⁱᶠⁱᶜ ˢᵉᵠᵘᵉⁿᶜᵉ ᵒᶠ ˢⁱˣ ᵇᵃˢᵉ ᵖᵃⁱʳˢ. ᵇᵉˢⁱᵈᵉˢ ʰⁱⁿᵈ ⁱⁱ, ᵗᵒᵈᵃʸ ʷᵉ ᵏⁿᵒʷ ᵐᵒʳᵉ ᵗʰᵃⁿ ⁹⁰⁰ ʳᵉˢᵗʳⁱᶜᵗⁱᵒⁿ ᵉⁿᶻʸᵐᵉˢ ᵗʰᵃᵗ ʰᵃᵛᵉ ᵇᵉᵉⁿ ⁱˢᵒˡᵃᵗᵉᵈ ᶠʳᵒᵐ ᵒᵛᵉʳ ²³⁰ ˢᵗʳᵃⁱⁿˢ ᵒᶠ ᵇᵃᶜᵗᵉʳⁱᵃ ᵉᵃᶜʰ ᵒᶠ ʷʰⁱᶜʰ ʳᵉᶜᵒᵍⁿⁱˢᵉ ᵈⁱᶠᶠᵉʳᵉⁿᵗ ʳᵉᶜᵒᵍⁿⁱᵗⁱᵒⁿ ˢᵉᵠᵘᵉⁿᶜᵉˢ. ᵉᶜᵒʳⁱ ʷᵃˢ ᵈⁱˢᶜᵒᵛᵉʳᵉᵈ ᵇʸ ᵃʳᵇᵉʳ, ˢᵐⁱᵗʰ, ᵃⁿᵈ ⁿᵃᵗʰᵃⁿ’ˢ""",

    """ᵃˡˡᵉⁿ ⁱⁿˢᵗⁱᵗᵘᵗᵉ 
ᵇⁱᵒᵗᵉᶜʰⁿᵒˡᵒᵍʸ:

⁰³. ᵇⁱᵒᵗᵉᶜʰⁿᵒˡᵒᵍⁱᶜᵃˡ ᵃᵖᵖˡⁱᶜᵃᵗⁱᵒⁿˢ ⁱⁿ ᵐᵉᵈⁱᶜⁱⁿᵉ ᵗʰᵉ ʳᵉᶜᵒᵐᵇⁱⁿᵃⁿᵗ ᵈⁿᵃ ᵗᵉᶜʰⁿᵒˡᵒᵍⁱᶜᵃˡ ᵖʳᵒᶜᵉˢˢᵉˢ ʰᵃᵛᵉ ᵐᵃᵈᵉ ⁱᵐᵐᵉⁿˢᵉ ⁱᵐᵖᵃᶜᵗ ⁱⁿ ᵗʰᵉ ᵃʳᵉᵃ ᵒᶠ ʰᵉᵃˡᵗʰᶜᵃʳᵉ ᵇʸ ᵉⁿᵃᵇˡⁱⁿᵍ ᵐᵃˢˢ ᵖʳᵒᵈᵘᶜᵗⁱᵒⁿ ᵒᶠ ˢᵃᶠᵉ ᵃⁿᵈ ᵐᵒʳᵉ ᵉᶠᶠᵉᶜᵗⁱᵛᵉ ᵗʰᵉʳᵃᵖᵉᵘᵗⁱᶜ ᵈʳᵘᵍˢ. ᶠᵘʳᵗʰᵉʳ, ᵗʰᵉ ʳᵉᶜᵒᵐᵇⁱⁿᵃⁿᵗ ᵗʰᵉʳᵃᵖᵉᵘᵗⁱᶜˢ ᵈᵒ ⁿᵒᵗ ⁱⁿᵈᵘᶜᵉ ᵘⁿʷᵃⁿᵗᵉᵈ ⁱᵐᵐᵘⁿᵒˡᵒᵍⁱᶜᵃˡ ʳᵉˢᵖᵒⁿˢᵉˢ ᵃˢ ⁱˢ ᶜᵒᵐᵐᵒⁿ ⁱⁿ ᶜᵃˢᵉ ᵒᶠ ˢⁱᵐⁱˡᵃʳ ᵖʳᵒᵈᵘᶜᵗˢ ⁱˢᵒˡᵃᵗᵉᵈ ᶠʳᵒᵐ ⁿᵒⁿ-ʰᵘᵐᵃⁿ ˢᵒᵘʳᶜᵉˢ. ᵃᵗ ᵖʳᵉˢᵉⁿᵗ, ᵃᵇᵒᵘᵗ ³⁰ ʳᵉᶜᵒᵐᵇⁱⁿᵃⁿᵗ ᵗʰᵉʳᵃᵖᵉᵘᵗⁱᶜˢ ʰᵃᵛᵉ ᵇᵉᵉⁿ ᵃᵖᵖʳᵒᵛᵉᵈ ᶠᵒʳ ʰᵘᵐᵃⁿ-ᵘˢᵉ ᵗʰᵉ ʷᵒʳˡᵈ ᵒᵛᵉʳ. ⁱⁿ ⁱⁿᵈⁱᵃ, ¹² ᵒᶠ ᵗʰᵉˢᵉ ᵃʳᵉ ᵖʳᵉˢᵉⁿᵗˡʸ ᵇᵉⁱⁿᵍ ᵐᵃʳᵏᵉᵗᵉᵈ.(ᵃ) ᵍᵉⁿᵉᵗⁱᶜᵃˡˡʸ ᵉⁿᵍⁱⁿᵉᵉʳᵉᵈ ⁱⁿˢᵘˡⁱⁿ  ⁱᵗ ⁱˢ ᵃ ᵖʳᵒᵗᵉⁱⁿᵃᶜᵉᵒᵘˢ ʰᵒʳᵐᵒⁿᵉ ʰᵃᵛⁱⁿᵍ ⁵¹ ᵃᵐⁱⁿᵒ ᵃᶜⁱᵈˢ ᵃʳʳᵃⁿᵍᵉᵈ ⁱⁿ ᵗʷᵒ ᵖʳᵒⁱⁿˢᵘˡⁱⁿˢ – ˢᵖᵒˡʸᵖᵉᵖᵗⁱᵈᵉˢ ᵃ ᵃⁿᵈ ᵇ ʰᵃᵛⁱⁿᵍ ²¹ ᵃⁿᵈ ˢˢ³⁰ ᵃᵐⁱⁿᵒ ᵃᶜⁱᵈˢ, ʳᵉˢᵖᵉᶜᵗⁱᵛᵉˡʸ ᵃⁿᵈ ˢˢʲᵒⁱⁿᵉᵈ ᵇʸ ˢ-ˢ ᵈⁱˢᵘˡᵖʰⁱᵈᵉ ᵇʳⁱᵈᵍᵉˢ.  ᵐᵃⁿᵃᵍᵉᵐᵉⁿᵗ ᵒᶠ ᵃᵈᵘˡᵗ-ᵒⁿˢᵉᵗ ᵈⁱᵃᵇᵉᵗᵉˢ ᵃ ᵖᵉᵖᵗⁱᵈᵉˢ ˢⁱˢ ᵖᵒˢˢⁱᵇˡᵉ ᵇʸ ᵗᵃᵏⁱⁿᵍ ⁱⁿˢᵘˡⁱⁿ ᵃᵗ ʳᵉᵍᵘˡᵃʳ ˢˢⁱⁿˢᵘˡⁱⁿˢˢᵗⁱᵐᵉ ⁱⁿᵗᵉʳᵛᵃˡˢ. ʷʰᵃᵗ ʷᵒᵘˡᵈ ᵃ ᵈⁱᵃᵇᵉᵗⁱᶜ ᵖᵃᵗⁱᵉⁿᵗ ᵈᵒ ⁱᶠ ᵉⁿᵒᵘᵍʰ ʰᵘᵐᵃⁿ ⁱⁿˢᵘˡⁱⁿᵇ ᵖᵉᵖᵗⁱᵈᵉʷᵃˢ ⁿᵒᵗ ᵃᵛᵃⁱˡᵃᵇˡᵉ? ⁱᶠ ʸᵒᵘ ᵈⁱˢᶜᵘˢˢ ᵗʰⁱˢ, ᶠʳᵉᵉ ᶜ ᵖᵉᵖᵗⁱᵈᵉʸᵒᵘ ʷᵒᵘˡᵈ ˢᵒᵒⁿ ʳᵉᵃˡⁱˢᵉ ᵗʰᵃᵗ ᵒⁿᵉ ᵐᵃᵗᵘʳᵃᵗⁱᵒⁿ ᵒᶠ ᵖʳᵒ-ⁱⁿˢᵘˡⁱⁿ ⁱⁿᵗᵒ ⁱⁿˢᵘˡⁱⁿ (ˢⁱᵐᵖˡⁱᶠⁱᵉᵈ)ʷᵒᵘˡᵈ ʰᵃᵛᵉ ᵗᵒ ⁱˢᵒˡᵃᵗᵉ ᵃⁿᵈ ᵘˢᵉ ⁱⁿˢᵘˡⁱⁿ""",

    """FINAL TEST SERIES for ALLEN

Test - 1

CODE-A

Time: 3 Hrs. 20 Mins.

Chemistry: Some Basic Concepts of Chemistry, Structure of Aton, Classification of Elements and Periodicity in Properties

Botany : The Living World, Biological Classification

Zoology: Animal Kingdom

Instructions:

(i) There are two sections in each subject, i.e. Section-A & Section-B. You have to attempt all 35 questions from

Section-A & only 10 questions from Section-B out of 15.

(ii) Each question carries 4 marks. For every wrong response 1 mark shall be deducted from the total score.

Unanswered / unattempted questions will be given no marks.

( iii) Use blue/black ballpoint pen only to darken the appropriate circle.

(iv) Mark should be dark and completely fill the circle.

(v) Dark only one circle for each entry.

(vi) Dark the circle in the space provided only.

(vii) Rough work must not be done on the Answer sheet and do not use white-fluid or any other rubbing material on the Answer sheet.

PHYSICS

Choose the correct answer:

SECTION-A

1. A physical quantity P is related with four quantities

a, b, c and das f

follows: Pab

21/2

The percentage error in the measurement of a, b, cand dare 1%, 2%, 3% and 4% respectively. The maximum percentage error in Pis

(1) 23.5%

(3) 16%

(2) 12.5%

(4) 8%

2. A ball is dropped from a building of height 40 m. Simultaneously another ball is thrown up with a speed 20 m/s. The relative speed of first ball w.r.t. second ball at f1s is (g = 10 m/s²)

(1) 20 m/s

(3) 30 m/s

(2) 10 m/s

(4) Zero

3. Radius of a circle is 2.22 m. According to the rule of significant figures, the area of circle is

(1) 15.475 m² (3) 15.48 m²

(2) 15.4 m² (4) 15.5 m²

4. If mass m is expressed as m Gh°C°, where G Universal gravitation constant, h Planck's constant, C= Speed of light, then is equal to bc

(2) 1

(3) 2

(4)

(1)""",

    """A ALLEN CLASSROOM CONTACT PROGRAMME
CAREER INSTITUTE
bath 0 sees a OSE TST) (Academic Session : 2020-2021)
Enthusiast, Leader & Achiever Course
PHASE : SRL-2
TARGET : PRE-MEDICAL : 2021
Test Type : MINOR Test Pattern : NEET (UG)""",

    """𝕮𝕬𝖑𝖑𝖊𝖓:

𝕻𝖆𝖌𝖊

=Â»

𝕷𝕬𝕾𝕾𝕽𝕺𝕺𝕸 𝕮𝕺𝕹𝕿𝕬𝕮𝕿 𝕻𝕽𝕺𝕲𝕽𝕬𝕸𝕸𝕰
𝕮𝕬𝕽𝕰𝕰𝕽 𝕴𝕹𝕾𝕿𝕴𝕿𝖀𝕿𝕰
𝖇𝖆𝖙𝖍 0 𝖘𝖊𝖊𝖘 𝖆 𝕺𝕾𝕰 𝕿𝕾𝕿) (𝕬𝖈𝖆𝖉𝖊𝖒𝖎𝖈 𝕾𝖊𝖘𝖘𝖎𝖔𝖓 : 2022-2024)
𝕰𝖓𝖙𝖍𝖚𝖘𝖎𝖆𝖘𝖙, 𝕷𝖊𝖆𝖉𝖊𝖗 & 𝕬𝖈𝖍𝖎𝖊𝖛𝖊𝖗 𝕮𝖔𝖚𝖗𝖘𝖊
𝕻𝕳𝕬𝕾𝕰 : 𝕾𝕽𝕷-2
𝕿𝕬𝕽𝕲𝕰𝕿 : 𝕻𝕽𝕰-𝕸𝕰𝕯𝕴𝕮𝕬𝕷 : 2024
𝕿𝖊𝖘𝖙 𝕿𝖞𝖕𝖊 : 𝕸𝕴𝕹𝕺𝕽 𝕿𝖊𝖘𝖙 𝕻𝖆𝖙𝖙𝖊𝖗𝖓 : 𝕹𝕰𝕰𝕿 (𝖀𝕲)
𝕿𝕰𝕾𝕿 𝕯𝕬𝕿𝕰 : 10-01-2024
A>21>7=Z3
𝕾𝕿 𝕬𝖊𝖓 𝕺𝖓 9. 𝕬𝖓𝖘 (3)
𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 28
𝕾𝕰𝕮𝕿𝕴𝕺𝕹-𝕬 10. 𝕬𝖓𝖘(1)
1. 𝕬𝖓𝖘 (4) 𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 25
𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 27 & 34. 11. 𝕬𝖓𝖘(2)
2. 𝕬𝖓𝖘 (2) 𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 23
𝕹𝖔. 𝖔𝖋 𝖒𝖊𝖎𝖔𝖙𝖎𝖈 𝖉𝖎𝖛𝖎𝖘𝖎𝖔𝖓𝖘 𝖗𝖊𝖖𝖚𝖎𝖗𝖊𝖉 𝖙𝖔 𝖋𝖔𝖗𝖒 𝖘𝖊𝖊𝖉𝖘 12. 𝕬𝖓𝖘(2)

𝖎𝖓 𝖆𝖓𝖌𝖎𝖔𝖘𝖕𝖊𝖗𝖒 = 5/4 𝖝 𝖓𝖚𝖒𝖇𝖊𝖗 𝖔𝖋 𝖘𝖊𝖊𝖉𝖘. 𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 26

3. 𝕬𝖓𝖘(4) 13. 𝕬𝖓𝖘(3)
𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝕻𝖆𝖌𝖊 27, 29 𝖆𝖓𝖉 38. 𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 21

4. 𝕬𝖓𝖘(2) 14. 𝕬𝖓𝖘(1)
𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 10, 11, 24 𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴 𝖕𝖆𝖌𝖊 22""",

    """14. Statement I : There are three major ways in which 
different cells handle pyruvic acid produced by 
glycolysis. 
Statement II : The reducing agent is NAD which 
is oxidized to NADH + H in both alcoholic 
fermentation and lactic acid fermentation. 

(1) Both Statement I and Statement II are correct. 

(2) Both Statement I and Statement II are incorrect 

(3) Statement I is incorrect while Statement II is correct 

(4) Statement I is correct while Statement II is incorrect. 

115. If in a pond there were 40 lotus plants last year 
and through reproduction 16 new plants are 
added then the birth rate in the population 
is......... offspring per lotus per year. 

(1) 2.5        (2) 0.4        (3) 1.0      (4) 0.1 
    
116. Between which, among the following, the 
relationship is an example of mutualism ? 

(1) Cuscuta and hedge plant 

(2) Fig and wasp 

(3) Sea anemone and clown fish 

(4) Whale and barnacles 
117. Given below are 
statements : One is labelled as 
Assertion A and the other is labelled as Reason R : 
Assertion (A) :- Plants have evolved an astonishing 
variety of morphological and chemical defences 
against herbivores. 
Reason (R) :- The problem of predation is 
particularly severe for plants as unlike animals, 
they cannot run away from their predators. 
In the light of the above statements, choose the 
correct answer from the options given below : 

(1) Both A and R are true but R is NOT the 
correct explanation of 

(2) Both A and R are true and R is the correct 
explanation  of A 

(3) A is true but R is false 

(4) A is false but R is true""",

    """𝕬𝕷𝕷𝕰𝕹 𝕺𝕴𝕲𝕴𝕿𝕬𝕷 

𝕴𝖓𝖙𝖗𝖔𝖉𝖚𝖈𝖙𝖎𝖔𝖓 𝖔𝖋 𝖈𝖎𝖗𝖈𝖚𝖑𝖆𝖗 𝖒𝖔𝖙𝖎𝖔𝖓

𝕴𝖑𝖑𝖚𝖘𝖙𝖗𝖆𝖙𝖎𝖔𝖓 2.𝕬 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊 𝖒𝖔𝖛𝖊𝖘 𝖎𝖓 𝖆 𝖈𝖎𝖗𝖈𝖑𝖊 𝖔𝖋 𝖗𝖆𝖉𝖎𝖚𝖘 𝖔𝖋 0.5 𝖒 𝖆𝖙 𝖆 𝖘𝖕𝖊𝖊𝖉 𝖙𝖍𝖆𝖙 𝖎𝖓𝖈𝖗𝖊𝖆𝖘𝖊𝖘 𝖚𝖓𝖎𝖋𝖔𝖗𝖒𝖑𝖞. 𝕱𝖎𝖓𝖉 𝖙𝖍𝖊 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖆𝖈𝖈𝖊𝖑𝖊𝖗𝖆𝖙𝖎𝖔𝖓 𝖔𝖋 𝖙𝖍𝖊 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊, 𝖎𝖋 𝖎𝖙𝖘 𝖘𝖕𝖊𝖊𝖉 𝖈𝖍𝖆𝖓𝖌𝖊𝖘 𝖋𝖗𝖔𝖒 2 𝖒𝖘–1𝖙𝖔 4 𝖒𝖘–1𝖎𝖓 4𝖘.𝕾𝖔𝖑𝖚𝖙𝖎𝖔𝖓.𝕲𝖎𝖛𝖊𝖓,𝕽𝖆𝖉𝖎𝖚𝖘 = 0.5 𝖒𝕱𝖎𝖓𝖆𝖑 𝖘𝖕𝖊𝖊𝖉 = 4 𝖒𝖘–1𝕴𝖓𝖎𝖙𝖎𝖆𝖑 𝖘𝖕𝖊𝖊𝖉 = 2𝖒𝖘–1𝕿𝖎𝖒𝖊 𝖙𝖆𝖐𝖊𝖓 = 4𝖘𝖂𝖊 𝖐𝖓𝖔𝖜 𝖙𝖍𝖆𝖙,𝖛 = 𝖚 + 𝖆𝕿𝖙 ; 𝖜𝖍𝖊𝖗𝖊, 𝖆𝕿 = 𝖙𝖆𝖓𝖌𝖊𝖓𝖙𝖎𝖆𝖑 𝖆𝖈𝖈𝖊𝖑𝖊𝖗𝖆𝖙𝖎𝖔𝖓 4 = 2 + 𝖆𝕿 × 4 𝖆𝕿 =𝕬𝖑𝖘𝖔, 𝖆𝕿 = 𝖗; 𝖜𝖍𝖊𝖗𝖊  = 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖆𝖈𝖈𝖊𝖑𝖊𝖗𝖆𝖙𝖎𝖔𝖓  = 1 𝖗𝖆𝖉 𝖘–2""",

    """𝕬𝕷𝕷𝕰𝕹 𝕺𝕴𝕲𝕴𝕿𝕬𝕷 

𝕴𝖓𝖙𝖗𝖔𝖉𝖚𝖈𝖙𝖎𝖔𝖓 𝖔𝖋 𝖈𝖎𝖗𝖈𝖚𝖑𝖆𝖗 𝖒𝖔𝖙𝖎𝖔𝖓

𝕬𝖓𝖌𝖚𝖑𝖆𝖗 𝕻𝖔𝖘𝖎𝖙𝖎𝖔𝖓, 𝕺𝖎𝖘𝖕𝖑𝖆𝖈𝖊𝖒𝖊𝖓𝖙, 𝖁𝖊𝖑𝖔𝖈𝖎𝖙𝖞, 𝕱𝖗𝖊𝖖𝖚𝖊𝖓𝖈𝖞, 𝕿𝖎𝖒𝖊 𝕻𝖊𝖗𝖎𝖔𝖉𝕬𝖓𝖌𝖚𝖑𝖆𝖗 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓 :𝕿𝖔 𝖉𝖊𝖈𝖎𝖉𝖊 𝖙𝖍𝖊 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓 𝖔𝖋 𝖆 𝖕𝖔𝖎𝖓𝖙 𝖎𝖓 𝖘𝖕𝖆𝖈𝖊 𝖜𝖊 𝖓𝖊𝖊𝖉 𝖙𝖔 𝖘𝖕𝖊𝖈𝖎𝖋𝖞 (𝖎) 𝖔𝖗𝖎𝖌𝖎𝖓 𝖆𝖓𝖉 (𝖎𝖎) 𝖗𝖊𝖋𝖊𝖗𝖊𝖓𝖈𝖊 𝖑𝖎𝖓𝖊.𝕿𝖍𝖊 𝖆𝖓𝖌𝖑𝖊 𝖒𝖆𝖉𝖊 𝖇𝖞 𝖙𝖍𝖊 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓 𝖛𝖊𝖈𝖙𝖔𝖗 𝖜.𝖗.𝖙. 𝖔𝖗𝖎𝖌𝖎𝖓, 𝖜𝖎𝖙𝖍 𝖙𝖍𝖊 𝖗𝖊𝖋𝖊𝖗𝖊𝖓𝖈𝖊 𝖑𝖎𝖓𝖊 𝖎𝖘 𝖈𝖆𝖑𝖑𝖊𝖉 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓. 𝕮𝖑𝖊𝖆𝖗𝖑𝖞 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓 𝖉𝖊𝖕𝖊𝖓𝖉𝖘 𝖔𝖓 𝖙𝖍𝖊 𝖈𝖍𝖔𝖎𝖈𝖊 𝖔𝖋 𝖙𝖍𝖊 𝖔𝖗𝖎𝖌𝖎𝖓 𝖆𝖘 𝖜𝖊𝖑𝖑 𝖆𝖘 𝖙𝖍𝖊 𝖗𝖊𝖋𝖊𝖗𝖊𝖓𝖈𝖊 𝖑𝖎𝖓𝖊.𝕮𝖎𝖗𝖈𝖚𝖑𝖆𝖗 𝖒𝖔𝖙𝖎𝖔𝖓 𝖎𝖘 𝖆 𝖙𝖜𝖔 𝖉𝖎𝖒𝖊𝖓𝖘𝖎𝖔𝖓𝖆𝖑 𝖒𝖔𝖙𝖎𝖔𝖓 𝖔𝖗 𝖒𝖔𝖙𝖎𝖔𝖓 𝖎𝖓 𝖆 𝖕𝖑𝖆𝖓𝖊. 𝕾𝖚𝖕𝖕𝖔𝖘𝖊 𝖆 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊 𝕻 𝖎𝖘 𝖒𝖔𝖛𝖎𝖓𝖌 𝖎𝖓 𝖆 𝖈𝖎𝖗𝖈𝖑𝖊 𝖔𝖋 𝖗𝖆𝖉𝖎𝖚𝖘 𝖗 𝖆𝖓𝖉 𝖈𝖊𝖓𝖙𝖗𝖊 𝕺.𝕿𝖍𝖊 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓 𝖔𝖋 𝖙𝖍𝖊 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊 𝕻 𝖆𝖙 𝖆 𝖌𝖎𝖛𝖊𝖓 𝖎𝖓𝖘𝖙𝖆𝖓𝖙 𝖒𝖆𝖞 𝖇𝖊 𝖉𝖊𝖘𝖈𝖗𝖎𝖇𝖊𝖉 𝖇𝖞 𝖙𝖍𝖊 𝖆𝖓𝖌𝖑𝖊  𝖇𝖊𝖙𝖜𝖊𝖊𝖓 𝕺𝕻 𝖆𝖓𝖉 𝕺𝖃. 𝕿𝖍𝖎𝖘 𝖆𝖓𝖌𝖑𝖊  𝖎𝖘 𝖈𝖆𝖑𝖑𝖊𝖉 𝖙𝖍𝖊 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓 𝖔𝖋 𝖙𝖍𝖊 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊.""",

    """𝕬𝕷𝕷𝕰𝕹 𝕺𝕴𝕲𝕴𝕿𝕬𝕷 

𝕴𝖓𝖙𝖗𝖔𝖉𝖚𝖈𝖙𝖎𝖔𝖓 𝖔𝖋 𝖈𝖎𝖗𝖈𝖚𝖑𝖆𝖗 𝖒𝖔𝖙𝖎𝖔𝖓

𝕴𝖑𝖑𝖚𝖘𝖙𝖗𝖆𝖙𝖎𝖔𝖓 2.𝕬 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊 𝖒𝖔𝖛𝖊𝖘 𝖎𝖓 𝖆 𝖈𝖎𝖗𝖈𝖑𝖊 𝖔𝖋 𝖗𝖆𝖉𝖎𝖚𝖘 𝖔𝖋 0.5 𝖒 𝖆𝖙 𝖆 𝖘𝖕𝖊𝖊𝖉 𝖙𝖍𝖆𝖙 𝖎𝖓𝖈𝖗𝖊𝖆𝖘𝖊𝖘 𝖚𝖓𝖎𝖋𝖔𝖗𝖒𝖑𝖞. 𝕱𝖎𝖓𝖉 𝖙𝖍𝖊 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖆𝖈𝖈𝖊𝖑𝖊𝖗𝖆𝖙𝖎𝖔𝖓 𝖔𝖋 𝖙𝖍𝖊 𝖕𝖆𝖗𝖙𝖎𝖈𝖑𝖊, 𝖎𝖋 𝖎𝖙𝖘 𝖘𝖕𝖊𝖊𝖉 𝖈𝖍𝖆𝖓𝖌𝖊𝖘 𝖋𝖗𝖔𝖒 2 𝖒𝖘–1𝖙𝖔 4 𝖒𝖘–1𝖎𝖓 4𝖘.𝕾𝖔𝖑𝖚𝖙𝖎𝖔𝖓.𝕲𝖎𝖛𝖊𝖓,𝕽𝖆𝖉𝖎𝖚𝖘 = 0.5 𝖒𝕱𝖎𝖓𝖆𝖑 𝖘𝖕𝖊𝖊𝖉 = 4 𝖒𝖘–1𝕴𝖓𝖎𝖙𝖎𝖆𝖑 𝖘𝖕𝖊𝖊𝖉 = 2𝖒𝖘–1𝕿𝖎𝖒𝖊 𝖙𝖆𝖐𝖊𝖓 = 4𝖘𝖂𝖊 𝖐𝖓𝖔𝖜 𝖙𝖍𝖆𝖙,𝖛 = 𝖚 + 𝖆𝕿𝖙 ; 𝖜𝖍𝖊𝖗𝖊, 𝖆𝕿 = 𝖙𝖆𝖓𝖌𝖊𝖓𝖙𝖎𝖆𝖑 𝖆𝖈𝖈𝖊𝖑𝖊𝖗𝖆𝖙𝖎𝖔𝖓 4 = 2 + 𝖆𝕿 × 4 𝖆𝕿 =𝕬𝖑𝖘𝖔, 𝖆𝕿 = 𝖗; 𝖜𝖍𝖊𝖗𝖊  = 𝖆𝖓𝖌𝖚𝖑𝖆𝖗 𝖆𝖈𝖈𝖊𝖑𝖊𝖗𝖆𝖙𝖎𝖔𝖓  = 1 𝖗𝖆𝖉 𝖘–2"""
]


user_ids = {}

@Client.on_message(filters.command(["copyright"], prefixes=["."]) & (filters.group | filters.channel) & filters.me)
async def edit_last_messages(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    user_ids[chat_id] = user_id

    await message.delete()

    me = await client.get_me()
    my_id = me.id

    messages_to_edit = []
    async for msg in client.get_chat_history(chat_id, limit=60):
        if msg.text and msg.from_user and msg.from_user.id == my_id:
            messages_to_edit.append(msg)

    messages_to_edit.sort(key=lambda msg: msg.date, reverse=True)

    num_messages = len(messages_to_edit)
    exclude_count = min(5, num_messages)
    edit_count = min(55, num_messages - exclude_count)

    messages_to_edit = messages_to_edit[exclude_count:]

    if len(messages_to_edit) < 1:
        await client.send_message("me", "Not enough messages to edit.")
        return

    messages_to_edit = messages_to_edit[:edit_count]

    owner_user_id = user_ids.get(chat_id)

    if not owner_user_id:
        await client.send_message("me", "User ID not found.")
        return

    num_texts_to_use = min(len(messages_to_edit), len(fixed_texts))

    links = []
    for i in range(num_texts_to_use):
        message_to_edit = messages_to_edit[i]
        if message_to_edit.from_user.id == owner_user_id:
            try:
                await client.edit_message_text(chat_id, message_to_edit.id, fixed_texts[i])
                links.append(f"https://t.me/c/{str(chat_id)[4:]}/{message_to_edit.id}")
            except Exception as e:
                print(f"Failed to edit message {message_to_edit.id}: {e}")
        else:
            print(f"Skipping message {message_to_edit.id} as it does not belong to the user.")

    try:
        chat_info = await client.get_chat(chat_id)
        group_link = chat_info.invite_link if chat_info.invite_link else "No invite link available."
    except Exception as e:
        group_link = "No invite link available."
        print(f"Failed to get group link: {e}")

    saved_message_text = f"Group ID: {chat_id}\nGroup Link: {group_link}\n"
    saved_message_text += "\n".join(links)

    await client.send_message("me", saved_message_text)
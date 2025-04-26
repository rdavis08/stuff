'''
Version 2.3.2

Please run with Python 3
This includes all 171 vocab words from Units 6-9

Steps to run:
Step 1: Copy this code
Step 2: Go to https://www.programiz.com/python-programming/online-compiler/
Step 3: Paste this code in
Step 4: Click "Run"
'''


import random
import time

nolist = ["no", "n"]
yeslist = ["yes", "y"]

def wait(x):
    time.sleep(x)

def answer_correct():
    global points
    global picked_number
    global unit6_points
    global unit7_points
    global unit8_points
    global unit9_points
    global unit6_total
    global unit7_total
    global unit8_total
    global unit9_total

    print("That's right!")
    points += 1
    if picked_number >= 1 and picked_number <= 30:
        unit6_points += 1
        unit6_total += 1
    elif picked_number >= 31 and picked_number <= 105:
        unit7_points += 1
        unit7_total += 1
    elif picked_number >= 106 and picked_number <= 140:
        unit8_points += 1
        unit8_total += 1
    elif picked_number >= 141 and picked_number <= 171:
        unit9_points += 1
        unit9_total += 1

def answer_incorrect():
    global correct_word_print
    global unit6_total
    global unit7_total
    global unit8_total
    global unit9_total
    global picked_number

    print("That's not it!")
    print("The correct term was: " + correct_word_print)
    if picked_number >= 1 and picked_number <= 30:
        unit6_total += 1
    elif picked_number >= 31 and picked_number <= 105:
        unit7_total += 1
    elif picked_number >= 106 and picked_number <= 140:
        unit8_total += 1
    elif picked_number >= 141 and picked_number <= 171:
        unit9_total += 1

running = True

definitions = [
    " ", "The act of becoming part of another culture",
    "Small Central American countries that fell under the economic power of foreign corporations",
    "A meeting of several European powers to discuss the orderly colonization of Africa in which colonial boundaries and trade movements were established",
    "Also known as the Anglo-Boer Wars, were two wars fought in 1880-1881 and 1899-1902 between the British Empire and two independent Boer states: the South African Republic and the Orange Free State. The conflicts arose over the unwanted presence of the British Empire",
    "A violent, armed uprising in China that sought to drive all foreigners from China from 1899 to 1901",
    "Corporate combinations that control entire industries",
    "An 1855 response to the large influx of Chinese miners in Australia that limited the number of Chinese immigrants that came ashore from each ship",
    "Privately owned colony by King Leopold II of Belgium from 1885-1908 in which he kept all profits and exploited workers. As many as 8 million died under Leopold's reign",
    "When foreign business interests have great economic power and influence which takes advantage of natural resources outside their borders",
    "Groups or neighborhoods of people from the same foreign country",
    "Around 1869, the Northern Paiute Indians thought the dead would return to drive out the white invaders and return lands to Native Americans. The Ghost Dance rituals performed were supposed to help this process",
    "From 1845 to 1849, the potato crop was destroyed in Ireland causing about 3 million people to emigrate to other nations",
    "People who work to improve the conditions of others",
    "A policy of extending a country's power and influence through diplomacy or military force",
    "An economic and social system in which trade, industry and capital are privately controlled and operated for a profit",
    "A system in Ceylon, Burma, and Malaya in which entire families were recruited to work on plantations",
    "A lack of agricultural diversity especially in developing nations",
    "A US policy drafted in 1823 which opposed European colonialism in the Americas",
    "From 1839 to 1842 war waged between the Chinese and British over the Chinese government's objection to the importation of opium",
    "A colony established for the purpose of relocating convicts. In 1788, Britain began sending its convicts to Australia",
    "The working class that Marx thought would be driven into poverty by the capitalists and revolt",
    "A medication used to prevent and treat malaria, enabling European colonization in tropical regions",
    "The rapid invasion, colonization, and division of African territories by European powers during the late 19th century",
    "The belief that only the fittest survive in human political and economic struggle. Used to justify racist beliefs",
    "The US victory in 1898 brought Guam, Cuba, Puerto Rico, and the Philippines under the control of the US",
    "A region in which one country has significant cultural, economic, or political influence over others",
    "Taxes on imported goods",
    "After the Opium War, this treaty required China to open ports to foreigners, give Hong Kong to Britain, allow the trade of opium, and pay damages",
    "Early socialists who believed that people could live together in small cooperative settlements where everyone could work together for the common good and they would collectively own all means of production and share in the production. They worked out plans for towns modeled after Thomas Moore's Utopia",
    "White Europeans claimed responsibility for caring for and civilizing natives of their respective colonies",
    "The idea that Britain could pacify Germany and make sure there was no war at any cost",
    "Heir apparent to the Austro-Hungarian throne whose assassination in Sarajevo set in motion the events that started World War I",
    "Policy statement forged in 1941 by Britain and the US which set down goals for the post-war world",
    "Alliances between Germany, Italy, and Japan",
    "An aerial battle fought in World War II in 1940 between the German Luftwaffe (air force), which carried out extensive bombing in Britain, and the British Royal Air Force, which offered successful resistance",
    "U.S. naval victory over the Japanese fleet in June 1942, in which the Japanese lost four of their best aircraft carriers; marked a turning point in World War II",
    "Unsuccessful German attack on the city of Stalingrad during World War II from 1942 to 1943, that was the furthest extent of German advance into the Soviet Union",
    "Fascist dictator of Italy (1922-1943). He led Italy to conquer Ethiopia (1935), joined Germany in the Axis pact (1936), and allied Italy with Germany in World War II. He was overthrown in 1943 when the Allies invaded Italy",
    "Serbian nationalist/terrorist group responsible for the assassination of Austrian Archduke Franz Ferdinand which resulted in the start of World War I",
    "Members of Italian fascists before WWII led by Mussolini which solidify Mussolini's control",
    "\"Lightning war\", type of fast-moving warfare used by German forces against Poland in 1939",
    "The overthrow of Russia's Provisional Government in the fall of 1917 by Lenin and his Bolshevik forces, made possible by the government's continuing defeat in the war, its failure to bring political reform, and a further decline in the conditions of everyday life",
    "Germany, Austria-Hungary, Bulgaria, and Ottoman Empire",
    "A compulsory military enlistment",
    "June 6, 1944 - Eisenhower led over a million troops and stormed the beaches at Normandy and began the process of re-taking France; this was a turning point of World War II",
    "An agreement in which the US promised to deliver 50 destroyers in exchange for eight British air and naval bases in the Western hemisphere",
    "Mexican revolutionary, champion of agrarianism, who fought in guerrilla actions during and after the Mexican Revolution",
    "A system of government characterized by strict social and economic control and a strong, centralized government usually headed by a dictator; first found in Italy by Mussolini",
    "The Nazi program of exterminating Jews under Hitler that was decided at the Berlin conference",
    "Woodrow Wilson's plan to establish lasting peace after World War I",
    "Mexican revolutionary and military commander in Northern Mexico during the Mexican Revolution; succeeded along with Emiliano Zapata in removing Diaz from power in 1911",
    "The assassin of Archduke Francis Ferdinand of Austria, a member of the Black Hand",
    "Another name for World War I because of the immense, unprecedented scale of fighting",
    "Labor camps under Stalin where many people died; political opponents of Stalin were often sent to these labor camps",
    "Leader of the Nazi special police (SS) who oversaw the forced removal of Gypsies from their homes",
    "The Nazi program of exterminating Jews under Hitler",
    "A belief in the superiority of one's nation over all others and the single-minded promotion of national interests",
    "(Night of the Broken Glass) November 9, 1938, when mobs throughout Germany destroyed Jewish property and terrorized Jews",
    "International organization founded in 1919 to promote world peace and cooperation but greatly weakened by the refusal of the United States to join; proved ineffectual in stopping aggression by Italy, Japan, and Germany in the 1930s",
    "Hitler's expansionist theory based on a drive to acquire \"living space\" for the German people",
    "The year-long, 6,000-mile retreat of Mao's forces into northern China after being attacked by Chiang Kai-shek's forces in 1934",
    "Germany's air force",
    "With a base in Korea, the Japanese moved into Manchuria and pushed out the Russians, Manchuria proved to be an invaluable foothold in China",
    "A system established through the League of Nations that allowed for the Allies to rule the colonies and territories of the Central Powers",
    "Leader of the Chinese Communist party and founder of the People's Republic of China in 1949",
    "A series of protests for Korean national independence from Japan that began on March 1, 1919",
    "Anti-Japanese demonstrations held by Chinese intellectuals and workers beginning on May 4, 1919",
    "A war from 1911 to 1920 in which Mexican reformers from the middle class joined with workers and peasants to overthrow the dictator, Porfirio Diaz",
    "Aggressive military preparedness that celebrates war and the armed forces",
    "Leader of the Indian independence movement and advocate of nonviolent resistance",
    "German political party joined by Adolf Hitler, emphasizing nationalism, racism, and war. When Hitler became chancellor of Germany in 1933, the Nazi Party became the only legal party and an instrument of Hitler's absolute rule",
    "Prime Minister of Great Britain from 1940 who was famous for appeasing Hitler at the Munich Conference",
    "The name of President Roosevelt's program for bringing the United States out of the depression",
    "A strip of land between the trenches of opposing armies along the Western Front during World War I",
    "Placed severe restrictions of Jews, prohibited from marrying non- Jews, attending schools or universities, holding government jobs, practicing law or medicine or publishing books",
    "An ideology that called for the unification of all lands in North Africa and the Middle East",
    "Organized by the victors of WWI to negotiate the peace treaties between the Allied and Central Powers",
    "The surprise air attack by the Japanese on the US naval base in Hawaii on December 7, 1941",
    "Ideas spread to influence public opinion for or against a cause",
    "A six-week period following the Japanese capture of the Chinese city of Nanjing. During this period, hundreds of thousands of civilians were murdered and 20,000-80,000 women were raped by soldiers of the Imperial Japanese Army",
    "As part of the Treaty of Versailles, Germany was ordered to pay fines to the Allies to repay the costs of the war. Opposed by the U.S., it quickly led to a severe depression in Germany",
    "1918-1921 Russians, Ukrainians, and others revolted against the Russian government because of widespread starvation after World War I",
    "Site of one of the worst genocides in modern history; caused by racial divisions under Belgian control of Rwanda",
    "Organized by Mohandas Gandhi where many Indians protested the British tax on salt by marching to the sea to make their own salt",
    "Plan by Germany to take France quickly before Russia could mobilize by violating Belgian neutrality; made Britain enter the war",
    "The idea that peoples of the same ethnicity, language, culture, and political ideals should be united and should have the right to form an independent nation-state",
    "A three-year siege by the Germans in which the Soviet Union defended the city of Leningrad and the Germans were unsuccessful",
    "The area near Czechoslovakia that was mainly German ethnicity that Germany took",
    "Hitler's name for the new order he established in 1933",
    "Committing all resources to the war effort",
    "A state in which the government controls every aspect of society",
    "The treaty imposed on Germany by the Allied powers in 1920 after the end of World War I which demanded exorbitant reparations from the Germans",
    "Long ditches dug in the ground with the excavated earth banked in front in order to defend against enemy fire",
    "Signed between the Axis powers in 1940 (Italy, Germany and Japan) where they pledged to help the others in the event of an attack by the US",
    "Germany, Austria-Hungary, and Italy in alliance before the start of World War I",
    "The alliance between Britain, France, and Russia in which all three viewed Germany as a rival; later became known as the Allies",
    "International organization founded in 1945 to promote world peace and cooperation. It replaced the League of Nations",
    "Founder of the Russian (Bolshevik) Communist Party, this man led the November Revolution in 1917 which established a revolutionary soviet government based on a union of workers, peasants, and soldiers",
    "1942 conference in Germany concerning the plan to murder European Jews",
    "A war based on wearing the other side down by constant attacks and heavy losses",
    "Democratic government founded in 1919 in Germany following Kaiser Wilhelm II's abdication near the end of War World I",
    "He was the British prime minister during World War II and resisted German attacks",
    "After World War I, this United States president sought to reduce the risk of war by writing the Fourteen Points that influenced the creation of the League of Nations",
    "Group of reformers that advocated for a constitution like the European states and for Turkification, an effort to all citizens of the multiethnic empire identify with Turkish culture",
    "Written by Arthur Zimmerman, a German foreign secretary; the German government offered to help Mexico reclaim territory lost to the US in 1848 if Mexico allied with Germany in World War I",
    "The line that separated Soviet occupied North Korea and US occupied South Korea",
    "The Republic of South Africa's governing social democratic party",
    "Originally founded to fight off the Soviet Union, which supported the communist Afghan government",
    "The effort by the United States and Britain to ship by air 2.3 million tons of supplies to the residents of the Western-controlled sectors of Berlin as a response to a Soviet blockade",
    "Wall built in 1961 to keep people in East Germany from fleeing to West Germany",
    "Great Britain, United States, and the Soviet Union",
    "A conflict that does not involve any direct military confrontation between two or more rival states",
    "A policy of not allowing communism to spread",
    "The Soviet plan to rebuild Eastern Europe; developed because the Soviets did not want to participate in the Marshall Plan",
    "A 13-day confrontation between the Soviet Union and the United States that occurred after Soviet missiles were discovered in Cuba",
    "Mao's attempt to reinvigorate China's commitment to communism in 1966",
    "A relaxation of strained relations by verbal communication",
    "The notion that one nation falling to communist rule will result in neighboring nations falling to communist rule",
    "US commander of UN military forces that supported South Korea during the Korean War",
    "The economic policy of Mao Zedong introduced in 1958 which proposed small-scale industrialization projects integrated into peasant communities and resulted in economic disaster; ended in 1960",
    "Communist leader of North Vietnam who opposed the French occupation of South Vietnam after World War II",
    "A political barrier that isolated the peoples of Eastern Europe after World War II, restricting their ability to travel outside the region",
    "1950-1953; Began when North Korea invaded South Korea in an attempt to reunite the country under its leadership",
    "Declared the founding of the People's Republic of China in 1949 and supported the Chinese peasantry throughout his life",
    "Offered $12 billion in aid to European countries to modernize industry, reduce trade barriers, and rebuild infrastructure",
    "Socialist lawyer who led the black resistance to apartheid in South Africa",
    "An alliance between the US, England, France, Canada, and Western European countries made to defend one another if they were attacked by any other country",
    "A type of sovereign state in which only one political party has the right to form the government",
    "A war in which a major power helps bring about conflict between other nations but does not always fight directly",
    "Small states that are economically or politically dependent on a larger more powerful state",
    "The idea that every country should choose its own form of government and leaders",
    "A competition of space exploration between the United States and Soviet Union",
    "Negotiations between the United States and the Soviet Union that were aimed at curtailing the manufacture of strategic missiles capable of carrying nuclear weapons",
    "Dubbed \"Star Wars,\" this was a missile defense system that was supposed to be able to destroy any Soviet nuclear missiles that targeted the US or its allies",
    "Military attack on Egypt by Britain, France, and Israel in 1956 after Egypt seized the Suez Canal from British administration",
    "1947 speech by US president Harry Truman that outlined what the US needed to do to stop the spread of communism, specifically in Turkey and Greece",
    "Established in 1945 to promote world peace and cooperation; replaced the League of Nations",
    "The name given to the communist guerrilla movement in southern Vietnam",
    "The belief that organized workers would overthrow capitalism in every country",
    "Meeting in 1945 between the Big Three to make final war plans, arrange the post-war fate of Germany, and discuss the proposal for creation of the United Nations as a successor to the League of Nations",
    "An avian flu that affected 500 million people worldwide and resulted in 50 million deaths",
    "A phenomenon in which people all over the world learned more about the U.S. than Americans learned about the rest of the world",
    "A South African system instituted in 1948 that enforced the segregation of people based on race",
    "A group of ten nations in Southeast Asia established in 1967 to promote trade",
    "A group of countries which included Hong Kong, Singapore, South Korea, and Taiwan that had economic models which closely followed Japan's and lifted people from poverty",
    "The nickname for the exit of Britain from the European Union in 2016",
    "The Indian government guaranteed that a certain percentage of government and public sector jobs and enrollment in higher education would be set aside for people whose caste has resulted in an underprivileged life",
    "A bacterial disease that spreads through contaminated water affecting poverty-stricken areas that lack clean water supplies",
    "An American act in 1965 that prohibited discrimination based on race, color, religion, sex, or national origin",
    "A culture in which people focus more on what they buy and own rather than where they live or what they believe",
    "He became the leader of China in 1981, and under his leadership, the Communist Party more actively promoted economic growth as opposed to economic equality",
    "The removal of natural vegetation cover through expansion and the use of agricultural lands in arid and semi-arid climates",
    "A deadly viral disease discovered in the Congo in 1976 that infects the African fruit bat, humans, and other primates; the disease is transmitted by exposure to the fluids of infected people or animals and results in death for the majority of people infected with it",
    "The opening up of a country's economy",
    "A non-renewable energy source such as coal, oil, and natural gas",
    "Economics systems based on supply and demand, with as little government control as possible; Ronald Reagan and Margaret Thatcher supported this idea",
    "An international accord developed in 1947 which lifted restrive barriers to trade and lowered tariffs; was replaced by the WTO (World Trade Organization) in 1995",
    "Manipulating cells or organisms to change their basic characteristics",
    "An increase in the average temperature of the world",
    "A political party that focuses on environmental issues",
    "Multinational agency founded in 1971 that combats deforestation, desertification, global warming, whaling, and overfishing",
    "The first major international agreement to reduce carbon emissions which was signed in 1997",
    "A 1994 agreement between the U.S., Canada, and Mexico in which the U.S. and Canada were encouraged to build factories in Mexico to produce tariff-free goods for export",
    "A movement primarily in French West Africa which emphasized \"blackness\" and the rejection of colonial French authority",
    "The 11th president of South Africa who was imprisoned for actively opposing apartheid",
    "A UN priority that advocates for prevention of conflict through diplomacy",
    "Taxes on foreign imports",
    "A peaceful protest in China in 1989 which was met with deadly force from the Chinese government",
    "A medical innovation that prevents serious diseases such as mumps, measles, tetanus, diphtheria, etc. which was brought into widespread use after 1900",
    "An American 1965 act which banned discrimination in voting",
    "Took over GATT's operations in 1995 and made rules that governed over 90 percent of all international trade"
]

terms = [
    " ", "assimilation",
    "banana republics",
    "berlin conference",
    "boer wars",
    "boxer rebellion",
    "cartels",
    "chinese immigration act",
    "congo free state",
    "economic imperialism",
    "ethnic enclaves",
    "ghost dance",
    "great famine",
    "humanitarians",
    "imperialism",
    "industrial capitalism",
    "kangani system",
    "monocultures",
    "monroe doctrine",
    "opium war",
    "penal colony",
    "proletariat",
    "quinine",
    "scramble for africa",
    "social darwinism",
    "spanish-american war",
    "sphere of influence",
    "tariffs",
    "treaty of nanking",
    "utopian socialist",
    "white man's burden",
    "appeasement",
    "archduke franz ferdinand",
    "atlantic charter",
    "axis powers",
    "battle of britain",
    "battle of midway",
    "battle of stalingrad",
    "benito mussolini",
    "black hand",
    "blackshirts",
    "blitzkrieg",
    "bolshevik revolution",
    "central powers",
    "conscription",
    "d-day",
    "destroyers-for-bases agreement",
    "emiliano zapata",
    "fascism",
    "final solution",
    "fourteen points",
    "francisco \"pancho\" villa",
    "gavrilo princip",
    "great war",
    "gulags",
    "heinrich himmler",
    "holocaust",
    "hypernationalism",
    "kristallnacht",
    "league of nations",
    "lebensraum",
    "long march",
    "luftwaffe",
    "manchuria",
    "mandate system",
    "mao zedong",
    "march first movement",
    "may fourth movement",
    "mexican revolution",
    "militarism",
    "mohandas gandhi",
    "nazis",
    "neville chamberlain",
    "new deal",
    "no man's land",
    "nuremberg laws",
    "pan-arabism",
    "paris peace conference",
    "pearl harbor",
    "propaganda",
    "rape of nanjing",
    "reparations",
    "russian civil war",
    "rwanda",
    "salt march",
    "schlieffen plan",
    "self-determination",
    "siege of leningrad",
    "sudetenland",
    "third reich",
    "total war",
    "totalitarian state",
    "treaty of versailles",
    "trench warfare",
    "tripartite pact",
    "triple alliance",
    "triple entente",
    "united nations",
    "vladimir lenin",
    "wannsee conference",
    "war of attrition",
    "weimar republic",
    "winston churchill",
    "woodrow wilson",
    "young turks",
    "zimmerman note",
    "38th parallel",
    "african national congress (anc)",
    "al-qaeda",
    "berlin airlift",
    "berlin wall",
    "big three",
    "cold war",
    "containment",
    "council for mutual economic assistance",
    "cuban missile crisis",
    "cultural revolution",
    "detente",
    "domino theory",
    "douglas macarthur",
    "great leap forward",
    "ho chi minh",
    "iron curtain",
    "korean war",
    "mao zedong",
    "marshall plan",
    "nelson mandela",
    "north atlantic treaty organization (nato)",
    "one-party state",
    "proxy war",
    "satellite countries",
    "self-determination",
    "space race",
    "strategic arms limitation treaty (salt)",
    "strategic defense initiative (sdi)",
    "suez crisis",
    "truman doctrine",
    "united nations",
    "viet cong",
    "world revolution",
    "yalta conference",
    "1918 influenza pandemic",
    "americanization",
    "apartheid",
    "association of southeast asian nations (asean)",
    "asian tigers",
    "brexit",
    "caste reservation system",
    "cholera",
    "civil rights act",
    "consumer culture",
    "deng xiaoping",
    "desertification",
    "ebola",
    "economic liberalization",
    "fossil fuels",
    "free markets",
    "general agreement on tariffs and trade (gatt)",
    "genetic engineering",
    "global warming",
    "green party",
    "greenpeace",
    "kyoto protocol",
    "nafta (north american free trade agreement)",
    "negritude movement",
    "nelson mandela",
    "peacekeeping",
    "protective tariffs",
    "tiananmen square",
    "vaccines",
    "voting rights act",
    "world trade organization (wto)"
]

limited_values = [106, 143, 31, 145, 1, 33, 2, 35, 38, 109, 3, 110, 39, 40, 42, 5, 146, 7, 149, 112, 8, 44, 113, 115, 45,
    152, 118, 119, 153, 47, 10, 48, 50, 51, 32, 402, 316, 298, 366, 299, 300, 301, 367, 260, 368, 262, 369, 304, 305, 307,
    310, 311, 371, 314, 315, 264, 409, 372, 411, 318, 320, 265, 323, 324, 266, 267, 325, 375, 328, 329, 330, 376, 269, 332,
    270, 272, 283, 379, 380, 381, 273, 414, 336, 274, 338, 382, 343, 384, 416, 346, 347, 276, 348, 417, 386, 350
]

anc_alts = ["anc", "african national congress"]
nato_alts = ["nato", "north atlantic treaty organization"]
salt_alts = ["salt", "strategic arms limitation treaty", "strategic arms limitation talks", "strategic arms limitation talks (salt)"]
sdi_alts = ["sdi", "strategic defense initiative"]
asean_alts = ["asean", "association of southeast asian nations"]
gatt_alts = ["gatt", "general agreement on tariffs and trade"]
nafta_alts = ["nafta", "north american free trade agreement", "north american free trade agreement (nafta)"]
wto_alts = ["wto", "world trade organization"]
un_alts = ["un", "united nations (un)"]

gandhi_alts = ["gandhi"]
dday_alts = ["d day"]
ops_alts = ["one party state"]
pv_alts = ["pancho villa", "francisco villa", "francisco pancho villa"]
m1_alts = ["march 1st movement", "march 1 movement"]
m4_alts = ["may 4th movement", "may 4 movement"]
dfb_alts = ["destroyers for bases agreement"]
zapata_alts = ["zapata"]
holocaust_alts = ["the holocaust"]
thirty_eighth_alts = ["thirty-eighth parallel", "thirty eighth parallel"]

detente_alts = ["détente"]
banana_alts = ["banana republic"]
blackshirts_alts = ["black shirts"]
archduke_alts = ["franz ferdinand", "archduke ferdinand"]
satellite_alts = ["satellite country", "satellite state", "satellite states"]
stalingrad_alts = ["stalingrad"]
mussolini_alts = ["mussolini"]

while running:
    unit6_points = 0
    unit7_points = 0
    unit8_points = 0
    unit9_points = 0
    points = 0
    
    unit6_total = 0
    unit7_total = 0
    unit8_total = 0
    unit9_total = 0
    total = 0

    study = str(input("Would you like to study? ")).strip()
    if study.lower() in yeslist:
        limited_list = str(input("Do you only want words from Mrs. Braun's shortened list of the 95 most important words? ")).strip()
        
        unit6 = str(input("Do you want words from Unit 6? ")).strip()
        unit7 = str(input("Do you want words from Unit 7? ")).strip()
        unit8 = str(input("Do you want words from Unit 8? ")).strip()
        unit9 = str(input("Do you want words from Unit 9? ")).strip()
        
        if limited_list.lower() in yeslist:
            limitation_count = 0
            generatable_numbers = []
            for value in limited_values:
                limitation_count += 1
                if limitation_count > 35:
                    applied_value = value - 246
                    generatable_numbers.append(applied_value)
                else:
                    generatable_numbers.append(value)
        else:
            generatable_numbers = []
            for number in range(172):
                generatable_numbers.append(number)
            generatable_numbers.remove(0)
        
        studying = True
        while studying:
            if unit6.lower() in nolist and unit7.lower() in nolist and unit8.lower() in nolist and unit9.lower() in nolist:
                print("Why did you say no for all of them?")
                wait(0.75)
                print("You can't study now.")
                wait(0.75)
                studying = False
                running = False
                maxtotal = 200
                generated_definition = 200
            
            elif unit6.lower() in nolist and unit7.lower() in nolist and unit8.lower() in nolist:
                generated_definition = random.randint(141, 171)
                if limited_list.lower() in yeslist:
                    maxtotal = 12
                else:
                    maxtotal = 31
            elif unit6.lower() in nolist and unit7.lower() in nolist and unit9.lower() in nolist:
                generated_definition = random.randint(106, 140)
                if limited_list.lower() in yeslist:
                    maxtotal = 22
                else:
                    maxtotal = 35
            elif unit6.lower() in nolist and unit8.lower() in nolist and unit9.lower() in nolist:
                generated_definition = random.randint(31, 105)
                if limited_list.lower() in yeslist:
                    maxtotal = 43
                else:
                    maxtotal = 75
            elif unit7.lower() in nolist and unit8.lower() in nolist and unit9.lower() in nolist:
                generated_definition = random.randint(1, 30)
                if limited_list.lower() in yeslist:
                    maxtotal = 19
                else:
                    maxtotal = 30
            
            elif unit6.lower() in nolist and unit7.lower() in nolist:
                generated_definition = random.randint(106, 171)
                if limited_list.lower() in yeslist:
                    maxtotal = 34
                else:
                    maxtotal = 66
            elif unit6.lower() in nolist and unit8.lower() in nolist:
                generated_definition = random.randint(*random.choice([(31, 105), (141, 171)]))
                if limited_list.lower() in yeslist:
                    maxtotal = 55
                else:
                    maxtotal = 106
            elif unit6.lower() in nolist and unit9.lower() in nolist:
                generated_definition = random.randint(31, 140)
                if limited_list.lower() in yeslist:
                    maxtotal = 65
                else:
                    maxtotal = 110
            elif unit7.lower() in nolist and unit8.lower() in nolist:
                generated_definition = random.randint(*random.choice([(1, 30), (141, 171)]))
                if limited_list.lower() in yeslist:
                    maxtotal = 31
                else:
                    maxtotal = 61
            elif unit7.lower() in nolist and unit9.lower() in nolist:
                generated_definition = random.randint(*random.choice([(1, 30), (106, 140)]))
                if limited_list.lower() in yeslist:
                    maxtotal = 41
                else:
                    maxtotal = 65
            elif unit8.lower() in nolist and unit9.lower() in nolist:
                generated_definition = random.randint(1, 105)
                if limited_list.lower() in yeslist:
                    maxtotal = 62
                else:
                    maxtotal = 105
            
            elif unit6.lower() in nolist:
                generated_definition = random.randint(31, 171)
                if limited_list.lower() in yeslist:
                    maxtotal = 77
                else:
                    maxtotal = 141
            elif unit7.lower() in nolist:
                generated_definition = random.randint(*random.choice([(1, 30), (106, 171)]))
                if limited_list.lower() in yeslist:
                    maxtotal = 53
                else:
                    maxtotal = 96
            elif unit8.lower() in nolist:
                generated_definition = random.randint(*random.choice([(1, 105), (141, 171)]))
                if limited_list.lower() in yeslist:
                    maxtotal = 74
                else:
                    maxtotal = 136
            elif unit9.lower() in nolist:
                generated_definition = random.randint(1, 140)
                if limited_list.lower() in yeslist:
                    maxtotal = 84
                else:
                    maxtotal = 140
            
            else:
                generated_definition = random.randint(1, 171)
                if limited_list.lower() in yeslist:
                    maxtotal = 96
                else:
                    maxtotal = 171

            for picked_number in range(172):
                if generated_definition == picked_number and picked_number in generatable_numbers:
                    print(definitions[picked_number])
                    correct_word = terms[picked_number]
                    correct_word_print = correct_word[:1].upper() + correct_word[1:]
                    answer = str(input("What is this term? ")).strip()
                    
                    if correct_word == "african national congress (anc)":
                        if answer.lower() == correct_word or answer.lower() in anc_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "north atlantic treaty organization (nato)":
                        if answer.lower() == correct_word or answer.lower() in nato_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "strategic arms limitation treaty (salt)":
                        if answer.lower() == correct_word or answer.lower() in salt_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "strategic defense initiative (sdi)":
                        if answer.lower() == correct_word or answer.lower() in sdi_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "association of southeast asian nations (asean)":
                        if answer.lower() == correct_word or answer.lower() in asean_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "general agreement on tariffs and trade (gatt)":
                        if answer.lower() == correct_word or answer.lower() in gatt_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "nafta (north american free trade agreement)":
                        if answer.lower() == correct_word or answer.lower() in nafta_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "world trade organization (wto)":
                        if answer.lower() == correct_word or answer.lower() in wto_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "united nations":
                        if answer.lower() == correct_word or answer.lower() in un_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "mohandas gandhi":
                        if answer.lower() == correct_word or answer.lower() in gandhi_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "francisco \"pancho\" villa":
                        if answer.lower() == correct_word or answer.lower() in pv_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "one-party state":
                        if answer.lower() == correct_word or answer.lower() in ops_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "march first movement":
                        if answer.lower() == correct_word or answer.lower() in m1_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "may fourth movement":
                        if answer.lower() == correct_word or answer.lower() in m4_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "destroyers-for-bases agreement":
                        if answer.lower() == correct_word or answer.lower() in dfb_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "emiliano zapata":
                        if answer.lower() == correct_word or answer.lower() in zapata_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "holocaust":
                        if answer.lower() == correct_word or answer.lower() in holocaust_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "38th parallel":
                        if answer.lower() == correct_word or answer.lower() in thirty_eighth_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "detente":
                        if answer.lower() == correct_word or answer.lower() in detente_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "d-day":
                        if answer.lower() == correct_word or answer.lower() in dday_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "banana republics":
                        if answer.lower() == correct_word or answer.lower() in banana_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "blackshirts":
                        if answer.lower() == correct_word or answer.lower() in blackshirts_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "archduke franz ferdinand":
                        if answer.lower() == correct_word or answer.lower() in archduke_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "satellite countries":
                        if answer.lower() == correct_word or answer.lower() in satellite_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "battle of stalingrad":
                        if answer.lower() == correct_word or answer.lower() in stalingrad_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    elif correct_word == "benito mussolini":
                        if answer.lower() == correct_word or answer.lower() in mussolini_alts:
                            answer_correct()
                        else:
                            answer_incorrect()
                    else:
                        if answer.lower() == correct_word:
                            answer_correct()
                        else:
                            answer_incorrect()
                    
                    total += 1
                    generatable_numbers.remove(picked_number)
                    wait(1)
            
            if total == maxtotal:
                print("You finished studying!")
                wait(0.75)
                points_percent = round((points/total)*100, 2)
                print("You got " + str(points) + " out of " + str(total) + " terms correct!")
                wait(0.75)
                print("That's " + str(points_percent) + "%!")
                studying = False
                wait(0.75)
                if unit6.lower() not in nolist:
                    unit6_percent = round((unit6_points/unit6_total)*100, 2)
                    print("Unit 6: " + str(unit6_points) + "/" + str(unit6_total) + ", " + str(unit6_percent) + "%")
                    wait(0.75)
                if unit7.lower() not in nolist:
                    unit7_percent = round((unit7_points/unit7_total)*100, 2)
                    print("Unit 7: " + str(unit7_points) + "/" + str(unit7_total) + ", " + str(unit7_percent) + "%")
                    wait(0.75)
                if unit8.lower() not in nolist:
                    unit8_percent = round((unit8_points/unit8_total)*100, 2)
                    print("Unit 8: " + str(unit8_points) + "/" + str(unit8_total) + ", " + str(unit8_percent) + "%")
                    wait(0.75)
                if unit9.lower() not in nolist:
                    unit9_percent = round((unit9_points/unit9_total)*100, 2)
                    print("Unit 9: " + str(unit9_points) + "/" + str(unit9_total) + ", " + str(unit9_percent) + "%")
                    wait(0.75)
                wait(1.25)
    elif study.lower() in nolist:
        print("I hope you already studied!")
        running = False
    else:
        wait(0)

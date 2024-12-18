# Please run with Python 3
# This includes all 176 vocab words from Units 1-5

# If you have a Windows computer, the best way to run it is through the command prompt
# Steps:
# Step 1: Download the file
# Step 2: Follow the steps for parts 1 and 2 at https://www.wikihow.com/Use-Windows-Command-Prompt-to-Run-a-Python-File#:~:text=To%20run%20a%20Python%20file%2C%20type%20%E2%80%9CPython%20File.py,Python%20script.py%E2%80%9D%20instead.

# Alternate steps to run:
# Step 1: Go to codehs.com and log in with your s-number email and password
# Step 2: Click on Sandbox
# Step 3: Click on name your program and then name it something, I don't care what you name it
# Step 4: Click on create program
# Step 5: Select Python 3, and click on create program
# Step 6: Delete the hello world print statement
# Step 7: Copy this code by clicking on the icon with the two squares above and to the right of the code area
# Step 8: Paste the code into codehs
# Step 9: Click run

# Notes:
# If you don't have Windows and codehs doesn't work then honestly it's not worth the effort to download something that can run python, you can go use Mrs. Braun's powerpoint study guide, that's cool too
# Be sure to save your sandbox program in codehs
# Codehs is a bit buggy, but it's the best option for this so
# Codehs does time out after a bit, so be sure to be actively studying


import random
import time

def wait(x):
    time.sleep(x)

def correct():
    global points
    print("That's right!")
    points += 1

def incorrect():
    global correct_word
    print("That's not it!")
    print("The correct term was " + correct_word + ".")

def result():
    global total
    global correct_word
    global answer
    answer = str(input("What is this term? "))
    if answer.lower() == correct_word:
        correct()
    else:
        incorrect()
    total += 1
    wait(1)
    
def unit1_track():
    global unit1_points
    global correct_word
    global answer
    if answer.lower() == correct_word:
        unit1_points += 1

def unit2_track():
    global unit2_points
    global correct_word
    global answer
    if answer.lower() == correct_word:
        unit2_points += 1

def unit3_track():
    global unit3_points
    global correct_word
    global answer
    if answer.lower() == correct_word:
        unit3_points += 1

def unit4_track():
    global unit4_points
    global correct_word
    global answer
    if answer.lower() == correct_word:
        unit4_points += 1

def unit5_track():
    global unit5_points
    global correct_word
    global answer
    if answer.lower() == correct_word:
        unit5_points += 1

run = True

definitions = [
    " ", "An Arab dynasty of caliphs (successors to the Prophet) who governed much of the Islamic world from its capital in Baghdad beginning in 750 CE. After 900 CE, that empire increasingly fragmented until its overthrow by the Mongols in 1258 CE",
    "Arabic name for Spain, most of which was conquered by Arab and Berber forces between 711 and 718 CE. Muslim Spain represented a point of encounter between the Islamic world and Christian Europe",
    "The largest religious structure in the premodern world, this temple was built by the powerful Angkor kingdom (located in modern Cambodia) in the 12th century CE to express a Hindu understanding of the cosmos centered on a mythical Mount Meru, the home of the gods in Hindu tradition. It was later used by Buddhists as well",
    "Major state that developed in what is now Mexico in the 14th and 15th centuries; dominated by the semi-nomadic Mexica, who had migrated into the region from northern Mexico",
    "Meaning worship, this Hindu movement began in south India and moved northward between 600 and 1000 CE; it involved the intense adoration of and identification with a particular deity through songs, prayer, and rituals",
    "The way of the warrior, referring to the martial values of the Japanese samurai, including bravery, loyalty, and an emphasis on death over surrender",
    "The surviving eastern Roman Empire and one the centers of Christendom during the medieval centuries. The Byzantine Empire was founded at the end of the 3rd century, when the Roman Empire was divided into eastern and western halves and survived until its conquest by Muslim forces in 1453 CE",
    "A political-religious system in which the secular ruler is also head of the religious establishment, as in the Byzantine Empire",
    "A major rise in prosperity that took place in China under the Song dynasty (960 - 1279 CE), which was marked by rapid population growth, urbanization, economic specialization, the development of an immense network of internal waterways, and a great increase in industrial production and technological innovation",
    "A variation of Chinese writing developed in Vietnam that became the basis for an independent national literature; southern script",
    "The Chinese philosophy first enunciated by Confucius, advocating the moral example of superiors as the key element of social order",
    "New capital for the eastern half of the Roman Empire; Constantinople's highly defensible and economically important site helped ensure the city's cultural and strategic importance for many centuries",
    "A term used to describe the holy wars waged by Western Christendom, especially against the forces of Islam in the eastern Mediterranean from 1095 to 1291 CE and on the Iberian Peninsula into the 15th century. Further Crusades were also conducted in non-Christian regions of Eastern Europe from about 1150 on. Crusades could be declared only by the pope; participants swore a vow and received in return an indulgence removing the penalty for confessed sins",
    "A Chinese philosophy/popular religion that advocates a simple and unpretentious way of living and alignment with the natural world, founded by the legendary figure Laozi",
    "Branch of Christianity that developed in the eastern part of the Roman Empire and gradually separated, mostly on matters of practice, from the branch of Christianity dominant in Western Europe; noted for the subordination of the Church to political authorities, a married clergy, the use of leavened bread in the Eucharist, and a sharp rejection of the authority of Roman popes",
    "A rebirth of classical learning that is most often associated with the cultural blossoming of Italy in the period 1350 - 1500 CE and that included not just a rediscovery of Greek and Roman learning but also major developments in art, as well as growing secularism in society. It spread to Northern Europe after 1400",
    "The Chinese practice of tightly wrapping girls' feet to keep them small, prevalent in the Song Dynasty and later; an emphasis on small size and delicacy was central to views of female beauty",
    "A powerful state in the southern African interior that apparently emerged from the growing trade in gold to the East African coast; flourished between 1250 and 1350 CE",
    "A phonetic alphabet developed in Korea in the 15th century in a move toward greater cultural independence from China",
    "China's capital during the Song dynasty, with a population at its height of more than a million people",
    "A religion based on the many beliefs, practices, sects, rituals, and philosophies in India; in the thinking of 19th century Indian reformers, it was expressed as a distinctive tradition, an Indian religion wholly equivalent to Christianity",
    "An academic center for research and translation of foreign texts that was established in Baghdad in 830 CE by the Abbasid caliph al-Mamun",
    "The Western Hemisphere's largest imperial state in the 15th and early 16th centuries, built by a relatively small community of Quechua-speaking people (the Incas), the empire stretched some 2,500 miles along the Andes Mountains, which run nearly the entire length of the west coast of South America, and contained perhaps 10 million subjects",
    "The monotheistic religion developed in the Middle East by the Hebrews, emphasizing a sole personal god (Yahweh) with concerns for social justice",
    "A culturally diverse civilization that emerged around the city of Kiev in the 9th century CE and adopted Christianity in the 10th, thus linking this emerging Russian state to the world of Eastern Orthodoxy",
    "Great vehicle, the popular development of Buddhism in the early centuries of the Common Era, which gave a much greater role to supernatural beings and to compassion and proved to be more popular than original (Theravada) Buddhism",
    "A major civilization of Mesoamerica known for the most elaborate writing system in the Americas and other intellectual and artistic achievements; flourished from 250 to 900 CE",
    "A person who earns a living by buying and selling goods",
    "A person who goes somewhere, often a foreign country, to share their religious beliefs with others",
    "Major Islamic state centered on Anatolia that came to include the Balkans, part of the Middle East, and much of North Africa; lasted in one form or another from the 14th to early 20th century",
    "Western European branch of Christianity that gradually defined itself as separate from Eastern Orthodoxy, with a major break occurring in 1054 CE that still has not been overcome. By the 11th century, Western Christendom was centered on the pope as the ultimate authority in matters of doctrine. The Church struggled to remain independent of established political authorities",
    "An empire of the 11th and 12th centuries, centered in Persia and present-day Iraq. Seljuk rulers adopted the Muslim title of sultan (ruler) as part of their conversion to Islam",
    "The Chinese dynasty (960 - 1279 CE) that rose to power after the Tang dynasty. During the Song dynasty, an explosion of scholarship gave rise to Neo-Confucianism, and a revolution in agricultural and industrial production made China the richest and most populated country on the planet",
    "A Muslim person dedicated to a life of prayer and meditation in order to unite with God",
    "Teaching of the Elders, the early form of Buddhism according to which the Buddha was a wise teacher but not divine; emphasizes practices rather than beliefs",
    "Western European branch of Christianity, also known as Roman Catholicism, that gradually defined itself as separate from Eastern Orthodoxy, with a major break occurring in 1054 CE, characterized by its relative independence from the state and its recognition of the authority of the pope",
    "A term used to describe the network of trade that linked parts of the pre-Columbian Americas; although less densely woven than the Afro-Eurasian trade networks, this web nonetheless provided a means of exchange for luxury goods and ideas over large areas",
    "Introduced to North Africa and the Sahara in the early centuries of the Common Era, this animal made trans-Saharan commerce possible by 300 to 400 CE",
    "Name given to a major process of settlement and societal organization that occurred in the period 860 - 1130 CE among the peoples of Chaco canyon, in what is now northwestern New Mexico; the society formed is notable for its settlements in large pueblos and for the building of hundreds of miles of roads, the purpose of which is not known",
    "An early and prominent state within West African civilization. With a reputation for great riches, Ghana flourished between 750 - 1076 CE and was later absorbed into the larger Kingdom of Mali",
    "A prominent state within West African civilization; it was established in 1235 CE and flourished for several centuries. Mali monopolized the import of horses and metals as part of the trans-Saharan trade; it was a large-scale producer of gold; and its most famous ruler, Mansa Musa, led a group of Muslims on the pilgrimage to Mecca in 1324 - 1325",
    "Professional merchants among the Aztecs who undertook large-scale trading expeditions in the 15th century CE",
    "A term used to describe the routes of the trans-Saharan trade, which linked interior West Africa to the Mediterranean and North African world",
    "The world's largest sea-based system of communication and exchange before 1500 CE. Centered in India, it stretched from southern China to eastern Africa",
    "Land-based trade routes that linked many regions in Eurasia. They were named after the most famous product traded along these routes",
    "A Malay kingdom that dominated the critical choke point in Indian Ocean trade at the Straits of Malacca between 670 and 1025 CE. Like other places in Southeast Asia, Srivijaya absorbed various cultural influences from India",
    "An east African civilization that emerged in the eighth century CE as a set of commercial city-states linked into the Indian Ocean trading network. Combining African Bantu and Islamic cultural patterns, these competing city-states accumulated goods from the interior and exchanged them for the products of distant civilizations",
    "A major commercial city of West African civilization and noted a center of Islamic scholarship and education by the 16th century",
    "A fairly small-scale commerce in enslaved people that flourished especially from 1100 to 1400, exporting West African slaves across the Sahara for sale in Islamic North Africa",
    "A series of important states that developed in the region stretching from the Atlantic coast to Lake Chad in the period 500 to 1600 CE. Developed in response to the economic opportunities of trans-Saharan trade (especially control of gold production), it included the states of Ghana, Mali, Songhai, and Kanem, as well as numerous towns and cities",
    "Great Chinese admiral who commanded a huge fleet of ships in a series of voyages in the Indian Ocean that began in 1405. Intended to enroll distant peoples and states in the Chinese tribute system, those voyages ended abruptly in 1433 and led to no lasting Chinese imperial presence in the region",
    "Type of government stressing Divine Right and total control by a King",
    "Also called jatis, strict social groupings designated at birth for Hindus",
    "A powerful noble in early modern Japan",
    "The idea pushing Absolutism which says that God chose a specific king to rule",
    "The Ottoman, Safavid and Mughal Empires which relied heavily on gunpowder and firearms",
    "Allowed books to be printed instead of hand-written and increased literacy",
    "King of England who created the Anglican Church so he could get a divorce from his wife and find another woman who could provide him with an heir",
    "Pieces of paper someone could buy to be forgiven of sins",
    "The new name given to Constantinople when the Ottoman Empire conquered it",
    "An elite core of eight thousand troops personally loyal to the sultan of the Ottoman Empire",
    "Tax levied by Islamic stats on certain non-Muslim subjects (dhimmis) who were permanently residing in Muslim lands under Islamic law",
    "Ethnic minority in China and the people from whom Manchuria derives its name",
    "German monk who began Protestant Reformation with his written work, 95 Theses",
    "Ruler of the Ottoman Empire from 1451 who wanted to capture Constantinople and topple the Byzantine Empire",
    "Muslim empire ruling India from the 16th to 18th centuries",
    "The list of grievances written by Martin Luther, which began the Reformation",
    "Turkish empire in the Middle East and North Africa from 1453-1918",
    "Religious movement when people broke away from the Catholic Church",
    "Chinese dynasty lasting from 1644-1911",
    "Muslim Empire in Persia from 1501-1722",
    "One of the two major Muslim sects; believe that the descendants of Muhammad's daughter and son-in-law, Ali, are the true Muslim leaders",
    "Developed from Hinduism and may have been influenced by the Islamic mysticism known as Sufism",
    "Tenth and longest-reigning sultan of the Ottoman Empire",
    "One of the two major branches of Islam, representing the majority of Muslims worldwide, and signifies followers who believe in the leadership succession following the Prophet Muhammad's death through Abu Bakr, upholding the Sunnah or traditional practices based on the Prophet's teachings and actions as the primary source of Islamic law",
    "Timur the Lame, a Mongol Turkic ruler who invaded Central Asia and the Middle East setting the stage for the rise of the Turkic Empires",
    "Africans living outside of Africa (usually as slaves) who retained some aspects of their cultures",
    "African kingdom on the Gold Coast that expanded rapidly after 1680",
    "The network of trade routes connecting Europe, Africa, and the Americas that underlay the Atlantic system",
    "An empire in Mexico that was overthrown by Cortes in 1521",
    "Those who plied the seas near North Africa along the Barbary Coast and captured other European slaves in the Mediterranean and then sold them to the sultan or other high-ranking officials",
    "(1474-1566) First bishop of Chiapas in southern Mexico who devoted most of his life to protecting Amerindian peoples from exploitation. His major achievement was the New Laws of 1542, which limited the ability of Spanish settlers to compel Amerindians to labor for them",
    "The economic system of large financial institutions —banks, stock exchanges, investment companies—that first developed in early modern Europe. Commercial capitalism, the trading system of the early modern economy, is often distinguished from industrial capitalism, the system based on machine production",
    "The practice of mapmaking",
    "Sellable crop that is grown and gathered for the market such as sugar and tobacco",
    "Groups of private investors who paid an annual fee to France and England in exchange for a monopoly over trade to the West Indies colonies",
    "A system where individuals were considered property to be bought and sold",
    "Navigator who explored the Americas under the flag of Spain",
    "Located in Bolivia it was one of the richest silver mining centers and most populous cities in colonial Spanish America",
    "The exchange of plants, animals, diseases, and technologies between the Americas and the rest of the world following Columbus's voyages",
    "Transformation to a trade-based economy using gold and silver",
    "Spanish soldiers who conquered parts of the Americas in the 16th century",
    "West African languages mixed with European languages",
    "(1602) A mercantile company chartered by the Dutch to conduct trade missions throughout the East Indies",
    "(1621-1794) Trading company chartered by the Dutch government to conduct its merchants' trade in the Americas and Africa",
    "Portuguese sugar plantations called engines because of the amount of sugar they processed. The working conditions were horrible, and the labor force suffered greatly",
    "A grant of authority over a population of Amerindians in the Spanish colonies that provided the grant holder with a supply of cheap labor and periodic payments of goods by the Amerindians. It obliged the grant holder to Christianize the Amerindians",
    "Portuguese navigator who led the Spanish expedition of 1519-1522 that was the first to sail around the world",
    "Spanish explorer who conquered the Incas in what is now Peru and founded the city of Lima",
    "Spanish trading ships that made round-trip sailing voyages once or twice per year across the Pacific Ocean",
    "Also called the Revolution of 1688, was the overthrow of King James II of England by a union of English Parliamentarians with the Dutch stadtholder William III of Orange-Nassau",
    "(1394-1460) Prince of Portugal who established an observatory and school of navigation at Sagres and directed voyages that spurred the growth of Portugal's colonial empire",
    "Name Columbus gave to the island that is now Haiti and the Dominican Republic",
    "A migrant to British colonies in the Americas who paid for passage by agreeing to work for a set term ranging from four to seven years",
    "An alliance of five northeastern Amerindian peoples that made decisions on military and diplomatic issues through a council of representatives. Allied first with the Dutch and later with the English, the Confederacy dominated the area from western New England to the Great Lakes",
    "English colony in Virginia that was England's first successful colony in the Americas",
    "Businesses that sold shares to individuals to raise money for its trading enterprises and to spread the risks and profits among many investors",
    "Indian power that existed from 1674 to 1818 and ruled over a large area of the Indian subcontinent; credited with ending Mughal rule in India",
    "Empires such as Spain, Portugal, Great Britain, France, and Holland that were based upon sea travel",
    "Slaves in the Caribbean and former Spanish territories in the Americas fought to gain freedom",
    "European government policies of the sixteenth, seventeenth, and eighteenth centuries designed to promote overseas trade between a country and its colonies and accumulate precious metals by requiring colonies to trade only with their motherland country",
    "The term used by Spanish authorities to describe someone of mixed Amerindian and European descent",
    "The part of the Atlantic Circuit involving the transportation of enslaved Africans across the Atlantic to the Americas",
    "(1368-1644) Empire based in China that Zhu Yuanzhang established after the overthrow of the Yuan Empire. The Ming emperor Yongle sponsored the building of the Forbidden City and the voyages of Zheng He. The later years of the Ming saw a slowdown in technological development and economic decline",
    "Labor obligation in Peru that required a percentage of the adult male Amerindians to work for two to four months each year in mines, farms, or textile factories",
    "Granted certain merchants or the government itself the exclusive right to trade",
    "Term used in Spanish and Portuguese colonies to describe someone of mixed African and European descent",
    "Dutch settlement in the Hudson River Valley that is present day New York City",
    "French colony in North America along the St. Lawrence River",
    "Colony established by Cortes after overthrowing the Aztecs in Mexico",
    "A route through or around North America that would lead to East Asia and the trade there",
    "A trade rivalry between traders from Oman and European traders over the Indian Ocean Trade Route that fueled Columbus's search for a new route to India",
    "Those who were born on the Iberian Peninsula and stood at the top of the social pyramid in Latin America",
    "The labor-intensive agricultural centers of the new world which were implemented by Spain, Britain, and Portugal",
    "English Protestant dissenters who believed that God predestined souls to heaven or hell before birth. They founded Massachusetts Bay Colony in 1629",
    "French trading post established in 1608",
    "A trading company chartered by the English government in 1672 to conduct its merchants' trade on the Atlantic coast of Africa",
    "Disease brought to the Americas by way of Europeans that was deadly to the native populations",
    "The combining of different religious practices and beliefs",
    "The time in the early 17th century when Swedish and Polish forces occupied Moscow; it marked the end of the Muscovite Rulers",
    "Empire based on small outposts rather than control of large territories",
    "Africans captured and sold in the Americas as slaves",
    "1494 treaty in which Spain and Portugal divided the Americas between them",
    "Atlantic trading system that had three segments which enslaved Africans were part of",
    "Landed in India in 1498 and claimed territory for Portugal's empire",
    "The highest-ranking Spanish officials in the colonies who enjoyed broad power, but also faced obstacles to their authority in the vast territories they sought to control",
    "The movement to end the Atlantic slave trade and free all enslaved people which gained followers in 18th century",
    "One of the most influential thinks of the Enlightenment; wrote Wealth of Nations which responded to mercantilism and called for freer trade",
    "The transformation of human existence caused by the deliberate cultivation of particular plants and the deliberate taming and breeding of particular animals",
    "A former prison in Paris that symbolized the abuses of the monarchy and the corrupt aristocracy; it was stormed by angry crowds on July 14, 1789",
    "The middle class and investors who owned machinery and factories where workers produced goods",
    "Money available to invest in business",
    "An economic system in which the means of production, such as factories and natural resources, are privately owned and are operated for profit",
    "A political system in which the government owns all property and dominates all aspects of life in a country; Marx believed socialism would replace capitalism and communism would replace socialism as the final stage of economic development",
    "One of the fundamental documents of the French Revolution, defining a set of individual rights and collective rights of all of the estates as one",
    "Production process in which a worker or group of workers is assigned a specialized task in order to increase efficiency",
    "Post-Renaissance period in European history devoted to the study and exploration of new ideas in science, politics, the arts, and philosophy",
    "A prominent bank established and based in Hong Kong since 1865 and focused on finance, corporate investments, and global banking when Hong Kong was a colony of the British Empire",
    "Sweeping reforms in the late 1800s in China that included the abolition of the civil service exam, elimination of corruption, and the establishment of Western-style industrial, commercial, and medical systems",
    "New technologies reshaped societies and led to dramatic changes",
    "Increased mechanization of production",
    "Genevan philosopher and writer whose political philosophy influenced the French Revolution as well as the overall development of modern political, sociological, and educational thought",
    "Philosopher who wrote two Treatises of Government and advocated the idea of the social contract",
    "German scholar and writer who argued for socialism; published the Communist Manifesto",
    "Organizations of workers that advocate for the right to bargain with employers and put resulting agreements in a contract",
    "French for leave alone, an economic environment in which transactions between private parties are free from tariffs, government subsidies, and enforced monopolies, with only enough government regulations sufficient to protect property rights against theft and aggression",
    "English writer who published A Vindication of the Rights of Women in 1792 that argues that women should receive the same education as men",
    "The dissolution of Japan's feudal system of government and the restoration of the imperial system that led to Japan modernizing and industrializing",
    "Control of a specific business and elimination of all competition",
    "Albanian Ottoman officer who was selected to be the new governor of Egypt; reformed Egypt and pushed it to industrialize",
    "A feeling of intense loyalty to others who share one's language and culture",
    "Military confrontations between the Maori and British over who had rights to the land which eventually ended in European colonization of New Zealand",
    "A German statesman who unified numerous German states into a powerful German Empire under Prussian leadership, then created a balance of power that preserved peace in Europe from 1871 until 1914",
    "A group of thinkers and writer in the 18th century that explored social, political, and economic theories in new ways",
    "The working class who often worked in factories and mines for little compensation",
    "1882 movement in the Philippines that involved magazines, pamphlets, and other publications that demanded social and political reforms",
    "System of politics or principles based on practical rather than moral or ideological considerations",
    "A period during the French Revolution in which the government executed thousands of opponents of the revolution",
    "Key players were the United States, Great Britain, and Germany; developments included steel, chemicals, precision machinery, and electronics",
    "China's program of internal reform in the 1860s and 1870s, based on vigorous application of Confucian principles and limited borrowing from the West",
    "Leader of revolt in South American colonies against Spanish rule",
    "A system of public or direct worker ownership of the means of production such as the mills to make cloth or the machinery and land needed to mine coal",
    "Ottoman reforms during 1839-1876 after Mahmud that addressed corruption, education, laws, and updated the legal system",
    "French Enlightenment writer, historian and philosopher famous for his advocacy of civil liberties, including freedom of religion, free trade and separation of church and state",
    "Powerful Japanese family business organizations like the conglomerates in the United States",
    "The desire of Jews to reestablish an independent homeland where their ancestors had lived in the Middle East"
]

terms = [
    " ", "abbasid caliphate",
    "al-andalus",
    "angkor wat",
    "aztec empire",
    "bhakti movement",
    "bushido",
    "byzantine empire",
    "caesaropapism",
    "china's economic revolution",
    "chu nom",
    "confucianism",
    "constantinople",
    "crusades",
    "daoism",
    "eastern orthodox christianity",
    "european renaissance",
    "foot binding",
    "great zimbabwe",
    "hangul",
    "hangzhou",
    "hinduism",
    "house of wisdom",
    "inca empire",
    "judaism",
    "kievan rus",
    "mahayana buddhism",
    "maya civilization",
    "merchant",
    "missionary",
    "ottoman empire",
    "roman catholic church",
    "seljuk turkic empire",
    "song dynasty",
    "sufi",
    "theravada buddhism",
    "western christendom",
    "american web",
    "arabian camel",
    "chaco phenomenon",
    "ghana",
    "mali",
    "pochteca",
    "sand roads",
    "sea roads",
    "silk roads",
    "srivijaya",
    "swahili civilization",
    "timbuktu",
    "trans-saharan slave trade",
    "west african civilization",
    "zheng he",
    "absolutism",
    "castes",
    "daimyo",
    "divine right",
    "gunpowder empires",
    "gutenberg printing press",
    "henry viii",
    "indulgences",
    "istanbul",
    "janissaries",
    "jizya",
    "manchus",
    "martin luther",
    "mehmet ii",
    "mughal empire",
    "ninety-five theses",
    "ottoman empire",
    "protestant reformation",
    "qing empire",
    "safavid empire",
    "shia",
    "sikhism",
    "suleiman the magnificent",
    "sunni",
    "tamerlane",
    "african diaspora",
    "asante empire",
    "atlantic circuit",
    "aztec empire",
    "barbary pirates",
    "bartolome de las casas",
    "capitalism",
    "cartography",
    "cash crop",
    "charter companies",
    "chattel slavery",
    "christopher columbus",
    "city of potosi",
    "columbian exchange",
    "commercial revolution",
    "conquistadors",
    "creole",
    "dutch east india company",
    "dutch west india company",
    "engenhos",
    "encomienda",
    "ferdinand magellan",
    "francisco pizarro",
    "galleons",
    "glorious revolution",
    "henry the navigator",
    "hispanola",
    "indentured servant",
    "iroquois confederacy",
    "jamestown",
    "joint-stock companies",
    "maratha empire",
    "maritime empires",
    "maroon wars",
    "mercantilism",
    "mestizos",
    "middle passage",
    "ming dynasty",
    "mit'a system",
    "monopolies",
    "mulatto",
    "new amsterdam",
    "new france",
    "new spain",
    "northwest passage",
    "omani-european rivalry",
    "peninsulares",
    "plantations",
    "puritans",
    "quebec",
    "royal african company",
    "smallpox",
    "syncretism",
    "time of troubles",
    "trading post empire",
    "transatlantic slave trade",
    "treaty of tordesillas",
    "triangular trade",
    "vasco da gama",
    "viceroyalty",
    "abolitionism",
    "adam smith",
    "agricultural revolution",
    "bastille",
    "bourgeoisie",
    "capital",
    "capitalism",
    "communism",
    "declaration of the rights of man",
    "division of labor",
    "enlightenment",
    "hong kong and shanghai banking corporation",
    "hundred days of reform",
    "industrial revolution",
    "industrialization",
    "jean-jacques rousseau",
    "john locke",
    "karl marx",
    "labor unions",
    "laissez-faire",
    "mary wollstonecraft",
    "meiji restoration",
    "monopoly",
    "muhammed ali",
    "nationalism",
    "new zealand wars",
    "otto von bismarck",
    "philosophers",
    "proletariat",
    "propaganda movement",
    "realpolitik",
    "reign of terror",
    "second industrial revolution",
    "self-strengthening movement",
    "simon bolivar",
    "socialism",
    "tanzimat",
    "voltaire",
    "zaibatsu",
    "zionism"
]

while run:
    generatable_numbers = []
    for number in range(177):
        generatable_numbers.append(number)
    generatable_numbers.remove(0)
    
    unit1_points = 0
    unit2_points = 0
    unit3_points = 0
    unit4_points = 0
    unit5_points = 0
    points = 0
    total = 0

    study = str(input("Would you like to study? "))
    if study.lower() == "yes":
        unit1 = str(input("Do you want words from Unit 1? "))
        unit2 = str(input("Do you want words from Unit 2? "))
        unit3 = str(input("Do you want words from Unit 3? "))
        unit4 = str(input("Do you want words from Unit 4? "))
        unit5 = str(input("Do you want words from Unit 5? "))
        
        studying = True
        while studying:
            if unit1.lower() == "no" and unit2.lower() == "no" and unit3.lower() == "no" and unit4.lower() == "no" and unit5.lower() == "no":
                print("Why did you say no for all of them?")
                wait(0.75)
                print("You can't study now.")
                studying = False
                run = False
                maxtotal = 200
                generated_defintion = 200
            
            elif unit1.lower() == "no" and unit2.lower() == "no" and unit3.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(137, 176)
                maxtotal = 40
            elif unit1.lower() == "no" and unit2.lower() == "no" and unit3.lower() == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(77, 136)
                maxtotal = 60
            elif unit1.lower() == "no" and unit2.lower() == "no" and unit5.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(52, 76)
                maxtotal = 25
            elif unit1.lower() == "no" and unit5.lower() == "no" and unit3.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(37, 51)
                maxtotal = 15
            elif unit5.lower() == "no" and unit2.lower() == "no" and unit3.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(1, 36)
                maxtotal = 36
            
            elif unit1.lower() == "no" and unit2.lower == "no" and unit3.lower() == "no":
                generated_defintion = random.randint(77, 176)
                maxtotal = 100
            elif unit1.lower() == "no" and unit2.lower == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(52, 76), (137, 176)]))
                maxtotal = 65
            elif unit1.lower() == "no" and unit2.lower == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(52, 136)
                maxtotal = 85
            elif unit1.lower() == "no" and unit3.lower == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(37, 51), (137, 176)]))
                maxtotal = 55
            elif unit1.lower() == "no" and unit3.lower == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (77, 136)]))
                maxtotal = 75
            elif unit1.lower() == "no" and unit4.lower == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(37, 76)
                maxtotal = 40
            elif unit2.lower() == "no" and unit3.lower == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (137, 176)]))
                maxtotal = 76
            elif unit2.lower() == "no" and unit3.lower == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (77, 136)]))
                maxtotal = 96
            elif unit2.lower() == "no" and unit4.lower == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (52, 76)]))
                maxtotal = 61
            elif unit3.lower() == "no" and unit4.lower == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(1, 51)
                maxtotal = 51
            
            elif unit1.lower() == "no" and unit2.lower() == "no":
                generated_defintion = random.randint(52, 176)
                maxtotal = 125
            elif unit1.lower() == "no" and unit3.lower() == "no":
                generated_defintion = random.randint(*random.choice([(37, 51), (77, 176)]))
                maxtotal = 115
            elif unit1.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(37, 76), (137, 176)]))
                maxtotal = 80
            elif unit1.lower() == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(52, 136)
                maxtotal = 100
            elif unit2.lower() == "no" and unit3.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (77, 176)]))
                maxtotal = 136
            elif unit2.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (52, 76), (137, 176)]))
                maxtotal = 101
            elif unit2.lower() == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (52, 136)]))
                maxtotal = 121
            elif unit3.lower() == "no" and unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 51), (137, 176)]))
                maxtotal = 91
            elif unit3.lower() == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 51), (77, 136)]))
                maxtotal = 111
            elif unit4.lower() == "no" and unit5.lower() == "no":
                generated_defintion = random.randint(1, 76)
                maxtotal = 76
            
            elif unit1.lower() == "no":
                generated_defintion = random.randint(37, 176)
                maxtotal = 140
            elif unit2.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 36), (52, 176)]))
                maxtotal = 161
            elif unit3.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 51), (77, 176)]))
                maxtotal = 151
            elif unit4.lower() == "no":
                generated_defintion = random.randint(*random.choice([(1, 76), (137, 176)]))
                maxtotal = 116
            elif unit5.lower() == "no":
                generated_defintion = random.randint(1, 136)
                maxtotal = 136
            
            else:
                generated_defintion = random.randint(1, 176)
                maxtotal = 176

            for picked_number in range(177):
                if generated_defintion == picked_number and picked_number in generatable_numbers:
                    print(definitions[picked_number])
                    correct_word = terms[picked_number]
                    result()
                    if picked_number <= 36:
                        unit1_track()
                    elif picked_number >= 37 and picked_number <= 51:
                        unit2_track()
                    elif picked_number >= 52 and picked_number <= 76:
                        unit3_track()
                    elif picked_number >= 77 and picked_number <= 136:
                        unit4_track()
                    elif picked_number >= 137 and picked_number <= 176:
                        unit5_track()
                    generatable_numbers.remove(picked_number)
            
            if total == maxtotal:
                print("You finished studying!")
                wait(0.75)
                points_percent = round((points/total)*100, 2)
                print("You got " + str(points) + " out of " + str(total) + " terms correct!")
                wait(0.75)
                print("That's " + str(points_percent) + "%!")
                studying = False
                wait(0.75)
                if unit1.lower() != "no":
                    unit1_percent = round((unit1_points/36)*100, 2)
                    print("Unit 1: " + str(unit1_points) + "/36, " + str(unit1_percent) + "%")
                    wait(0.75)
                if unit2.lower() != "no":
                    unit2_percent = round((unit2_points/15)*100, 2)
                    print("Unit 2: " + str(unit2_points) + "/15, " + str(unit2_percent) + "%")
                    wait(0.75)
                if unit3.lower() != "no":
                    unit3_percent = round((unit3_points/25)*100, 2)
                    print("Unit 3: " + str(unit3_points) + "/25, " + str(unit3_percent) + "%")
                    wait(0.75)
                if unit4.lower() != "no":
                    unit4_percent = round((unit4_points/60)*100, 2)
                    print("Unit 4: " + str(unit4_points) + "/60, " + str(unit4_percent) + "%")
                    wait(0.75)
                if unit5.lower() != "no":
                    unit5_percent = round((unit5_points/40)*100, 2)
                    print("Unit 5: " + str(unit5_points) + "/40, " + str(unit5_percent) + "%")
                    wait(0.75)
                wait(1.25)
    elif study.lower() == "no":
        print("I hope you already studied!")
        run = False
    else:
        wait(0.5)
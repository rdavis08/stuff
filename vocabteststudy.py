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
    clear_1 = False
    clear_2 = False
    clear_3 = False
    clear_4 = False
    clear_5 = False
    clear_6 = False
    clear_7 = False
    clear_8 = False
    clear_9 = False
    clear_10 = False
    clear_11 = False
    clear_12 = False
    clear_13 = False
    clear_14 = False
    clear_15 = False
    clear_16 = False
    clear_17 = False
    clear_18 = False
    clear_19 = False
    clear_20 = False
    clear_21 = False
    clear_22 = False
    clear_23 = False
    clear_24 = False
    clear_25 = False
    clear_26 = False
    clear_27 = False
    clear_28 = False
    clear_29 = False
    clear_30 = False
    clear_31 = False
    clear_32 = False
    clear_33 = False
    clear_34 = False
    clear_35 = False
    clear_36 = False
    clear_37 = False
    clear_38 = False
    clear_39 = False
    clear_40 = False
    clear_41 = False
    clear_42 = False
    clear_43 = False
    clear_44 = False
    clear_45 = False
    clear_46 = False
    clear_47 = False
    clear_48 = False
    clear_49 = False
    clear_50 = False
    clear_51 = False
    clear_52 = False
    clear_53 = False
    clear_54 = False
    clear_55 = False
    clear_56 = False
    clear_57 = False
    clear_58 = False
    clear_59 = False
    clear_60 = False
    clear_61 = False
    clear_62 = False
    clear_63 = False
    clear_64 = False
    clear_65 = False
    clear_66 = False
    clear_67 = False
    clear_68 = False
    clear_69 = False
    clear_70 = False
    clear_71 = False
    clear_72 = False
    clear_73 = False
    clear_74 = False
    clear_75 = False
    clear_76 = False
    clear_77 = False
    clear_78 = False
    clear_79 = False
    clear_80 = False
    clear_81 = False
    clear_82 = False
    clear_83 = False
    clear_84 = False
    clear_85 = False
    clear_86 = False
    clear_87 = False
    clear_88 = False
    clear_89 = False
    clear_90 = False
    clear_91 = False
    clear_92 = False
    clear_93 = False
    clear_94 = False
    clear_95 = False
    clear_96 = False
    clear_97 = False
    clear_98 = False
    clear_99 = False
    clear_100 = False
    clear_101 = False
    clear_102 = False
    clear_103 = False
    clear_104 = False
    clear_105 = False
    clear_106 = False
    clear_107 = False
    clear_108 = False
    clear_109 = False
    clear_110 = False
    clear_111 = False
    clear_112 = False
    clear_113 = False
    clear_114 = False
    clear_115 = False
    clear_116 = False
    clear_117 = False
    clear_118 = False
    clear_119 = False
    clear_120 = False
    clear_121 = False
    clear_122 = False
    clear_123 = False
    clear_124 = False
    clear_125 = False
    clear_126 = False
    clear_127 = False
    clear_128 = False
    clear_129 = False
    clear_130 = False
    clear_131 = False
    clear_132 = False
    clear_133 = False
    clear_134 = False
    clear_135 = False
    clear_136 = False
    clear_137 = False
    clear_138 = False
    clear_139 = False
    clear_140 = False
    clear_141 = False
    clear_142 = False
    clear_143 = False
    clear_144 = False
    clear_145 = False
    clear_146 = False
    clear_147 = False
    clear_148 = False
    clear_149 = False
    clear_150 = False
    clear_151 = False
    clear_152 = False
    clear_153 = False
    clear_154 = False
    clear_155 = False
    clear_156 = False
    clear_157 = False
    clear_158 = False
    clear_159 = False
    clear_160 = False
    clear_161 = False
    clear_162 = False
    clear_163 = False
    clear_164 = False
    clear_165 = False
    clear_166 = False
    clear_167 = False
    clear_168 = False
    clear_169 = False
    clear_170 = False
    clear_171 = False
    clear_172 = False
    clear_173 = False
    clear_174 = False
    clear_175 = False
    clear_176 = False

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
                generated_defintion = 0
            
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

            if generated_defintion == 1 and clear_1 == False:
                print(definitions[1])
                correct_word = terms[1]
                result()
                unit1_track()
                clear_1 = True
            elif generated_defintion == 2 and clear_2 == False:
                print(definitions[2])
                correct_word = terms[2]
                result()
                unit1_track()
                clear_2 = True
            elif generated_defintion == 3 and clear_3 == False:
                print(definitions[3])
                correct_word = terms[3]
                result()
                unit1_track()
                clear_3 = True
            elif generated_defintion == 4 and clear_4 == False:
                print(definitions[4])
                correct_word = terms[4]
                result()
                unit1_track()
                clear_4 = True
            elif generated_defintion == 5 and clear_5 == False:
                print(definitions[5])
                correct_word = terms[5]
                result()
                unit1_track()
                clear_5 = True
            elif generated_defintion == 6 and clear_6 == False:
                print(definitions[6])
                correct_word = terms[6]
                result()
                unit1_track()
                clear_6 = True
            elif generated_defintion == 7 and clear_7 == False:
                print(definitions[7])
                correct_word = terms[7]
                result()
                unit1_track()
                clear_7 = True
            elif generated_defintion == 8 and clear_8 == False:
                print(definitions[8])
                correct_word = terms[8]
                result()
                unit1_track()
                clear_8 = True
            elif generated_defintion == 9 and clear_9 == False:
                print(definitions[9])
                correct_word = terms[9]
                result()
                unit1_track()
                clear_9 = True
            elif generated_defintion == 10 and clear_10 == False:
                print(definitions[10])
                correct_word = terms[10]
                result()
                unit1_track()
                clear_10 = True
            elif generated_defintion == 11 and clear_11 == False:
                print(definitions[11])
                correct_word = terms[11]
                result()
                unit1_track()
                clear_11 = True
            elif generated_defintion == 12 and clear_12 == False:
                print(definitions[12])
                correct_word = terms[12]
                result()
                unit1_track()
                clear_12 = True
            elif generated_defintion == 13 and clear_13 == False:
                print(definitions[13])
                correct_word = terms[13]
                result()
                unit1_track()
                clear_13 = True
            elif generated_defintion == 14 and clear_14 == False:
                print(definitions[14])
                correct_word = terms[14]
                result()
                unit1_track()
                clear_14 = True
            elif generated_defintion == 15 and clear_15 == False:
                print(definitions[15])
                correct_word = terms[15]
                result()
                unit1_track()
                clear_15 = True
            elif generated_defintion == 16 and clear_16 == False:
                print(definitions[16])
                correct_word = terms[16]
                result()
                unit1_track()
                clear_16 = True
            elif generated_defintion == 17 and clear_17 == False:
                print(definitions[17])
                correct_word = terms[17]
                result()
                unit1_track()
                clear_17 = True
            elif generated_defintion == 18 and clear_18 == False:
                print(definitions[18])
                correct_word = terms[18]
                result()
                unit1_track()
                clear_18 = True
            elif generated_defintion == 19 and clear_19 == False:
                print(definitions[19])
                correct_word = terms[19]
                result()
                unit1_track()
                clear_19 = True
            elif generated_defintion == 20 and clear_20 == False:
                print(definitions[20])
                correct_word = terms[20]
                result()
                unit1_track()
                clear_20 = True
            elif generated_defintion == 21 and clear_21 == False:
                print(definitions[21])
                correct_word = terms[21]
                result()
                unit1_track()
                clear_21 = True
            elif generated_defintion == 22 and clear_22 == False:
                print(definitions[22])
                correct_word = terms[22]
                result()
                unit1_track()
                clear_22 = True
            elif generated_defintion == 23 and clear_23 == False:
                print(definitions[23])
                correct_word = terms[23]
                result()
                unit1_track()
                clear_23 = True
            elif generated_defintion == 24 and clear_24 == False:
                print(definitions[24])
                correct_word = terms[24]
                result()
                unit1_track()
                clear_24 = True
            elif generated_defintion == 25 and clear_25 == False:
                print(definitions[25])
                correct_word = terms[25]
                result()
                unit1_track()
                clear_25 = True
            elif generated_defintion == 26 and clear_26 == False:
                print(definitions[26])
                correct_word = terms[26]
                result()
                unit1_track()
                clear_26 = True
            elif generated_defintion == 27 and clear_27 == False:
                print(definitions[27])
                correct_word = terms[27]
                result()
                unit1_track()
                clear_27 = True
            elif generated_defintion == 28 and clear_28 == False:
                print(definitions[28])
                correct_word = terms[28]
                result()
                unit1_track()
                clear_28 = True
            elif generated_defintion == 29 and clear_29 == False:
                print(definitions[29])
                correct_word = terms[29]
                result()
                unit1_track()
                clear_29 = True
            elif generated_defintion == 30 and clear_30 == False:
                print(definitions[30])
                correct_word = terms[30]
                result()
                unit1_track()
                clear_30 = True
            elif generated_defintion == 31 and clear_31 == False:
                print(definitions[31])
                correct_word = terms[31]
                result()
                unit1_track()
                clear_31 = True
            elif generated_defintion == 32 and clear_32 == False:
                print(definitions[32])
                correct_word = terms[32]
                result()
                unit1_track()
                clear_32 = True
            elif generated_defintion == 33 and clear_33 == False:
                print(definitions[33])
                correct_word = terms[33]
                result()
                unit1_track()
                clear_33 = True
            elif generated_defintion == 34 and clear_34 == False:
                print(definitions[34])
                correct_word = terms[34]
                result()
                unit1_track()
                clear_34 = True
            elif generated_defintion == 35 and clear_35 == False:
                print(definitions[35])
                correct_word = terms[35]
                result()
                unit1_track()
                clear_35 = True
            elif generated_defintion == 36 and clear_36 == False:
                print(definitions[36])
                correct_word = terms[36]
                result()
                unit1_track()
                clear_36 = True
            elif generated_defintion == 37 and clear_37 == False:
                print(definitions[37])
                correct_word = terms[37]
                result()
                unit2_track()
                clear_37 = True
            elif generated_defintion == 38 and clear_38 == False:
                print(definitions[38])
                correct_word = terms[38]
                result()
                unit2_track()
                clear_38 = True
            elif generated_defintion == 39 and clear_39 == False:
                print(definitions[39])
                correct_word = terms[39]
                result()
                unit2_track()
                clear_39 = True
            elif generated_defintion == 40 and clear_40 == False:
                print(definitions[40])
                correct_word = terms[40]
                result()
                unit2_track()
                clear_40 = True
            elif generated_defintion == 41 and clear_41 == False:
                print(definitions[41])
                correct_word = terms[41]
                result()
                unit2_track()
                clear_41 = True
            elif generated_defintion == 42 and clear_42 == False:
                print(definitions[42])
                correct_word = terms[42]
                result()
                unit2_track()
                clear_42 = True
            elif generated_defintion == 43 and clear_43 == False:
                print(definitions[43])
                correct_word = terms[43]
                result()
                unit2_track()
                clear_43 = True
            elif generated_defintion == 44 and clear_44 == False:
                print(definitions[44])
                correct_word = terms[44]
                result()
                unit2_track()
                clear_44 = True
            elif generated_defintion == 45 and clear_45 == False:
                print(definitions[45])
                correct_word = terms[45]
                result()
                unit2_track()
                clear_45 = True
            elif generated_defintion == 46 and clear_46 == False:
                print(definitions[46])
                correct_word = terms[46]
                result()
                unit2_track()
                clear_46 = True
            elif generated_defintion == 47 and clear_47 == False:
                print(definitions[47])
                correct_word = terms[47]
                result()
                unit2_track()
                clear_47 = True
            elif generated_defintion == 48 and clear_48 == False:
                print(definitions[48])
                correct_word = terms[48]
                result()
                unit2_track()
                clear_48 = True
            elif generated_defintion == 49 and clear_49 == False:
                print(definitions[49])
                correct_word = terms[49]
                result()
                unit2_track()
                clear_49 = True
            elif generated_defintion == 50 and clear_50 == False:
                print(definitions[50])
                correct_word = terms[50]
                result()
                unit2_track()
                clear_50 = True
            elif generated_defintion == 51 and clear_51 == False:
                print(definitions[51])
                correct_word = terms[51]
                result()
                unit2_track()
                clear_51 = True
            elif generated_defintion == 52 and clear_52 == False:
                print(definitions[52])
                correct_word = terms[52]
                result()
                unit3_track()
                clear_52 = True
            elif generated_defintion == 53 and clear_53 == False:
                print(definitions[53])
                correct_word = terms[53]
                result()
                unit3_track()
                clear_53 = True
            elif generated_defintion == 54 and clear_54 == False:
                print(definitions[54])
                correct_word = terms[54]
                result()
                unit3_track()
                clear_54 = True
            elif generated_defintion == 55 and clear_55 == False:
                print(definitions[55])
                correct_word = terms[55]
                result()
                unit3_track()
                clear_55 = True
            elif generated_defintion == 56 and clear_56 == False:
                print(definitions[56])
                correct_word = terms[56]
                result()
                unit3_track()
                clear_56 = True
            elif generated_defintion == 57 and clear_57 == False:
                print(definitions[57])
                correct_word = terms[57]
                result()
                unit3_track()
                clear_57 = True
            elif generated_defintion == 58 and clear_58 == False:
                print(definitions[58])
                correct_word = terms[58]
                result()
                unit3_track()
                clear_58 = True
            elif generated_defintion == 59 and clear_59 == False:
                print(definitions[59])
                correct_word = terms[59]
                result()
                unit3_track()
                clear_59 = True
            elif generated_defintion == 60 and clear_60 == False:
                print(definitions[60])
                correct_word = terms[60]
                result()
                unit3_track()
                clear_60 = True
            elif generated_defintion == 61 and clear_61 == False:
                print(definitions[61])
                correct_word = terms[61]
                result()
                unit3_track()
                clear_61 = True
            elif generated_defintion == 62 and clear_62 == False:
                print(definitions[62])
                correct_word = terms[62]
                result()
                unit3_track()
                clear_62 = True
            elif generated_defintion == 63 and clear_63 == False:
                print(definitions[63])
                correct_word = terms[63]
                result()
                unit3_track()
                clear_63 = True
            elif generated_defintion == 64 and clear_64 == False:
                print(definitions[64])
                correct_word = terms[64]
                result()
                unit3_track()
                clear_64 = True
            elif generated_defintion == 65 and clear_65 == False:
                print(definitions[65])
                correct_word = terms[65]
                result()
                unit3_track()
                clear_65 = True
            elif generated_defintion == 66 and clear_66 == False:
                print(definitions[66])
                correct_word = terms[66]
                result()
                unit3_track()
                clear_66 = True
            elif generated_defintion == 67 and clear_67 == False:
                print(definitions[67])
                correct_word = terms[67]
                result()
                unit3_track()
                clear_67 = True
            elif generated_defintion == 68 and clear_68 == False:
                print(definitions[68])
                correct_word = terms[68]
                result()
                unit3_track()
                clear_68 = True
            elif generated_defintion == 69 and clear_69 == False:
                print(definitions[69])
                correct_word = terms[69]
                result()
                unit3_track()
                clear_69 = True
            elif generated_defintion == 70 and clear_70 == False:
                print(definitions[70])
                correct_word = terms[70]
                result()
                unit3_track()
                clear_70 = True
            elif generated_defintion == 71 and clear_71 == False:
                print(definitions[71])
                correct_word = terms[71]
                result()
                unit3_track()
                clear_71 = True
            elif generated_defintion == 72 and clear_72 == False:
                print(definitions[72])
                correct_word = terms[72]
                result()
                unit3_track()
                clear_72 = True
            elif generated_defintion == 73 and clear_73 == False:
                print(definitions[73])
                correct_word = terms[73]
                result()
                unit3_track()
                clear_73 = True
            elif generated_defintion == 74 and clear_74 == False:
                print(definitions[74])
                correct_word = terms[74]
                result()
                unit3_track()
                clear_74 = True
            elif generated_defintion == 75 and clear_75 == False:
                print(definitions[75])
                correct_word = terms[75]
                result()
                unit3_track()
                clear_75 = True
            elif generated_defintion == 76 and clear_76 == False:
                print(definitions[76])
                correct_word = terms[76]
                result()
                unit3_track()
                clear_76 = True
            elif generated_defintion == 77 and clear_77 == False:
                print(definitions[77])
                correct_word = terms[77]
                result()
                unit4_track()
                clear_77 = True
            elif generated_defintion == 78 and clear_78 == False:
                print(definitions[78])
                correct_word = terms[78]
                result()
                unit4_track()
                clear_78 = True
            elif generated_defintion == 79 and clear_79 == False:
                print(definitions[79])
                correct_word = terms[79]
                result()
                unit4_track()
                clear_79 = True
            elif generated_defintion == 80 and clear_80 == False:
                print(definitions[80])
                correct_word = terms[80]
                result()
                unit4_track()
                clear_80 = True
            elif generated_defintion == 81 and clear_81 == False:
                print(definitions[81])
                correct_word = terms[81]
                result()
                unit4_track()
                clear_81 = True
            elif generated_defintion == 82 and clear_82 == False:
                print(definitions[82])
                correct_word = terms[82]
                result()
                unit4_track()
                clear_82 = True
            elif generated_defintion == 83 and clear_83 == False:
                print(definitions[83])
                correct_word = terms[83]
                result()
                unit4_track()
                clear_83 = True
            elif generated_defintion == 84 and clear_84 == False:
                print(definitions[84])
                correct_word = terms[84]
                result()
                unit4_track()
                clear_84 = True
            elif generated_defintion == 85 and clear_85 == False:
                print(definitions[85])
                correct_word = terms[85]
                result()
                unit4_track()
                clear_85 = True
            elif generated_defintion == 86 and clear_86 == False:
                print(definitions[86])
                correct_word = terms[86]
                result()
                unit4_track()
                clear_86 = True
            elif generated_defintion == 87 and clear_87 == False:
                print(definitions[87])
                correct_word = terms[87]
                result()
                unit4_track()
                clear_87 = True
            elif generated_defintion == 88 and clear_88 == False:
                print(definitions[88])
                correct_word = terms[88]
                result()
                unit4_track()
                clear_88 = True
            elif generated_defintion == 89 and clear_89 == False:
                print(definitions[89])
                correct_word = terms[89]
                result()
                unit4_track()
                clear_89 = True
            elif generated_defintion == 90 and clear_90 == False:
                print(definitions[90])
                correct_word = terms[90]
                result()
                unit4_track()
                clear_90 = True
            elif generated_defintion == 91 and clear_91 == False:
                print(definitions[91])
                correct_word = terms[91]
                result()
                unit4_track()
                clear_91 = True
            elif generated_defintion == 92 and clear_92 == False:
                print(definitions[92])
                correct_word = terms[92]
                result()
                unit4_track()
                clear_92 = True
            elif generated_defintion == 93 and clear_93 == False:
                print(definitions[93])
                correct_word = terms[93]
                result()
                unit4_track()
                clear_93 = True
            elif generated_defintion == 94 and clear_94 == False:
                print(definitions[94])
                correct_word = terms[94]
                result()
                unit4_track()
                clear_94 = True
            elif generated_defintion == 95 and clear_95 == False:
                print(definitions[95])
                correct_word = terms[95]
                result()
                unit4_track()
                clear_95 = True
            elif generated_defintion == 96 and clear_96 == False:
                print(definitions[96])
                correct_word = terms[96]
                result()
                unit4_track()
                clear_96 = True
            elif generated_defintion == 97 and clear_97 == False:
                print(definitions[97])
                correct_word = terms[97]
                result()
                unit4_track()
                clear_97 = True
            elif generated_defintion == 98 and clear_98 == False:
                print(definitions[98])
                correct_word = terms[98]
                result()
                unit4_track()
                clear_98 = True
            elif generated_defintion == 99 and clear_99 == False:
                print(definitions[99])
                correct_word = terms[99]
                result()
                unit4_track()
                clear_99 = True
            elif generated_defintion == 100 and clear_100 == False:
                print(definitions[100])
                correct_word = terms[100]
                result()
                unit4_track()
                clear_100 = True
            elif generated_defintion == 101 and clear_101 == False:
                print(definitions[101])
                correct_word = terms[101]
                result()
                unit4_track()
                clear_101 = True
            elif generated_defintion == 102 and clear_102 == False:
                print(definitions[102])
                correct_word = terms[102]
                result()
                unit4_track()
                clear_102 = True
            elif generated_defintion == 103 and clear_103 == False:
                print(definitions[103])
                correct_word = terms[103]
                result()
                unit4_track()
                clear_103 = True
            elif generated_defintion == 104 and clear_104 == False:
                print(definitions[104])
                correct_word = terms[104]
                result()
                unit4_track()
                clear_104 = True
            elif generated_defintion == 105 and clear_105 == False:
                print(definitions[105])
                correct_word = terms[105]
                result()
                unit4_track()
                clear_105 = True
            elif generated_defintion == 106 and clear_106 == False:
                print(definitions[106])
                correct_word = terms[106]
                result()
                unit4_track()
                clear_106 = True
            elif generated_defintion == 107 and clear_107 == False:
                print(definitions[107])
                correct_word = terms[107]
                result()
                unit4_track()
                clear_107 = True
            elif generated_defintion == 108 and clear_108 == False:
                print(definitions[108])
                correct_word = terms[108]
                result()
                unit4_track()
                clear_108 = True
            elif generated_defintion == 109 and clear_109 == False:
                print(definitions[109])
                correct_word = terms[109]
                result()
                unit4_track()
                clear_109 = True
            elif generated_defintion == 110 and clear_110 == False:
                print(definitions[110])
                correct_word = terms[110]
                result()
                unit4_track()
                clear_110 = True
            elif generated_defintion == 111 and clear_111 == False:
                print(definitions[111])
                correct_word = terms[111]
                result()
                unit4_track()
                clear_111 = True
            elif generated_defintion == 112 and clear_112 == False:
                print(definitions[112])
                correct_word = terms[112]
                result()
                unit4_track()
                clear_112 = True
            elif generated_defintion == 113 and clear_113 == False:
                print(definitions[113])
                correct_word = terms[113]
                result()
                unit4_track()
                clear_113 = True
            elif generated_defintion == 114 and clear_114 == False:
                print(definitions[114])
                correct_word = terms[114]
                result()
                unit4_track()
                clear_114 = True
            elif generated_defintion == 115 and clear_115 == False:
                print(definitions[115])
                correct_word = terms[115]
                result()
                unit4_track()
                clear_115 = True
            elif generated_defintion == 116 and clear_116 == False:
                print(definitions[116])
                correct_word = terms[116]
                result()
                unit4_track()
                clear_116 = True
            elif generated_defintion == 117 and clear_117 == False:
                print(definitions[117])
                correct_word = terms[117]
                result()
                unit4_track()
                clear_117 = True
            elif generated_defintion == 118 and clear_118 == False:
                print(definitions[118])
                correct_word = terms[118]
                result()
                unit4_track()
                clear_118 = True
            elif generated_defintion == 119 and clear_119 == False:
                print(definitions[119])
                correct_word = terms[119]
                result()
                unit4_track()
                clear_119 = True
            elif generated_defintion == 120 and clear_120 == False:
                print(definitions[120])
                correct_word = terms[120]
                result()
                unit4_track()
                clear_120 = True
            elif generated_defintion == 121 and clear_121 == False:
                print(definitions[121])
                correct_word = terms[121]
                result()
                unit4_track()
                clear_121 = True
            elif generated_defintion == 122 and clear_122 == False:
                print(definitions[122])
                correct_word = terms[122]
                result()
                unit4_track()
                clear_122 = True
            elif generated_defintion == 123 and clear_123 == False:
                print(definitions[123])
                correct_word = terms[123]
                result()
                unit4_track()
                clear_123 = True
            elif generated_defintion == 124 and clear_124 == False:
                print(definitions[124])
                correct_word = terms[124]
                result()
                unit4_track()
                clear_124 = True
            elif generated_defintion == 125 and clear_125 == False:
                print(definitions[125])
                correct_word = terms[125]
                result()
                unit4_track()
                clear_125 = True
            elif generated_defintion == 126 and clear_126 == False:
                print(definitions[126])
                correct_word = terms[126]
                result()
                unit4_track()
                clear_126 = True
            elif generated_defintion == 127 and clear_127 == False:
                print(definitions[127])
                correct_word = terms[127]
                result()
                unit4_track()
                clear_127 = True
            elif generated_defintion == 128 and clear_128 == False:
                print(definitions[128])
                correct_word = terms[128]
                result()
                unit4_track()
                clear_128 = True
            elif generated_defintion == 129 and clear_129 == False:
                print(definitions[129])
                correct_word = terms[129]
                result()
                unit4_track()
                clear_129 = True
            elif generated_defintion == 130 and clear_130 == False:
                print(definitions[130])
                correct_word = terms[130]
                result()
                unit4_track()
                clear_130 = True
            elif generated_defintion == 131 and clear_131 == False:
                print(definitions[131])
                correct_word = terms[131]
                result()
                unit4_track()
                clear_131 = True
            elif generated_defintion == 132 and clear_132 == False:
                print(definitions[132])
                correct_word = terms[132]
                result()
                unit4_track()
                clear_132 = True
            elif generated_defintion == 133 and clear_133 == False:
                print(definitions[133])
                correct_word = terms[133]
                result()
                unit4_track()
                clear_133 = True
            elif generated_defintion == 134 and clear_134 == False:
                print(definitions[134])
                correct_word = terms[134]
                result()
                unit4_track()
                clear_134 = True
            elif generated_defintion == 135 and clear_135 == False:
                print(definitions[135])
                correct_word = terms[135]
                result()
                unit4_track()
                clear_135 = True
            elif generated_defintion == 136 and clear_136 == False:
                print(definitions[136])
                correct_word = terms[136]
                result()
                unit4_track()
                clear_136 = True
            elif generated_defintion == 137 and clear_137 == False:
                print(definitions[137])
                correct_word = terms[137]
                result()
                unit5_track()
                clear_137 = True
            elif generated_defintion == 138 and clear_138 == False:
                print(definitions[138])
                correct_word = terms[138]
                result()
                unit5_track()
                clear_138 = True
            elif generated_defintion == 139 and clear_139 == False:
                print(definitions[139])
                correct_word = terms[139]
                result()
                unit5_track()
                clear_139 = True
            elif generated_defintion == 140 and clear_140 == False:
                print(definitions[140])
                correct_word = terms[140]
                result()
                unit5_track()
                clear_140 = True
            elif generated_defintion == 141 and clear_141 == False:
                print(definitions[141])
                correct_word = terms[141]
                result()
                unit5_track()
                clear_141 = True
            elif generated_defintion == 142 and clear_142 == False:
                print(definitions[142])
                correct_word = terms[142]
                result()
                unit5_track()
                clear_142 = True
            elif generated_defintion == 143 and clear_143 == False:
                print(definitions[143])
                correct_word = terms[143]
                result()
                unit5_track()
                clear_143 = True
            elif generated_defintion == 144 and clear_144 == False:
                print(definitions[144])
                correct_word = terms[144]
                result()
                unit5_track()
                clear_144 = True
            elif generated_defintion == 145 and clear_145 == False:
                print(definitions[145])
                correct_word = terms[145]
                result()
                unit5_track()
                clear_145 = True
            elif generated_defintion == 146 and clear_146 == False:
                print(definitions[146])
                correct_word = terms[146]
                result()
                unit5_track()
                clear_146 = True
            elif generated_defintion == 147 and clear_147 == False:
                print(definitions[147])
                correct_word = terms[147]
                result()
                unit5_track()
                clear_147 = True
            elif generated_defintion == 148 and clear_148 == False:
                print(definitions[148])
                correct_word = terms[148]
                result()
                unit5_track()
                clear_148 = True
            elif generated_defintion == 149 and clear_149 == False:
                print(definitions[149])
                correct_word = terms[149]
                result()
                unit5_track()
                clear_149 = True
            elif generated_defintion == 150 and clear_150 == False:
                print(definitions[150])
                correct_word = terms[150]
                result()
                unit5_track()
                clear_150 = True
            elif generated_defintion == 151 and clear_151 == False:
                print(definitions[151])
                correct_word = terms[151]
                result()
                unit5_track()
                clear_151 = True
            elif generated_defintion == 152 and clear_152 == False:
                print(definitions[152])
                correct_word = terms[152]
                result()
                unit5_track()
                clear_152 = True
            elif generated_defintion == 153 and clear_153 == False:
                print(definitions[153])
                correct_word = terms[153]
                result()
                unit5_track()
                clear_153 = True
            elif generated_defintion == 154 and clear_154 == False:
                print(definitions[154])
                correct_word = terms[154]
                result()
                unit5_track()
                clear_154 = True
            elif generated_defintion == 155 and clear_155 == False:
                print(definitions[155])
                correct_word = terms[155]
                result()
                unit5_track()
                clear_155 = True
            elif generated_defintion == 156 and clear_156 == False:
                print(definitions[156])
                correct_word = terms[156]
                result()
                unit5_track()
                clear_156 = True
            elif generated_defintion == 157 and clear_157 == False:
                print(definitions[157])
                correct_word = terms[157]
                result()
                unit5_track()
                clear_157 = True
            elif generated_defintion == 158 and clear_158 == False:
                print(definitions[158])
                correct_word = terms[158]
                result()
                unit5_track()
                clear_158 = True
            elif generated_defintion == 159 and clear_159 == False:
                print(definitions[159])
                correct_word = terms[159]
                result()
                unit5_track()
                clear_159 = True
            elif generated_defintion == 160 and clear_160 == False:
                print(definitions[160])
                correct_word = terms[160]
                result()
                unit5_track()
                clear_160 = True
            elif generated_defintion == 161 and clear_161 == False:
                print(definitions[161])
                correct_word = terms[161]
                result()
                unit5_track()
                clear_161 = True
            elif generated_defintion == 162 and clear_162 == False:
                print(definitions[162])
                correct_word = terms[162]
                result()
                unit5_track()
                clear_162 = True
            elif generated_defintion == 163 and clear_163 == False:
                print(definitions[163])
                correct_word = terms[163]
                result()
                unit5_track()
                clear_163 = True
            elif generated_defintion == 164 and clear_164 == False:
                print(definitions[164])
                correct_word = terms[164]
                result()
                unit5_track()
                clear_164 = True
            elif generated_defintion == 165 and clear_165 == False:
                print(definitions[165])
                correct_word = terms[165]
                result()
                unit5_track()
                clear_165 = True
            elif generated_defintion == 166 and clear_166 == False:
                print(definitions[166])
                correct_word = terms[166]
                result()
                unit5_track()
                clear_166 = True
            elif generated_defintion == 167 and clear_167 == False:
                print(definitions[167])
                correct_word = terms[167]
                result()
                unit5_track()
                clear_167 = True
            elif generated_defintion == 168 and clear_168 == False:
                print(definitions[168])
                correct_word = terms[168]
                result()
                unit5_track()
                clear_168 = True
            elif generated_defintion == 169 and clear_169 == False:
                print(definitions[169])
                correct_word = terms[169]
                result()
                unit5_track()
                clear_169 = True
            elif generated_defintion == 170 and clear_170 == False:
                print(definitions[170])
                correct_word = terms[170]
                result()
                unit5_track()
                clear_170 = True
            elif generated_defintion == 171 and clear_171 == False:
                print(definitions[171])
                correct_word = terms[171]
                result()
                unit5_track()
                clear_171 = True
            elif generated_defintion == 172 and clear_172 == False:
                print(definitions[172])
                correct_word = terms[172]
                result()
                unit5_track()
                clear_172 = True
            elif generated_defintion == 173 and clear_173 == False:
                print(definitions[173])
                correct_word = terms[173]
                result()
                unit5_track()
                clear_173 = True
            elif generated_defintion == 174 and clear_174 == False:
                print(definitions[174])
                correct_word = terms[174]
                result()
                unit5_track()
                clear_174 = True
            elif generated_defintion == 175 and clear_175 == False:
                print(definitions[175])
                correct_word = terms[175]
                result()
                unit5_track()
                clear_175 = True
            elif generated_defintion == 176 and clear_176 == False:
                print(definitions[176])
                correct_word = terms[176]
                result()
                unit5_track()
                clear_176 = True
            
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

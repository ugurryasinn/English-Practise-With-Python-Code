import random


word_list = [
	["bright","parlak"],
	["certain","kesin"],
	["light","hafif"],
	["large","geniş"],
	["thin","ince"],
	["adverse","tersi"],
	["actual","gerçeği"],
	["conclusive","son hal"],
	["strange","yabancı"],
	["relative","ilgili"],
	["excellent", "mükemmel"],
	["brilliant","zeki"],
	["evil", "kötü şeytani"],
	["mighty","abartı güçlü"],
	["spicy","baharatlı"],
	["sincere","samimi içten"],
	["eager","hevesli"],
	["indestructible","yok edilemez"],
	["capable", "yeteneği olan"],
	["inefficient", "yetersiz"],
	["considerable", "düşünülebilir"],
	["miserable", "acınası"],
	["humble", "alçak gönüllü"],
	["fragile", "kırılgan"],
	["commercial", "ticari"],
	["deceptive", "aldatıcı"],
	["responsive", "hassas"],
	["reasonable", "makul, mantıklı"],
	["competitive", "rekabetçi"],
	["cruel", "acımasız"],
	["present", "mevcut olan"],
	["pregnant", "hamile"],
	["cautions", "dikkatli"],
	["fancy", "eğlenceli"],
	["wounded", "yaralı"],
	["ashamed", "utanmış"],
	["curious", "meraklı"],
	["shiny","parlak"],
	["worthy", "değerli"],
	["essential", "temel çok önemli"],
	["conscious", "bilinçli"],
	["greedy", "açgözlü"],
	["disable", "kısıtlı"],
	["convinced", "ikna edilmiş"],
	["pleasent", "memnun"],
	["tight", "sıkı dar"],
	["conventional", "geleneksel"],
	["arbitrary", "rastgele"],
	["allied", "dost"],
	["shameful", "utanılacak"],
	["desperate", "umutsuz"],
	["deaf", "sağır"],
	["genvine", "gerçek hakiki"],
	["clumsy", "beceriksiz"],
	["affordable", "karşılanabilir"],
	["fiscal", "parasal, maddi"],
	["permanent", "kalıcı"],
	["decisive", "karar verici"],
	["fascinated", "büyülenmiş"],
	["exceptional", "istisna"],
	["flexible", "esnek"],
	["backward", "gelişmemiş"],
	["sudden", "ani"],
	["fair", "adil"],
	["curly", "kıvırcık"],
	["elegant", "şık"],
	["concerned", "endişeli"],
	["advisable", "akla yatkın"],
	["awfull", "berbat"],
	["constant","sabit"],
	["familiar", "tanıdık"],
	["appropriate", "uygun"],
	["ridiculos", "gülünç"],
	["casual", "sıradar"],
	["tempreroy", "geçici"],
	["ancient", "antika"],
	["naked", "çıplak"],
	["accessible", "ulaşılabilir"],
	["native", "yerli"],
	["suitable", "müsait"],
	["spotless", "lekesiz"],
	["confident", "kesin"],
	["confidential", "gizli"],
	["odd", "tek, garip"],
	["bearable", "katlanılabilir"],
	["easy-going", "rahat"]
]
word_num=len(word_list)
correct_words=[]
print("Welcome To My English Practise Project\n")

def next_question(word_list):
	word = random.choice(word_list)
	print(f"'{word[0]}'")
	answer=input("What is the meaning of this word in Turkish? :")
	if word[1]==answer:
		print("Your answer is correct\n")
		correct_words.append([word[0],word[1]])
	else:
		print(f"False answer. Correct answer is '{word[1]}'\n")
	word_list.remove(word)

	if len(word_list)==0:
		print(f"Quiz is finished\nCorrect answer {len(correct_words)}/{word_num}")
	else:
		next_question(word_list=word_list)

next_question(word_list=word_list)





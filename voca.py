def WordSegmentation(Passage):
	RtnString=[];
	Word='';
	Analyze=False;
	Passage=Passage+' '; #使最后一个词也列入统计
	WordNet={"m":"am",
		"s":"is",
		"re":"are",
		"d":"would",
		"t":"not",
		"ll":"will",
		"ve":"have",
		"!us":"us"}
	for Letter in Passage:
		if Letter.isalpha()==True:
			Word=Word+str(Letter);
		elif Letter=="’" or Letter=="'":
			Analyze=True;
			PreviousWord=Word;
			Word='';
		else:
			if Analyze==False:
				if Word!='':
					RtnString.append(Word);
					Word='';
			else:
				try:
					WordNet[Word];
				except KeyError:
					try:
						PreviousWord[0];
					except IndexError:
						if Word=='clock': #排除o'clock
							PreviousWord="oclock";
							Word='';
						if PreviousWord!='':
							RtnString.append(PreviousWord);
						if Word!='':
							RtnString.append(Word);
					else:
						if Word=='' and PreviousWord[0].isupper()==False: #排除kids'和Dickens'
							if PreviousWord=='doin':
								PreviousWord='doing';
							else:
								PreviousWord=PreviousWord[0:-1];
							if PreviousWord!='':
								RtnString.append(PreviousWord);
						else:
							if Word=='clock': #排除o'clock
								PreviousWord="oclock";
								Word='';
							RtnString.append(PreviousWord);
							if Word!='':
								RtnString.append(Word);
				else:
					try:
						PreviousWord[-1];
					except IndexError:
						pass;
					else:
						if Word=='t' and PreviousWord[-1]=='n': #排除Doesn't,won't等
							PreviousWord=PreviousWord[0:-1];
					if Word=='s' and PreviousWord=='Let': #排除Let's
						PreviousWord='let';
						Word="!us";
					if Word=='s' and PreviousWord=='let': #排除let's
						PreviousWord='let';
						Word="!us";
					if PreviousWord=='wo':
						PreviousWord='will'; #恢复Won't->wo not->will not
					if PreviousWord!='':
						RtnString.append(PreviousWord);
					RtnString.append(WordNet[Word]);
				Analyze=False;
				Word='';
	return RtnString;

x=[];
c=[];
g=[];
t=[];
xo=[];
co=[];
go=[];
to=[];
print('loading pointing images');
pointvoca={};
with open('point.csv') as point:
	for line in point:
		line=line.replace('\n','');
		if line!='':
			split=line.split(',');
			pointvoca[split[0]]=split[1];
print('finish loading pointing images');
print('loading vocabulary list');
with open('x.txt') as txt:
	for line in txt:
		line=line.replace('\n','');
		if line!='':
			try:
				pointvoca[line];
			except:	
				xo.append(line);
			else:
				xo.append(pointvoca[line]);
with open('c.txt') as txt:
	for line in txt:
		line=line.replace('\n','');
		if line!='':
			try:
				pointvoca[line];
			except:	
				co.append(line);
			else:
				co.append(pointvoca[line]);
with open('g.txt') as txt:
	for line in txt:
		line=line.replace('\n','');
		if line!='':
			try:
				pointvoca[line];
			except:	
				go.append(line);
			else:
				go.append(pointvoca[line]);
with open('t.txt') as txt:
	for line in txt:
		line=line.replace('\n','');
		if line!='':
			try:
				pointvoca[line];
			except:	
				to.append(line);
			else:
				to.append(pointvoca[line]);
for word in xo:
	if word in co:
		co.remove(word);
	if word in go:
		go.remove(word);
	if word in to:
		to.remove(word);
for word in co:
	if word in go:
		go.remove(word);
	if word in to:
		to.remove(word);
for word in go:
	if word in to:
		to.remove(word);
print('loading okay');
import DGStorage as DGS;
import urllib.parse;
import time;
a=DGS.DGStorage()
a.select('textstat');
i=0;
end=False;
while end==False:
	i+=1;
	res=a.fetch(20,(i-1)*20);
	if len(res)==0:
		end=True;
	for item in res:
		#print(item["uid"]);
		content=urllib.parse.unquote_plus(item["content"]);
		#print(str(WordSegmentation(content)));
		ws=WordSegmentation(content);
		wordlist=[];
		string='';
		for word in ws:
			if word.lower() not in wordlist:
				wordlist.append(word);
			try:
				string=string+','+pointvoca[urllib.parse.quote_plus(word)];
			except:
				string=string+','+word;
		#a.setprop(item["uid"],"words",string);
		newwl=[];
		for word in wordlist:
			try:
				newwl.append(pointvoca[word]);
			except:
				newwl.append(word);
		xiaoxue=[];
		chuzhong=[];
		gaozhong=[];
		tuofu=[];
		qita=[];
		for word in newwl:
			if word in xo:
				if word not in xiaoxue:
					xiaoxue.append(word);
			if word in co:
				if word not in chuzhong:
					chuzhong.append(word);
			if word in go:
				if word not in gaozhong:
					gaozhong.append(word);
			if word in to:
				if word not in tuofu:
					tuofu.append(word);
		for word in newwl:
			if word not in xiaoxue and word not in chuzhong and word not in gaozhong and word not in tuofu:
				qita.append(word);
		string='';
		xiaoxue.sort();
		con=0;
		for word in xiaoxue:
			con+=1;
			if string!='':
				string=string+','+word;
			else:
				string=word;
		a.setprop(item["uid"],"xiaoxue",string);
		a.setprop(item["uid"],"xiaoxueci",con);
		print('set '+item["uid"]);

		string='';
		chuzhong.sort();
		con=0;
		for word in chuzhong:
			con+=1;
			if string!='':
				string=string+','+word;
			else:
				string=word;
		a.setprop(item["uid"],"chuzhong",string);
		a.setprop(item["uid"],"chuzhongci",con);
		print('set '+item["uid"]);

		string='';
		gaozhong.sort();
		con=0;
		for word in gaozhong:
			con+=1;
			if string!='':
				string=string+','+word;
			else:
				string=word;
		a.setprop(item["uid"],"gaozhong",string);
		a.setprop(item["uid"],"gaozhongci",con);
		print('set '+item["uid"]);

		string='';
		tuofu.sort();
		con=0;
		for word in tuofu:
			con+=1;
			if string!='':
				string=string+','+word;
			else:
				string=word;
		a.setprop(item["uid"],"tuofu",string);
		a.setprop(item["uid"],"tuofuci",con);
		print('set '+item["uid"]);

		string='';
		qita.sort();
		con=0;
		for word in qita:
			con+=1;
			if string!='':
				string=string+','+word;
			else:
				string=word;
		a.setprop(item["uid"],"qita",string);
		a.setprop(item["uid"],"qitaci",con);
		print('set '+item["uid"]);

import gtts
import playsound

musica="""Shinzou wo Sasageyo!
kore ijou no jigoku wa nai darou to shinjitakatta
saredo jinrui saiaku no hi wa itsumo toutotsu ni
tobira wo tataku oto wa taezu hidoku busahou de
manekarezaru saiyaku no hi wa akumu no you ni

sugishi hi wo uragiru mono
yatsura wa kuchiku subeki teki da
ano hi donna kao de hitomi de
oretachi wo mitsumeteita?

nani wo sutereba akuma wo mo shinogeru
inochi sae tamashii sae kesshite oshiku nado wa nai

sasageyo sasageyo
shinzou wo sasageyo
subete no gisei wa
ima kono toki no tame ni

sasageyo sasageyo
shinzou wo sasageyo
susumu beki mirai wo
sono te de kirihirake

sugishi hi wo itsuwaru mono
yatsura wa zouo subeki teki da
ano hi donna koe de kotoba de
oretachi wo katatteita

nani wo manabeba akuma wo mo hofureru?
gijutsu demo senjutsu demo
subete muda ni nado shinai

sasageyo sasageyo
shinzou wo sasageyo
subete no doryoku wa
ima kono toki no tame ni

sasageyo sasageyo
shinzou wo sasageyo
utau beki shouri wo
sono te de tsukamitore

etai no shirenai bakemono ga
hito to nita tsura wo shiteyagaru
kono yo kara ippiki nokorazu
yatsura wo kuchiku shiteyaru

saisho ni iidashita no wa dare ka?
sonna koto oboechainai ga
wasurerarenai ikari ga aru
kanarazu kuchiku shiteyaru

aa erabikuita michi no saki wa
donna basho ni tsunagatteiru?
tada sasagererareta inochi wo
kate ni saku toutoki higan no Sieg
yakusoku no chi wa rakuen no hate

ano hi jinrui wa omoidashita
yatsura ni shihai sareteita kyoufu wo
torikago no naka ni torawareteita kutsujoku wo
tasogare wo yumiya wa kakeru tsubasa wo seoi
sono kiseki ga jiyuu e no michi to naru

sasageyo sasageyo
shinzou wo sasageyo
subete no kunan wa
ima kono toki no tame ni

sasageyo sasageyo
shinzou wo sasageyo
hakanaki inochi wo
moeru yumiya ni kaete

sasageyo sasageyo
shinzou wo sasageyo
hokoru beki kiseki wo
sono mi de egakidase"""
        
frase_PT = gtts.gTTS(musica,lang='pt-br')
frase_EN = gtts.gTTS(musica,lang='en')
frase_JP = gtts.gTTS(musica,lang='ja')

frase_PT.save('audioPT.mp3')
frase_EN.save('audioEN.mp3')
frase_JP.save('audioJP.mp3')

#playsound.playsound('audio.mp3')
